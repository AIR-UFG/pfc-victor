# TCC - Victor F. C. Ribeiro
A ideia inicial do projeto é uma pesquisa na área de análise de dados e estatísticas esportivas, entendendo melhor a ideia de "arquétipos" em esportes e como eles se relacionam para poder prever resultados e entender jogos.

> Título: *

## Revisão bibliográfica
Artigos que possuírem pdf estarão na pasta [artigos](./artigos) e serão indicados pelo emoji  ':bookmark_tabs:'.

* String de busca atual: _(archetypoid OR archetype) AND (analysis OR data OR perfomance OR statistic) AND (sports OR team OR player)_

1. Archetypoid analysis for sports analytics (2017) [:bookmark_tabs:](./artigos/Archetypoid-Analysis--Vinue&Epifanio.pdf)
   - Link para o artigo: [https://www.researchgate.net/publication/317336036_Archetypoid_analysis_for_sports_analytics](https://www.researchgate.net/publication/317336036_Archetypoid_analysis_for_sports_analytics)
   - **TODO**: artigo possui referências que parecem ser boas, quanto a origem de conceitos e abordagens iniciais.
   - O artigo comenta sobre a diferença entre '_archetypes_' e '_archetypoids_'. Ambos os conceitos partem do princípio que para análises e melhor identificar pontos extremos (jogadores muito bons ou ruins) do que pontos médios, enquanto '_archetype_' refere a um jogador ideal (uma combinação convexa dos jogadores analisados) muitas vezes não existe, deixando o conceito pouco tangível. Visando melhorar essa ideia foi criado o conceito de '_archetypoid_' em que será um jogador real para que os demais sejam comparados a ele, deixando análises e o entendimento do jogo mais fácil. O propósito deste artigo é utilizar a análise de '_archetypoids_' (ADA) para encontrar jogadores e times que seriam tais pontos. O artigo faz três análises: caso multivariado, em que os dados de esportes são coletados como features; segundo caso em teremos dados funcionais (o dado é uma função continua); e o terceiro caso em que não temos features apenas dissimilaridades entre observações. Ao fim, o artigo propõe a encontrar uma metodoligia que identifique os '_archetypoids_' com os dados de qualquer esporte.
  
2. Looking for archetypes: Applying game data mining to hearthstone decks (2022) [:bookmark_tabs:](./artigos/Applying-game-data-mining-to-hearthstone-decks.pdf)
   - Link para o artigo: [https://www.sciencedirect.com/science/article/abs/pii/S1875952122000222](https://www.sciencedirect.com/science/article/abs/pii/S1875952122000222)
   - O artigo se propõe a usar a análise de arquétipos para identificar bons decks já existentes e com isso ver como as classes de carta de relacionam a fim de montar o deck ideal. Aqui serão utilizadas técnicas de clusterização (k-Means e agrupamento hierárquico) para identificar os grupos em que determinadas cartas se encaixam, como propósito final o entedimento melhor do funcionamento do jogo e o artigo também diz que a análise ajuda no desenvolvimento de agentes inteligentes para jogos de cartas e em tomadas de decisão em tempo real.
  
3. Information theory and player archetype choice in Hearthstone (2020)
   - Link para o artigo: [https://www.sciencedirect.com/science/article/pii/S0020025521001043](https://www.sciencedirect.com/science/article/pii/S0020025521001043)
   - _Leitura em andamento_
  
4. Sports analytics for balanced team-building decisions (2021)
   - Link para o artigo: [https://www.tandfonline.com/doi/full/10.1080/01605682.2022.2118634](https://www.tandfonline.com/doi/full/10.1080/01605682.2022.2118634)
   - _Leitura em andamento_

5. A Survey on Applications of Modern Deep Learning Techniques in Team Sports Analytics (2021)
   - Link para o artigo: [https://www.researchgate.net/publication/350910169_A_Survey_on_Applications_of_Modern_Deep_Learning_Techniques_in_Team_Sports_Analytics](https://www.researchgate.net/publication/350910169_A_Survey_on_Applications_of_Modern_Deep_Learning_Techniques_in_Team_Sports_Analytics)
   - _Leitura pendente_

6. [BLOG] A Survey of Sports Analytics (2021)
   - Link para o artigo: [https://gabs-rol43.medium.com/a-survey-of-sports-analytics-2254f1d9a933](https://gabs-rol43.medium.com/a-survey-of-sports-analytics-2254f1d9a933)
   - Este survey diz sobre a importância do 'sports analytics' para grandes times atualmente e mostra a ideia geral sobre como conseguem 'fazer _analytics_', classificando em trẽs pontos principais: aquisição de dados, enriquecimento de dados e análise. O primeiro ponto se refere a como os times conseguem os dados, as principais estratégias são: coletar o movimento dos atletas (por sensores ou algoritmos que identificam via video), identificar eventos (algoritmos que definem a partida como sequência de eventos, por exemplo gol, falta, tiro de meta no futebol) ou dados descritivos (estatísticas individuais/coletivas).Já o enriquecimento de dados é apresentado como estratégias que visam dar um siginificado a mais para os dados coletados e assim melhorar a performance do time, técnicas para visualização de dados, análises espaço temporais, zonas de conflito (baseando em dados de movimento identificar zonas congestionadas e espaços livres) e _expected values_  (uma métrica que tenta definir o valor esperado de uma determinada ação de um atleta em determinado tempo). Por fim, o terceiro ponto é a interpretação dos dados, identificar falhas em regras, entender a evolução do jogo e transmitir para o time a ideia e importância dos dados.



