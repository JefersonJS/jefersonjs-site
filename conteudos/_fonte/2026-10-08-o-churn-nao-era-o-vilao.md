---
titulo: O churn não era o vilão
data: 2026-10-01
agenda: 2026-10-08
serie: Laudo
rotulo: BASTIDORES
pilar: Preditivo
resumo: A base encolhia e todos chamavam de churn. Separar quem cancela de quem só reduz o uso mostrou que o problema era seis vezes maior e estava em outro lugar.
imagens: post-03.png
linkedin: 
---
A liderança via a base de clientes mais valiosos encolhendo todo mês e tratava isso como churn. A resposta padrão era cupom de reativação, e o número não mexia.

Antes de construir qualquer modelo, fui conferir a premissa. O indicador misturava dois eventos diferentes: o cliente que zera o uso e o cliente que continua ativo, mas passa a usar bem menos.

Separados, os dois contavam histórias opostas. O churn de verdade, o cliente que zera, rodava perto de 4% ao mês, estável, com pico sazonal previsível. O churn parcial rodava perto de 22% ao mês, quase seis vezes mais, parado num patamar alto. Era ele que explicava a queda.

Essa separação muda a estratégia. Quem cancelou já foi, e trazer de volta é caro. Quem reduziu o uso ainda está dentro de casa, só desacelerou, e agir antes custa pouco. Em número de diretoria, o churn parcial levava entre 4% e 5% do volume total da empresa, todo mês. Ninguém tinha esse número.

O cupom também ficou explicado. Quem tinha usado cupom no mês anterior tinha mais churn parcial e mais churn depois. O cupom trazia de volta justamente quem só voltava por cupom.

O Peter Fader defende em *Customer Centricity* que nem todo cliente vale o mesmo e que a estratégia começa por saber quais sustentam o negócio. Aqui, os clientes que sustentavam o negócio estavam indo embora aos poucos, sem nunca aparecer como cancelamento.

O modelo veio depois e foi simples: um score de 0 a 10 para apontar quem tende a reduzir o uso, uma lista trabalhada com comunicação de valor, sem cupom, e um grupo de controle para medir o efeito. O que destravou o projeto não foi o modelo. Foi separar os dois eventos antes de construir qualquer coisa.

Se você acompanha churn só como cancelamento, vale abrir o mesmo indicador em dois: quem saiu e quem continuou, mas caiu de nível. A segunda curva costuma contar outra história.

Na sua base, você mede a queda de uso ou só o cancelamento?

## Referências

- Peter Fader, *Customer Centricity* (Wharton Digital Press, 2012)
- Case: [Signals, previsão de churn parcial](https://jefersonjs.com.br/cases/signals-downgrade-preditivo/)
