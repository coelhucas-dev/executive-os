# Setup guiado por IA

Se voce nao quer lidar com Git, Python ou terminal, o fluxo principal deve ser feito pelo Claude.

## Como funciona

1. Voce cola o prompt de onboarding no Claude.
2. O Claude instala ou atualiza o bloco gerenciado do Business OS no proprio `CLAUDE.md`.
   Como apoio, o installer tambem mantem uma copia em `~/.claude/CLAUDE.business-os.md`.
3. O Claude faz uma entrevista curta para entender como voce opera.
4. O Claude cria ou adapta a estrutura inicial do vault.
5. A partir dai, pedidos em linguagem natural sobre empresa, app, reunioes, follow-ups e rotina devem passar pelo Business OS.

## O que o Claude deve fazer

- preservar instrucoes suas que ja existirem no `CLAUDE.md`
- atualizar apenas o bloco gerenciado do Business OS
- manter o conteudo canonico do Business OS separado em `CLAUDE.business-os.md`
- usar skills do Business OS quando o caminho correto nao estiver obvio
- usar Obsidian CLI para consultar e materializar contexto real do vault
- evitar responder do nada sobre estado operacional sem verificar o sistema

## O que ele vai perguntar

O onboarding precisa descobrir pelo menos:

- que tipo de negocio voce opera
- qual e o seu papel
- quantas threads de reuniao, follow-up e delegacao voce carrega
- quais responsabilidades de life admin precisam entrar
- se conteudo e marca pessoal entram na estrutura inicial

## Regra mais importante

Se o assunto tem consequencia real na sua operacao ou na sua vida, o Claude deve tratar isso como Business OS mesmo que voce nao fale a palavra "vault".
