---
titulo: Vazamento: o modelo que olha para o futuro sem perceber
data: 2026-10-01
agenda: 2026-10-22
serie: Laudo
rotulo: BASTIDORES
pilar: Preditivo
resumo: Modelo que acerta 85% no teste e desaba em produção costuma ter o mesmo defeito: usou um dado que ainda não existia no dia da decisão.
imagens: post-09.png
linkedin: 
---
Quando alguém me mostra um modelo de churn que "acerta 85%", a primeira pergunta que eu faço não é sobre o algoritmo. É sobre o calendário: o que o modelo sabia, e quando.

A maior parte dos modelos que brilham no teste e desabam em produção tem o mesmo defeito, o vazamento. Para prever um evento, o modelo usa uma informação que só existiria depois dele. No teste parece genial porque, sem perceber, está olhando a resposta.

No Signals, um modelo para prever churn parcial num SaaS de agendamento, essa foi a regra técnica mais importante: todo sinal usado para prever um mês é medido só com o que se sabia no dia da decisão.

Na prática, a regra virou arquitetura. Os sinais ficaram numa tabela por cliente e mês, medidos point-in-time. O que aconteceu em cada mês ficou numa tabela separada de desfechos. O backtest é o cruzamento das duas, e fica muito mais difícil um dado do futuro entrar por engano. De quebra, trocar o evento previsto, de churn parcial para churn ou ativação, virou trocar uma coluna.

A regra também apareceu onde eu não esperava: na data de gerar a lista. O sinal mais forte era o ritmo da primeira semana do mês. Num mês em que a primeira segunda-feira cai no dia seis, uma lista gerada antes do dia oito marcaria a base inteira como risco, só porque a semana ainda não tinha acontecido. A regra virou gerar no dia oito, nunca antes.

Kaufman, Rosset, Perlich e Stitelman descreveram esse problema em 2012, no artigo "Leakage in Data Mining", com casos reais, vários deles de competições de data mining. A conclusão continua valendo: acurácia alta no passado não prova nada se o modelo teve acesso a algo que ainda não existia.

Se você tem um modelo em produção, faça a conferência mais barata que existe. Para cada variável, pergunte em que dia aquele valor estaria disponível. Se a resposta for "depois do evento", o acerto está inflado.

Qual foi o vazamento mais difícil de enxergar que você já encontrou num modelo?

## Referências

- Shachar Kaufman, Saharon Rosset, Claudia Perlich e Ori Stitelman, "Leakage in Data Mining: Formulation, Detection, and Avoidance", *ACM TKDD* (2012)
- Foster Provost e Tom Fawcett, *Data Science for Business* (O'Reilly, 2013), trechos sobre avaliação e vazamento
- Case: [Signals](https://jefersonjs.com.br/cases/signals-downgrade-preditivo/)
