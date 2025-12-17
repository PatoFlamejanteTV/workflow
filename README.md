# Fluxo de Trabalho

Documentação do fluxo de trabalho da Nogo apps.

## Visão Geral

Utilizamos um método similar ao Kanban, que consiste em 3 padrões:

1. Comunicação.
2. Organização.
3. Controle de Versão.

# Slack (Comunicação)

- brainstorm_10min: Reunião semanal com projetos do github, issues do github e codacy em 10min.
 1. Issues com a etiqueta "stuck" (travado)
 2. Sprints
 3. Próximas funcionalidades
- change_request: Se você quiser solicitar uma mudança no projeto sobre algo em andamento.
- general: Assuntos gerais.
- github: Integração com o github.
- reviews_codacy: Novas revisões do codacy.
- visitors_slaask: Sala de bate-papo para visitantes do nosso site.

# Projetos do Github (Organização)

- Cartões (Cards)
 1. Você pode usar projetos para criar um fluxo de trabalho e organizar as tarefas e a equipe em notas.
 2. Cada tarefa deve ser possível de ser feita em mais de 2 horas e menos de 6 horas; caso contrário, divida ou junte algumas tarefas em uma só.
 3. Só pode ir para frente (puxado para a próxima coluna) e todas as colunas podem ter apenas 6 tarefas de uma vez.
 4. Todo título de cartão precisa ter a data atual.
 5. Nossa meta é o mínimo de 6 tarefas semanais.
 6. Toda sexta-feira limpamos a coluna "done" (feito).
 7. Toda vez que eu mudo um cartão de coluna para outra coluna, tenho que mudar a data para a atual.
- Issues
 1. Toda nota que você cria tem que ser convertida em uma issue quando você a coloca na coluna "To do" (A fazer) e completa os dados.
 2. Os dados da issue são: responsável (assign), marco (milestone - estágio do projeto), etiqueta (label - tipo) e descrição.
 3. A etiqueta "Stuck" é usada se alguma tarefa está estática por mais de 3 dias na mesma coluna ou algo não foi aprovado na revisão, o que ganha prioridade e a equipe discute no slack. Quando você resolver a issue travada, mude a etiqueta de "stuck" para "priority" (prioridade).
 4. Novo (new), substituir (replace), bug e prioridade (priority) são os outros tipos.
 5. Toda issue tem que se tornar um commit na sua branch.
 6. Podemos ver em "pulse" e nos gráficos informações sobre nossas issues e pulls.
 7. Quando você faz uma revisão em uma issue, você pode usar o emoji "like" ou "dislike" (este precisa de um comentário) para simbolizar o que você acha e pode comentar ao longo das atualizações da issue.
 8. Quando deletamos issues na sexta-feira da coluna "done", precisamos fechá-las.

## Colunas

- Backlog: Aqui discutimos nossas ideias, dificuldades e planos. Uma vez por semana fazemos a reunião de brainstorm.
- To do: Aqui temos todas as tarefas (issues) aprovadas para fazer com descrições, etiquetas, responsáveis e marcos.
- Doing (testing): Aqui mostra o que está em progresso.
- Done: A tarefa está finalizada e agora pode esperar por revisão.
- Review (testing): Aqui analisa-se o código ao receber um pull request e fazem-se comentários nas linhas, cria-se uma revisão e discute-se sobre mudanças, solicita-se mudanças ou aprova-se com um ícone de like. Quando a revisão estiver completa, feche a issue e apague a issue da coluna.

# Controle de Versão

Trabalhe na sua branch e apenas quando seu trabalho estiver pronto tente um pull request, todo pull request precisa de uma descrição explicando o que mudou e por quê.

Ex: 

- O que mudou?

Exemplo de texto, exemplo de texto, Exemplo de texto, exemplo de texto, Exemplo de texto, exemplo de texto, Exemplo de texto, exemplo de texto, Exemplo de texto, exemplo de texto.

- Por quê?

Exemplo de texto, exemplo de texto, Exemplo de texto, exemplo de texto, Exemplo de texto, exemplo de texto, Exemplo de texto, exemplo de texto, Exemplo de texto, exemplo de texto.

## Lista de Verificação de Revisão de Código

A revisão precisa ser feita em 3 níveis:

1. Receber um pull request.
2. Teste do Codacy.
3. Teste de Build e teste de UI.
4. Teste de comparação com git ou github.
5. Aprovar (mudar para a coluna done) ou desaprovar (adicionar etiqueta "stuck").

Mais detalhes:

- Coluna "doing" e "review" precisam fazer esses testes.
- A pessoa que faz a revisão não pode ser a mesma que fez o código.

## Geral

- O código funciona?
- O código está limpo?
- O código está encapsulado e orientado a objetos?
- O código respeita padrões de projeto, material design e convenções android?
- Existe algo redundante ou desnecessário?
- O projeto está modulado com baixo acoplamento?
- Todos os métodos e variáveis estão comentados ou com escopo explícito.
- Algum log ou debug é desnecessário?
- Se o projeto precisa de alguma importação no gradle, máquina virtual e etc... toda a equipe precisa ser informada e criar uma documentação.
- O código comentado foi removido?
- A build funciona?
- A UI está funcionando em todos os dispositivos que deveria?
- O codacy vê algum problema no seu código que precisa ser consertado?

## Codacy

O codacy faz algumas revisões automáticas e nos dá uma melhor visão no código e a integração com o Travis faz a build online.

# Git

Você pode analisar no git local as diferenças com os truques abaixo deste tópico e no github (prioridade) quando criar um pull request.
Fazer a revisão no github é a melhor maneira de criar uma revisão pública. Você pode fazer comentários nas linhas do código, só use o git se precisar de uma análise mais profunda.
Não esqueça de sempre fazer um pull para o repositório local depois do push. Para você atualizar o master remoto antes de atualizar o master local.

## Truques para comparar e logs

- git diff (mostra as mudanças)
- git diff HEAD
- git diff --word-diff (mostra apenas as mudanças e não a linha toda)
- git diff --staged (mostra as mudanças na área de stage)
- git --stat (mostra apenas os arquivos alterados)
- git checkout (muda branches)
- git log (mostra commits de autores com datas)
- git log --oneline (mostra apenas as descrições dos commits)
- git log --stat (vê os arquivos que mudaram também)

## Possíveis erros

1. Se você tem um repositório dentro do seu repositório.
2. Se você não tem acesso à chave do repositório.
3. Se o repositório remoto tem mudanças para puxar (pull).
4. Se você está tentando fazer push para o master ao invés da sua branch.

## Mais truques de git:![alt tag](http://i.imgur.com/Ia1S7R8.png)

## PS: Nossa página do projeto (com download e visão geral) estará disponível com github pages e nosso blog está no medium.
## PS2: Protótipos podem ser feitos no site [InVIsion](https://projects.invisionapp.com) ou [MarvelApp](https://marvelapp.com).


## Index

- [scripts/](scripts/)
