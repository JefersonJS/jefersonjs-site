---
titulo: Atribuição por pessoa, não por clique
data: 2026-10-01
agenda: 2026-10-07
serie: Laudo
rotulo: FRAMEWORK
pilar: Mensuração
resumo: O último clique dizia que o CRM valia 2% das ativações. Trocar o clique pela pessoa como unidade de análise mostrou 12%, e mudou a conversa com a liderança.
imagens: post-02.png
linkedin: 
---
Quase todo relatório de atribuição conta cliques e sessões. Só que quem se cadastra, compra ou ativa é uma pessoa, e uma pessoa costuma passar por vários canais antes de decidir.

Essa diferença ficou clara num projeto de CRM de uma plataforma self-service. O relatório de último clique do Google Analytics dizia que o CRM respondia por 2% das ativações, abaixo da meta e parado havia meses. A pergunta da head de CRM era direta: o canal piorou ou a conta está medindo errado?

Para responder, troquei a unidade de análise, do clique para a pessoa. Esse foi o trabalho mais pesado do projeto, mais do que o modelo. Cada toque de e-mail, WhatsApp, push e banner precisava ser ligado a quem ativou. O e-mail virou a chave principal, o user_id resolveu o que acontecia dentro do app, e o push e o banner, que só tinham o dispositivo, ganharam uma ponte determinística até o usuário.

Com a pessoa no centro, o mesmo dado passou a responder perguntas diferentes. O último clique virou o piso, igual ao relatório antigo. O primeiro clique mostrou quem abria a jornada. A influência, qualquer toque numa janela de 7 dias, mostrou o teto.

Na leitura de influência, já sem o e-mail transacional que sai para todo mundo que se cadastra, o CRM participava de perto de 12% das ativações. Seis vezes o número antigo. E 65% dessas ativações tinham dois ou mais toques, o que explica por que o último clique enxergava tão pouco: o e-mail abria a jornada e o WhatsApp fechava.

Duas cautelas fizeram esse número ser aceito. A primeira foi chamar de participação, não de causa, porque estar presente antes da ativação não prova que o CRM a gerou. A segunda foi avisar que as fatias por canal não somam o total, já que a mesma pessoa pode ser tocada por mais de um canal.

O George Box escreveu que todo modelo está errado, mas alguns são úteis. Nenhuma das quatro leituras é a certa. Lado a lado, elas mostram o que nenhuma mostra sozinha.

Se a sua atribuição ainda é por sessão, um bom começo é contar quantas conversões tiveram mais de um toque antes. Se for a maioria, o último clique está escondendo parte do valor dos canais que trabalham no meio da jornada.

Na sua empresa, qual canal você desconfia que o último clique está subestimando?

## Referências

- George E. P. Box, "Science and Statistics", *Journal of the American Statistical Association* (1976), e "Robustness in the Strategy of Scientific Model Building" (1979), onde aparece o "mas alguns são úteis"
- [Acxiom, First-party data identity foundation](https://www.acxiom.com/blog/first-party-data-identity-foundation/): pesquisa EMARKETER/Acxiom 2026, mais de 90% já usam identificadores para reconhecer clientes entre canais
- Case: [Atribuição multitoque de CRM](https://jefersonjs.com.br/cases/atribuicao-multitoque-crm/)
