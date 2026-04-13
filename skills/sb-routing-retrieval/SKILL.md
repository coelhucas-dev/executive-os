---
name: sb-routing-retrieval
description: "Use esta skill para pedidos sobre onde uma nota deve ficar em um vault Obsidian do Business OS e como a IA deve buscar, encaminhar ou recuperar o conjunto mínimo de notas relevantes. Use esta skill sempre que o usuário perguntar onde colocar algo, qual pasta usar, como organizar uma nota, como buscar no vault ou como recuperar apenas o contexto necessário."
---

# Business OS Routing and Retrieval

## Roteamento

- Roteie por ownership, não por conveniência.
- Se uma nota for sobre uma pessoa, empresa, projeto, reunião, decisão, conteúdo, rotina ou frente de operação pessoal, coloque-a no lugar dono desse assunto.
- Se a ownership não estiver clara, use `00 Inbox`.

## Retrieval

1. Comece pelo dashboard ou home note mais próximo.
2. Busque na pasta candidata mais restrita.
3. Leia apenas as notas atômicas necessárias para a tarefa.
4. Pare de ampliar a busca quando já houver contexto suficiente para agir.

## Nota sobre o Obsidian CLI

Ao usar o Obsidian CLI, aponte para o vault com `vault='{{OBSIDIAN_VAULT_NAME}}'` em vez da sintaxe quebrada por argumento posicional.
