---
titulo: Nunca conte à IA o que você acha que tem
data: 2026-10-01
agenda: 2026-11-12
serie: IA na prática
rotulo: IA NA PRÁTICA · 03
pilar: Viés
resumo: Um médico de Stanford explica por que a IA concorda com a sua hipótese, esquece detalhes e se perde em datas. Os mesmos mecanismos aparecem em qualquer análise de dados feita com IA.
imagens: ia-03.png
linkedin: 
---
O canal Silicon Valley Girl publicou uma conversa com o Jonathan Chen, médico e pesquisador de Stanford que estuda IA na educação médica. O título resume o conselho principal: nunca conte à IA o que você acha que tem.

O motivo é o comportamento do modelo. A IA tende a concordar com quem pergunta. Se o paciente chega dizendo "acho que é X", ela puxa o raciocínio para X, e quem já estava no caminho errado vai mais longe nele. A recomendação do Chen é descrever só os fatos objetivos: o que sente, desde quando, o que mudou.

Dois outros pontos da conversa me chamaram mais atenção. O primeiro é que o erro mais comum que ele vê não é a IA inventar coisas, é esquecer. Ao resumir um prontuário de mil páginas, ela deixa de fora o nódulo pequeno. O segundo é que, com anos de exames num bloco só, o modelo se perde em datas e números e passa a comentar um resultado de sete anos atrás como se fosse atual.

Ele também cita um ensaio de Stanford com 70 médicos. Os que viram a análise da IA antes de formar a própria opinião acertaram 85% dos casos, contra 82% de quem consultou a IA depois e 75% de quem usou só os recursos tradicionais.

O Chen não fala de analytics, mas os mesmos mecanismos aparecem em qualquer análise feita com um LLM. A versão de negócio do "acho que é X" é a pergunta "por que o Meta fez o CAC subir?". Ela já traz a resposta, e o modelo vai procurar evidência contra o Meta e parar quando encontrar. O esquecimento aparece quando pedimos o resumo de um relatório longo. A confusão com datas aparece quando colamos uma série de dois anos e pedimos a tendência.

As sugestões dele funcionam igual. Faça a pergunta com fatos, não com a hipótese: "o que mudou no CAC nas últimas quatro semanas, por canal?". Peça o contrário do que você espera, como "me convença de que não foi o Meta". E, para decisão importante, confira a resposta com um segundo modelo antes de levar o número para a reunião.

Qual foi a última pergunta que você fez a uma IA já sabendo a resposta que queria?

## Referências

- [Silicon Valley Girl em Português, "Médico de Stanford alerta: nunca conte à IA o que você acha que tem"](https://www.youtube.com/watch?v=1YeU5H4V5_M), com Jonathan Chen (versão dublada do canal original)
- [Ensaio randomizado com 70 clínicos sobre a ordem de uso da IA no diagnóstico (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12155023/)
