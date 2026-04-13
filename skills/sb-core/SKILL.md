---
name: sb-core
description: "Use esta skill para pedidos sobre como um vault Obsidian do Business OS funciona: estrutura do vault, pastas, dashboards, templates, metadados, tipos de nota, regras de notas atômicas e onde cada nota deve ficar. Use esta skill sempre que o usuário falar sobre como o vault é organizado, como as notas devem ser estruturadas, como reuniões, empresas, pessoas, projetos, tarefas, decisões ou conteúdo devem viver no vault, ou como a IA deve navegar e recuperar contexto com eficiência."
---

# Business OS Core

Use esta skill para entender o vault do Business OS antes de agir. Leia `references/second-brain-core.md` quando precisar do modelo de pastas, das regras de metadados, das regras de ownership das notas ou da disciplina de retrieval.

## Regras centrais

- Pastas definem ownership.
- Links definem relationships.
- Use uma nota por entidade, evento ou decisão.
- Evite arquivos-dump cumulativos como `Meetings.md`, `Decisions.md` ou `Tasks.md`.
- Prefira dashboards, home notes e buscas restritas por pasta antes de leituras amplas.
- Mantenha a estrutura e as chaves de frontmatter em inglês; títulos e corpos das notas podem usar qualquer idioma.

## Quando usar

- O usuário pergunta como o vault é organizado.
- O usuário quer saber onde uma nota deve ficar.
- O Codex precisa decidir entre múltiplas pastas candidatas.
- Uma skill de workflow precisa da arquitetura-base antes de criar ou mover notas.

## O que não fazer

- Não invente modelos alternativos de pastas dentro de skills especialistas.
- Não colapse múltiplos históricos em uma única nota grande.
- Não amplie o retrieval se um dashboard ou uma busca restrita por pasta já for suficiente.
