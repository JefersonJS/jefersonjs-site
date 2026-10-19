---
titulo: Propensão não é uplift
data: 2026-10-01
agenda: 2026-10-26
serie: Laudo
rotulo: LAUDO #04
pilar: Preditivo
resumo: Score de churn diz quem vai sair. A campanha de retenção precisa saber quem fica se a empresa agir. São perguntas diferentes, e confundir as duas custa dinheiro.
imagens: post-10.png
linkedin: 
---
Um modelo de churn responde bem a uma pergunta: quem tem mais chance de sair. O problema é que a campanha de retenção precisa da resposta para outra: quem fica se a gente agir.

As duas parecem iguais e não são. A literatura de uplift modeling divide os clientes em quatro grupos: os que ficam de qualquer jeito, os que saem de qualquer jeito, os persuadíveis, que só ficam se você agir, e os "cães adormecidos", que saem justamente porque você mexeu com eles.

Um score de propensão coloca no topo da lista quem tem mais risco, e ali os quatro grupos aparecem misturados. Num white paper da Stochastic Solutions, Nicholas Radcliffe relata que a ação de retenção típica é contraproducente para algo como 30% dos clientes abordados. A empresa paga para empurrar cliente para fora.

Vi uma versão disso num SaaS de agendamento. A resposta padrão para a queda da base era cupom, e os dados mostraram que quem tinha usado cupom no mês anterior saía mais, não menos. O cupom trazia de volta quem só voltava por cupom.

O Judea Pearl explica a diferença com a escada da causalidade. Propensão fica no primeiro degrau, a associação: quem se parece com quem saiu. Saber quem responde a uma ação exige o segundo degrau, a intervenção, e intervenção se mede com experimento.

Por isso, no Signals, o score servia para escolher a lista, mas o efeito era medido contra um grupo de controle sorteado, que não recebia nada. A métrica, definida antes, era quantos clientes continuavam no nível core no fim do mês. Sem esse grupo, qualquer melhora podia ser só o cliente que ia ficar de qualquer jeito.

Prever risco é a parte fácil. O que justifica o orçamento de retenção é provar que a ação mudou o comportamento.

Se a sua retenção já usa um score, o próximo passo é separar uma fatia da lista, algo entre 10% e 20%, como grupo de controle na próxima campanha. É o jeito mais barato de saber se a ação está ajudando ou atrapalhando.

As campanhas de retenção da sua empresa têm grupo de controle?

## Referências

- [Nicholas Radcliffe, Uplift Modelling for Retention (Stochastic Solutions)](https://www.stochasticsolutions.com/pdf/uplift-modelling-for-retention.pdf)
- Judea Pearl e Dana Mackenzie, *The Book of Why* (Basic Books, 2018), a escada da causalidade
- Case: [Signals](https://jefersonjs.com.br/cases/signals-downgrade-preditivo/)
