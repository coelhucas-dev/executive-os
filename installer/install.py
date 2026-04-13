#!/usr/bin/env python3
import argparse
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SPEC_DIR = ROOT / "spec"
SKILLS_DIR = ROOT / "skills"
ADAPTERS_DIR = ROOT / "adapters"
TEMPLATES_DIR = ROOT / "templates"
MANIFEST_PATH = SPEC_DIR / "vault-manifest.json"
SUPPORTED_TOOLS = ["codex", "claude"]
EXPERIMENTAL_TOOLS = ["cursor", "antigravity"]
CLAUDE_MANAGED_BLOCK_START = "<!-- BEGIN BUSINESS OS MANAGED BLOCK -->"
CLAUDE_MANAGED_BLOCK_END = "<!-- END BUSINESS OS MANAGED BLOCK -->"


def load_manifest():
    return json.loads(MANIFEST_PATH.read_text())


def resolve_vault_name(vault_path: Path | None, vault_name: str | None) -> str | None:
    if vault_name:
        return vault_name
    if vault_path:
        return vault_path.name
    return None


def render_text(content: str, vault_name: str | None = None, target_name: str | None = None) -> str:
    if "{{PLATFORM}}" in content and target_name:
        platform = Path(target_name).parts[-2]
        content = content.replace("{{PLATFORM}}", platform)
    cli_vault_name = vault_name or "your-vault-name"
    content = content.replace("{{OBSIDIAN_VAULT_NAME}}", cli_vault_name)
    return content


