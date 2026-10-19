---
titulo: Acesso não é contexto
data: 2026-10-01
agenda: 2026-11-05
serie: IA na prática
rotulo: IA NA PRÁTICA · 02
pilar: Contexto
resumo: A IA disse não conhecer nenhuma marca parceira da Marina Mogilko, embora quase todo acordo tivesse passado por ela. Ter acesso, buscar, ler e interpretar são etapas diferentes.
imagens: ia-02.png
linkedin: 
---
A Marina Mogilko pediu ao Claude uma estratégia de crescimento para as parcerias com marcas da empresa dela. A resposta foi que ele não sabia o nome de nenhuma marca com quem ela já tinha trabalhado, mesmo com quase todo acordo tendo passado por ele de algum jeito, na revisão da newsletter de um patrocinador ou no gancho de uma campanha.

Ela reescreveu o pedido com mais detalhe e recebeu categorias genéricas: SaaS B2B, fintech, ferramentas de RH. O problema não era o prompt.

A explicação que ela dá na newsletter é a parte mais útil. Ter acesso a uma informação, buscar, ler e interpretar são etapas diferentes, e qualquer uma pode falhar sem aviso. O mais provável é que o modelo tenha buscado por "patrocínio" ou "marca", palavras que, num projeto organizado em torno de conteúdo, não ficam onde os acordos realmente estão. Quando a IA diz que não encontrou, isso descreve a busca, não prova que o dado não existe.

O segundo ponto é frescor. O que ela tinha passado ao modelo eram regras e materiais enviados uma vez e nunca atualizados, enquanto o CRM muda no momento em que alguém do time move um negócio de etapa. Para perguntas sobre o estado atual do negócio, ela passou a usar a IA que fica onde o dado está, e manteve o Claude para pensar e rascunhar. A edição foi patrocinada pela HubSpot, então a conclusão sobre ferramenta tem dono. O diagnóstico, não.

Em analytics, esse erro tem versões conhecidas. O modelo consulta um export de três meses atrás e responde com confiança. A métrica "receita" existe em quatro tabelas e ele escolhe uma. O dado que mudou ontem ainda não chegou à camada que ele lê.

Vi isso de perto ao montar um data warehouse com LLM para consultas em linguagem natural. A qualidade da resposta dependia menos do modelo e mais de o dado estar num lugar só, atualizado em D-1, com a mesma definição usada no painel.

Antes de culpar o prompt, vale fazer três perguntas sobre a resposta errada: o modelo tinha acesso ao dado, encontrou o dado, e o dado estava atualizado?

Na última vez que uma IA errou um número no seu time, qual dessas três etapas falhou?

## Referências

- [Marina Mogilko, "Context", Future Proof (22/09/2026)](https://siliconvalleygirl.beehiiv.com/p/context-b9d8), edição patrocinada pela HubSpot
