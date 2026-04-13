---
name: sb-vault
description: "Use esta skill para qualquer pedido envolvendo um vault Obsidian do Business OS. Use esta skill sempre que o usuário falar sobre o vault, notas, pastas, dashboards, templates, reuniões, empresas, pessoas, projetos, tarefas, decisões, conteúdo, encaminhamento de notas, recuperação de contexto, organização de informação ou criação da estrutura do Business OS."
---

# Business OS Vault

Use esta skill como roteador principal para pedidos sobre o Business OS no Obsidian.

## Quando usar

- O usuário menciona um vault do Business OS ou do Second Brain sem nomear uma `sb-` skill específica.
- O usuário pede para organizar, criar, encaminhar, recuperar, capturar ou estruturar notas no Obsidian.
- O usuário fala sobre reuniões, empresas, pessoas, projetos, tarefas, decisões, conteúdo, dashboards, templates ou sobre onde uma nota deve ficar.
- A skill especialista correta não está óbvia a partir do primeiro pedido.

## O que fazer

1. Leia `references/router.md`.
2. Decida qual comportamento especialista é necessário:
   - `sb-core` para arquitetura e estrutura
   - `sb-create-vault` para bootstrap e geração
   - `sb-capture` para captura em inbox e triagem
   - `sb-meeting-ingestion` para reuniões e transcrições
   - `sb-routing-retrieval` para colocação de notas e retrieval restrito
   - `sb-tasks-followups` para próximos passos e trabalho delegado
   - `sb-decisions` para notas de decisão duráveis
   - `sb-content-ops` para fluxos de conteúdo
3. Aplique as regras do Business OS:
   - pastas definem ownership
   - links definem relationships
   - use notas atômicas
   - evite notas-dump

## Regra de retrieval

Comece pelo dashboard ou home note mais próximo, depois faça uma busca restrita por pasta, e então leia apenas as notas atômicas necessárias.

## Nota sobre o Obsidian CLI

Ao usar o Obsidian CLI, aponte para o vault com `obsidian vault='{{OBSIDIAN_VAULT_NAME}}' ...`. Não use a forma posicional `obsidian "{{OBSIDIAN_VAULT_NAME}}" ...`.
