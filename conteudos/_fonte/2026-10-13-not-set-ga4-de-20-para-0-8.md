---
titulo: (not set) no GA4: de 20% para 0,8%
data: 2026-10-01
agenda: 2026-10-13
serie: Laudo
rotulo: LAUDO #02
pilar: Mensuração
resumo: (not set) quase nunca tem uma causa só. É a soma de perdas pequenas, cada uma de um time. Foi assim que 20% do tráfego sem origem caiu para 0,8%.
imagens: post-04.png
linkedin: 
---
Num projeto, 20% do tráfego do GA4 aparecia como (not set): um quinto das sessões sem origem. Depois de uma auditoria da jornada inteira, caiu para 0,8%.

(not set) não é um canal. É o GA4 avisando que não recebeu a informação. Quando um quinto do tráfego cai ali, toda comparação entre canais é feita com quatro quintos do dado, e ninguém sabe se o quinto que falta se parece com o resto.

O que torna o problema difícil é que ele quase nunca tem uma causa só. Costuma ser a soma de perdas pequenas, cada uma num ponto diferente da jornada: uma conta do Google Ads sem vínculo, o gclid que some num redirect, UTM fora do padrão, evento enviado pelo servidor sem a sessão junto. Desde 15/06/2026 existe mais uma: o ad_storage passou a ser o único portão do dado entre GA4 e Google Ads, e um banner de consentimento mal configurado corta esse dado sem avisar.

Por isso não adianta corrigir o primeiro erro encontrado e declarar vitória. A queda para 0,8% veio de auditar etapa por etapa, do primeiro clique ao evento de conversão, e estruturar o tracking em cada uma.

A lição é sobre dono. Cada uma dessas perdas é pequena e pertence a um time diferente: mídia, desenvolvimento, produto, quem cuida do consentimento. Somadas, viram um quinto do dado. Enquanto ninguém olha a soma, ela cresce.

Para medir o tamanho do problema hoje, abra o relatório de aquisição de tráfego, veja o percentual de (not set) nos últimos 30 dias e cruze com dispositivo e página de destino. O padrão que aparecer costuma apontar a primeira causa.

Quanto do seu tráfego está em (not set) hoje?

## Referências

- [Google, [GA4] What the value (not set) means in your reports](https://support.google.com/analytics/answer/1009667?hl=en)
- [Digital Applied, GA4's June 15 consent change](https://www.digitalapplied.com/blog/ga4-consent-split-june-15-2026-ad-storage-tracking-audit)
