# Business OS for Obsidian

Business OS e um sistema operacional pessoal e executivo para empresarios brasileiros que vivem no meio de reunioes, follow-ups, decisoes, projetos, conteudo e coordenacao.

Em vez de usar o Obsidian como um bloco de notas generico, este repo cria um ambiente operacional estruturado para a IA ler pouco, entender melhor e agir com consistencia.

## O problema

Empresario nao perde contexto porque faltou um app. Perde contexto porque a operacao fica espalhada em:

- WhatsApp, email e conversas soltas
- reunioes que viram historico morto
- tarefas delegadas que somem
- decisoes que nao ficam registradas
- projetos sem ownership claro
- assistentes de IA que respondem bem, mas nao atualizam o sistema real

## A proposta

Business OS organiza a vida operacional em um vault do Obsidian que a IA consegue usar de verdade.

O modelo base e simples:

- pastas definem ownership
- links definem relationships
- dashboards orientam navegacao
- notas atomicas guardam contexto duravel
- a IA deve buscar pouco, agir com precisao e deixar rastro no sistema

## Para quem e

- founders e operators
- donos de negocio
- executivos com muitas frentes abertas
- pessoas que precisam acompanhar reunioes, delegacao, waiting-for e decisoes sem depender da memoria
- quem quer usar Claude ou Codex como copiloto operacional, e nao como chatbot generico

## O que voce ganha

- continuidade real entre reunioes, projetos e follow-ups
- menos contexto perdido em chat
- menos resposta generica da IA
- mais clareza sobre o que esta aberto, delegado e parado
- uma estrutura que a IA consegue consultar e atualizar com disciplina

## O que vem no v1 publico

- especificacao publica do vault
- templates e dashboards operacionais
- skills `sb-` para Codex
- adapter oficial para `Claude`
- adapter oficial para `Codex`
- instalador com configuracao publica de vault name e vault path
- prompt few-shot de onboarding para setup guiado por IA

Integracoes experimentais:

- `Cursor`
- `Antigravity`

## Jeitos de começar

### 1. Jeito recomendado: setup guiado por IA

Se voce nao quer lidar com Git, Python ou terminal, use o fluxo guiado pelo Claude:

1. Abra o Claude.
2. Cole o [Prompt few-shot de onboarding para Claude](prompts/few-shot-onboarding-claude.md).
3. Deixe o Claude instalar o bloco gerenciado, entrevistar voce rapidamente e montar a estrutura inicial.

Esse e o fluxo principal de produto para usuario final.

### 2. Jeito tecnico: installer local

Se voce quer montar tudo manualmente no ambiente local, rode:

```bash
python3 installer/install.py \
  --tool codex \
  --tool claude \
  --vault-path /tmp/business-os \
  --generate-vault
```

Dry-run:

```bash
python3 installer/install.py \
  --dry-run \
  --tool codex \
  --tool claude \
  --vault-path /tmp/business-os \
  --generate-vault
```

Se quiser usar um nome de vault diferente do nome da pasta, passe `--vault-name`.

## Como o sistema funciona no dia a dia

1. Capture tudo o que estiver solto em `00 Inbox`.
2. Transforme reunioes em notas de reuniao.
3. Extraia follow-ups e decisoes em notas separadas quando fizer sentido.
4. Use `Today` e `This Week` como paineis de execucao.
5. Trate empresa, pessoa, projeto, decisao e tarefa como objetos operacionais separados.

Regra central: a IA nao deve apenas responder. Ela deve consultar ou atualizar o sistema quando o assunto tiver consequencia real na sua operacao.

## Diferencial do Business OS

Nao e so um template de Obsidian.

Tambem nao e so um prompt para IA.

E a combinacao de:

- estrutura publica de vault
- regras de roteamento e retrieval
- prompts e adapters para ferramentas de IA
- uso disciplinado de contexto operacional real

Sem isso, a IA conversa. Com isso, ela opera.

## Notas de produto

- o lancamento publico atual e Brazil-first em linguagem e onboarding
- nomes de pastas e metadados ficam em ingles para manter consistencia estrutural
- titulos e corpo das notas podem ficar em portugues
- `Claude` e `Codex` sao os canais prioritarios no v1

## Estrutura do repo

- `spec/`: especificacao publica do vault e manifest
- `templates/`: templates e dashboards
- `skills/`: skills `sb-` para uso com Codex
- `adapters/`: payloads de instrucao por ferramenta
- `installer/`: geracao de vault e instalacao local
- `prompts/`: prompts de onboarding e operacao
- `docs/`: guias de uso

## Documentacao principal

- [Setup guiado por IA](docs/setup-guiado-por-ia.md)
- [Primeira semana](docs/primeira-semana.md)
- [Como a IA opera](docs/como-a-ia-opera.md)
- [Como usar com IA](docs/uso-com-ia.md)
- [Operações do dia a dia](docs/operacoes-do-dia-a-dia.md)
- [Prompt few-shot de onboarding para Claude](prompts/few-shot-onboarding-claude.md)
- [Exemplos few-shot de onboarding para Claude](prompts/few-shot-onboarding-claude-examples.md)
- [Prompt operacional base](prompts/one-shot-business-os.md)
