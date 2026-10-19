---
titulo: 57,5% do tráfego já não é humano: o que isso faz com o seu GA4
data: 2026-10-01
agenda: 2026-10-14
serie: Laudo
rotulo: AGENTES
pilar: Fraude
resumo: O tráfego automatizado passou o humano na rede da Cloudflare. Para o analytics, isso quebra a premissa de que existe uma pessoa do outro lado do painel.
imagens: post-05-1.png, post-05-2.png, post-05-3.png, post-05-4.png, post-05-5.png, post-05-6.png, post-05-7.png
alts: Capa: 57,5% do tráfego já não é humano, o que isso faz com o seu GA4 | Sinal 1: log do servidor, agente que não roda JavaScript só aparece aqui | Sinal 2: clique pago sem sessão no GA4 | Sinal 3: formulário preenchido em 3 segundos | Sinal 4: funil por hora com pico de madrugada e conversão zero | Sinal 5: só conta a conversão que o backend confirma | O painel foi feito para humanos. O tráfego, não mais.
linkedin: 
---
Em junho, o CEO da Cloudflare, Matthew Prince, disse que o tráfego automatizado já tinha passado o humano: 57,5% das requisições de páginas HTML na rede deles. Ele esperava isso só para 2027.

Parte desse tráfego é agente de IA navegando em nome de alguém, lendo página, comparando preço, preenchendo formulário. E isso mexe numa premissa que quase todo painel de marketing carrega sem perceber: a de que existe uma pessoa do outro lado.

O agente quebra o analytics de dois jeitos opostos. O que não roda JavaScript some do GA4: você não vê a visita, mas paga por ela no servidor e, às vezes, no clique. O que roda JavaScript entra como usuário, com sessão de dois segundos, rejeição alta e lead que nunca atende o telefone.

No primeiro caso, o número fica menor do que a realidade. No segundo, fica pior. Em nenhum dos dois a taxa de rejeição, o tempo na página ou a conversão continuam dizendo o que diziam antes.

Não dá para esperar que a ferramenta resolva isso sozinha, mas dá para saber onde olhar. Estes são os cinco lugares onde eu procuro agente e bot hoje:

1. Log do servidor: o agente que não roda JavaScript só aparece aqui.
2. Clique pago sem sessão no GA4, comparado hora a hora.
3. Formulário preenchido em poucos segundos, por lead que nunca atende.
4. Funil por hora: pico de madrugada com conversão zero.
5. Conversão confirmada no backend: só conta o que o backend confirma.

O ponto de partida mais simples é o segundo. Compare cliques pagos com sessões no GA4, hora a hora. Se a diferença crescer em horários que não fazem sentido para o seu público, existe tráfego que o painel não está tratando como deveria.

No seu painel, qual métrica você já desconfia que está sendo distorcida por bot?

## Referências

- [Tom's Hardware, Bots have now passed human traffic online](https://www.tomshardware.com/tech-industry/artificial-intelligence/bots-have-now-passed-human-traffic-online-cloudflare-boss-laments-says-agentic-traffic-wasnt-expected-to-eclipse-real-people-until-next-year) (Matthew Prince, 03/06/2026)
- [Snowplow, How AI agents and bots are breaking your web analytics](https://snowplow.io/events/how-ai-agents-and-bots-are-breaking-your-web-analytics)
