---
titulo: LLM sem camada semântica inventa métrica
data: 2026-10-01
agenda: 2026-10-15
serie: Laudo
rotulo: BASTIDORES
pilar: Dados e IA
resumo: Um warehouse unificado com LLM devolveu mais de 2 dias por semana a dois times. O ganho veio da definição das métricas, não do modelo.
imagens: post-06.png
linkedin: 
---
Os times de Mídia Paga e de Conteúdo/SEO gastavam boa parte da semana juntando dado de plataforma com indicador de negócio. Construí um data warehouse que reunia os dados das plataformas e os ligava aos indicadores da empresa, com painel atualizado em D-1 e um LLM para consultas em linguagem natural. Os dois times ganharam mais de dois dias de trabalho por semana.

É tentador dar o crédito ao LLM. Mas ele foi a última camada, não a principal.

Pense na pergunta mais comum de um time de mídia: "qual foi o CAC de ontem?". Para responder, alguém precisa decidir qual custo usar, qual janela de conversão e o que conta como cliente. Se essas decisões não estiverem escritas em algum lugar, o modelo decide sozinho. Responde com confiança, e pode responder diferente a cada vez.

Esse risco tem nome há décadas. O Ralph Kimball chamava de dimensões e fatos conformados: uma definição de cliente, de receita e de canal, usada igual em todos os relatórios. Hoje a mesma ideia aparece como camada semântica, e as ferramentas de text-to-SQL chegaram a ela pelo caminho difícil, descobrindo que o modelo precisa consultar métricas definidas, não tabelas cruas.

A lição que eu levo é que IA sobre dados não diminui a necessidade de modelagem. Aumenta. Uma métrica mal definida num painel gera um gráfico errado que alguém acaba percebendo. Num LLM, gera uma resposta errada, bem escrita, para cada pessoa que pergunta.

Se o seu time quer colocar uma IA para responder sobre os números, comece por um teste simples: faça a mesma pergunta para a IA e para o painel oficial. Se as respostas não baterem, o problema está na definição, não no modelo.

Você já fez esse teste? As respostas bateram?

## Referências

- Ralph Kimball e Margy Ross, *The Data Warehouse Toolkit* (Wiley, 3ª ed., 2013), dimensões e fatos conformados
- [dbt, Semantic layer vs text-to-SQL (2026)](https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026)
- [Cube, Semantic layer for AI agents (2026)](https://cube.dev/articles/semantic-layer-for-ai-agents-2026)
