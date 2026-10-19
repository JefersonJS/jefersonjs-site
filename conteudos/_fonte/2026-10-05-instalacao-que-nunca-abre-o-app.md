---
titulo: Instalação que nunca abre o app: o sinal de fraude que o painel não mostra
data: 2026-10-01
agenda: 2026-10-05
serie: Laudo
rotulo: LAUDO #01
pilar: Fraude
resumo: Um parceiro pago por compra entregava volume e quase nenhuma compra no backend. Três sinais no dado bruto da AppsFlyer bastaram para provar a fraude.
imagens: post-01.png
linkedin: 
---
Um parceiro de programática entregava tudo o que prometia no painel: volume de instalação e as compras que cobrava. Ele era pago por CPA, em cima da primeira compra dentro do app, então o custo parecia sob controle.

O problema apareceu numa revisão de rotina, numa métrica que não está em nenhum relatório padrão: a taxa de instalação para primeira abertura. Nos outros parceiros, 92% das instalações viravam abertura, quase na hora. Nesse, 38%.

Instalação que nunca abre o app não é usuário. Na maior parte das vezes é alguém disputando o crédito de uma instalação, ou um aparelho que nunca teve gente do outro lado.

Uma taxa estranha, sozinha, não prova fraude. Então fui atrás de mais dois sinais no dado bruto da AppsFlyer. O primeiro foi IP e device ID: muitas instalações saindo dos mesmos blocos de IP, e o mesmo device ID aparecendo em "usuários" diferentes. O segundo foi receita: cruzei as instalações suspeitas com o backend, e quase nenhuma tinha gerado compra, mesmo sendo cobradas como compra.

Com três sinais independentes apontando para o mesmo parceiro, o caso fechou. Cerca de 35% do volume dele era fraude. O parceiro foi bloqueado, os valores futuros foram renegociados e a empresa conseguiu retroativo. Entre o que voltou e a verba realocada, foram mais de R$ 100 mil, sem contratar o Protect360, cuja cotação passava de US$ 5 mil por mês.

O que fica desse caso é o que o Ron Kohavi chama de Lei de Twyman: quando um número parece interessante demais, a primeira hipótese deve ser erro. Um parceiro com volume alto, pago por compra, e quase nenhuma compra no backend é exatamente esse número.

O método tem limite. Ele pega o padrão mais comum, como click flooding e instalação vinda de device farm ou emulador. Fraude com aparelho real por trás passa, e aí a ferramenta dedicada faz falta.

Para testar na sua conta, o primeiro passo cabe numa consulta: instalação para primeira abertura, por parceiro, comparada com a média dos outros. Quem estiver muito abaixo merece o cruzamento com IP, device ID e receita.

Você já tirou essa taxa por parceiro? Qual foi a maior diferença que apareceu?

## Referências

- Kohavi, Tang e Xu, *Trustworthy Online Controlled Experiments* (Cambridge, 2020), capítulo sobre a Lei de Twyman
- [AppsFlyer, The State of Fraud for Marketers 2026](https://www.appsflyer.com/pt/resources/reports/mobile-ad-fraud-state)
- [AppsFlyer, Mobile ad fraud: the marketer's field guide](https://www.appsflyer.com/blog/measurement-analytics/mobile-ad-fraud-for-marketers/) (sequestro de atribuição, SDK spoofing)
- Case: [Antifraude mobile com AppsFlyer](https://jefersonjs.com.br/cases/antifraude-programatica-mobile/)
