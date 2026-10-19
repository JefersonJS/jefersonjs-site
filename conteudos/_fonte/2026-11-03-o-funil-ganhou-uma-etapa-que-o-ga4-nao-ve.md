---
titulo: O funil ganhou uma etapa que o GA4 não vê
data: 2026-10-01
agenda: 2026-11-03
serie: IA na prática
rotulo: IA NA PRÁTICA · 01
pilar: GEO
resumo: O podcast da Marina Mogilko tinha 1,56 milhão de inscritos e não aparecia no ChatGPT. O que ela mediu para mudar isso mostra uma etapa do funil que o GA4 não enxerga.
imagens: ia-01.png
linkedin: 
---
A Marina Mogilko tem 1,56 milhão de inscritos no YouTube com o podcast Silicon Valley Girl. Quando perguntou ao ChatGPT quais podcasts de IA e startups seguir, o dela não apareceu.

Antes de mexer em qualquer coisa, ela mediu. Escreveu perguntas sobre a categoria sem o nome da marca e acompanhou as respostas numa ferramenta de monitoramento. O podcast não aparecia em nenhuma das 1.008 fontes que os modelos usavam para responder e só surgia em 5 de 49 perguntas, sempre puxado pelo nome de algum convidado. Das 1.008 fontes, 459 eram listas do tipo "os melhores".

O diagnóstico explicou o resto. A IA cita quem é citado por terceiros, e lê texto, não vídeo. As correções foram de base: arrumar o cadastro no Wikidata, que classificava o podcast como canal do YouTube; criar uma página por episódio com a transcrição no HTML; usar nos títulos as palavras que a própria IA usa para buscar; e procurar os sites que a IA mais cita.

Em dez semanas, a visibilidade foi de 2,2% para 7,8%. Uma segunda métrica saiu do zero para 2,6%: quantas vezes o modelo abriu o site dela para montar a resposta.

O que mais me interessa nesse caso é a mensuração. Nenhum desses números aparece no GA4. A pergunta, a resposta e a marca citada sem clique acontecem fora do site. E o clique que sobra é menor: o Pew Research mostrou que quem vê o resumo de IA do Google clica num link em 8% das visitas, contra 15% de quem não vê.

Na prática, o funil de busca ganhou uma etapa antes do clique, com perguntas próprias: a marca foi citada, em que posição, como foi descrita, e o modelo usou o site como fonte. Quem mede só a sessão está medindo o que sobra dessa etapa.

Tem uma regra da Marina que vale para qualquer monitoramento desse tipo: as perguntas monitoradas não podem ter o nome da marca. Pergunta com o nome só confirma quem já conhecia você.

Para começar, escreva vinte perguntas que um cliente faria sobre a sua categoria, sem o nome da sua empresa, e rode em dois ou três assistentes. Anote quem aparece e quais sites são citados como fonte.

Se você fizer esse teste hoje, quem você acha que aparece no lugar da sua marca?

## Referências

- [Marina Mogilko, "I have 1.56M subscribers. ChatGPT couldn't find me", Future Proof (02/08/2026)](https://siliconvalleygirl.beehiiv.com/p/i-have-1-56m-subscribers-chatgpt-couldn-t-find-me)
- [Pew Research Center, Google users are less likely to click on links when an AI summary appears (22/07/2025)](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)