def ensure_dir(path: Path, dry_run: bool):
    if dry_run:
        print(f"[dry-run] mkdir -p {path}")
        return
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str, overwrite: bool, dry_run: bool):
    if path.exists() and not overwrite:
        print(f"[skip] {path}")
        return
    if dry_run:
        print(f"[dry-run] write {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def upsert_managed_block(existing: str, block: str) -> str:
    start = existing.find(CLAUDE_MANAGED_BLOCK_START)
    end = existing.find(CLAUDE_MANAGED_BLOCK_END)
    if start != -1 and end != -1 and end > start:
        end += len(CLAUDE_MANAGED_BLOCK_END)
        before = existing[:start].rstrip()
        after = existing[end:].lstrip()
        sections = [section for section in [before, block.strip(), after] if section]
        return "\n\n".join(sections) + "\n"
    stripped = existing.rstrip()
    if not stripped:
        return block.strip() + "\n"
    return stripped + "\n\n" + block.strip() + "\n"


def should_render_text_file(path: Path) -> bool:
    return path.suffix in {".md", ".mdc", ".json"}


def copy_tree(src: Path, dst: Path, overwrite: bool, dry_run: bool, vault_name: str | None = None):
    if not src.exists():
        raise FileNotFoundError(src)
    if dry_run:
        print(f"[dry-run] copy {src} -> {dst}")
        return
    if dst.exists() and overwrite:
        shutil.rmtree(dst)
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.rglob("*"):
        rel = item.relative_to(src)
        target = dst / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            if target.exists() and not overwrite:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            if should_render_text_file(item):
                rendered = render_text(item.read_text(), vault_name=vault_name, target_name=str(rel))
                target.write_text(rendered)
            else:
                shutil.copy2(item, target)


def generate_vault(vault_path: Path, overwrite: bool, dry_run: bool):
    manifest = load_manifest()
    ensure_dir(vault_path, dry_run)
    for folder in manifest["folders"]:
        ensure_dir(vault_path / folder, dry_run)

    obsidian_dir = vault_path / ".obsidian"
    ensure_dir(obsidian_dir, dry_run)
    daily_cfg = {
        "folder": manifest["obsidian_config"]["daily_notes_folder"],
        "format": manifest["obsidian_config"]["daily_notes_format"],
        "template": "99 Templates/Daily Note.md",
        "autorun": False,
    }
    templates_cfg = {"folder": manifest["obsidian_config"]["templates_folder"]}
    write_text(obsidian_dir / "daily-notes.json", json.dumps(daily_cfg, indent=2) + "\n", overwrite, dry_run)
    write_text(obsidian_dir / "templates.json", json.dumps(templates_cfg, indent=2) + "\n", overwrite, dry_run)

    for target, template_name in manifest["seed_files"].items():
        template_path = TEMPLATES_DIR / template_name
        content = render_text(template_path.read_text(), target_name=target)
        write_text(vault_path / target, content, overwrite, dry_run)


def install_codex(overwrite: bool, dry_run: bool, vault_name: str | None):
    target = Path.home() / ".codex" / "skills"
    ensure_dir(target, dry_run)
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if skill_dir.is_dir():
            copy_tree(skill_dir, target / skill_dir.name, overwrite, dry_run, vault_name=vault_name)
    agents_target = Path.home() / ".codex" / "AGENTS.md"
    agents_content = render_text((ADAPTERS_DIR / "codex" / "AGENTS.md").read_text(), vault_name=vault_name)
    write_text(agents_target, agents_content, overwrite, dry_run)


def install_claude(overwrite: bool, dry_run: bool, vault_name: str | None):
    target = Path.home() / ".claude" / "CLAUDE.md"
    block = render_text((ADAPTERS_DIR / "claude" / "CLAUDE.md").read_text(), vault_name=vault_name)
    helper_target = Path.home() / ".claude" / "CLAUDE.business-os.md"
    write_text(helper_target, block, overwrite, dry_run)
    if dry_run:
        action = "write" if overwrite or not target.exists() else "merge"
        print(f"[dry-run] {action} managed Business OS block in {target}")
        return
    if not target.exists() or overwrite:
        write_text(target, block, True, dry_run)
        return
    merged = upsert_managed_block(target.read_text(), block)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(merged)


def install_cursor(overwrite: bool, dry_run: bool, vault_name: str | None):
    target = Path.home() / ".cursor" / "rules" / "second-brain.mdc"
    content = render_text((ADAPTERS_DIR / "cursor" / "second-brain.mdc").read_text(), vault_name=vault_name)
    write_text(target, content, overwrite, dry_run)


def install_antigravity(overwrite: bool, dry_run: bool, vault_name: str | None):
    target = Path.home() / ".antigravity" / "SECOND_BRAIN.md"
    content = render_text((ADAPTERS_DIR / "antigravity" / "SECOND_BRAIN.md").read_text(), vault_name=vault_name)
    write_text(target, content, overwrite, dry_run)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Instala o Business OS no Obsidian e configura os adapters oficiais para Codex e Claude."
    )
    parser.add_argument("--tool", action="append", choices=SUPPORTED_TOOLS + EXPERIMENTAL_TOOLS, default=[])
    parser.add_argument("--vault-path", type=Path)
    parser.add_argument("--vault-name")
    parser.add_argument("--generate-vault", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    vault_name = resolve_vault_name(args.vault_path, args.vault_name)
    if not args.tool and not args.generate_vault:
        raise SystemExit("Nada para fazer. Use --tool e/ou --generate-vault.")
    if args.generate_vault and not args.vault_path:
        raise SystemExit("--generate-vault requer --vault-path.")

    if "codex" in args.tool:
        install_codex(args.overwrite, args.dry_run, vault_name)
    if "claude" in args.tool:
        install_claude(args.overwrite, args.dry_run, vault_name)
    if "cursor" in args.tool:
        print("[aviso] cursor está em suporte experimental no v1 público.")
        install_cursor(args.overwrite, args.dry_run, vault_name)
    if "antigravity" in args.tool:
        print("[aviso] antigravity está em suporte experimental no v1 público.")
        install_antigravity(args.overwrite, args.dry_run, vault_name)
    if args.generate_vault:
        generate_vault(args.vault_path, args.overwrite, args.dry_run)


if __name__ == "__main__":
    main()
