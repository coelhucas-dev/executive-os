# Roteador do Business OS

Este é o roteador coringa para pedidos do Business OS.

Nota de CLI pública:

- use `obsidian vault='{{OBSIDIAN_VAULT_NAME}}' ...`
- não use `obsidian "{{OBSIDIAN_VAULT_NAME}}" ...`

Mapeie a linguagem comum do usuário para as skills especialistas:

- "crie o vault", "bootstrap", "configure a estrutura" -> `sb-create-vault`
- "onde isso deve ficar?", "organize isso", "ache a pasta certa" -> `sb-routing-retrieval`
- "capture isso", "salve isso", "coloque isso no meu vault" -> `sb-capture`
- "meeting", "transcript", "call", "summary", "action items desta call" -> `sb-meeting-ingestion`
- "task", "follow-up", "delegado", "waiting for" -> `sb-tasks-followups`
- "decision", "decision log", "documente esta escolha" -> `sb-decisions`
- "content", "draft", "plataforma", "campanha", "ideia" -> `sb-content-ops`
- "como este vault funciona?", "como isso é estruturado?" -> `sb-core`
