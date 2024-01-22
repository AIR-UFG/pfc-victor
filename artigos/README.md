## Abstracts
1) _Towards a Time-Aware Hidden Markov Model for the Truco Game_: Similar to Poker, the game of Truco has challenges for Artificial intelligence. Considering a large number of game states, a scenario
characterized by partial visibility, stochastic behavior, and score susceptible to bluff; this game offers a good set of rules to test and improve AI techniques. In this article, we describe the
creation of a Hidden Markov Model (HMM) agent using temporal control. The model has an embedded vector that adjusts its probabilities for further game actions, consequently, improving the model
playing performance. The evaluation is given with over 210,000 matches, serving as empirical proof of the idea.

2) _A Markovian model for the Game of Truco_: In recent years, the advancement of Artificial Intelligence (AI) for games is notorious. However, despite achieving the expected results, many AI
techniques require considerable computational power, which is not viable when games are running in more basic computing platforms. Observing the need ofcreating and using light-weight techniques,
this work uses a Markovian structure for the development of an agent to play the card game of Truco. The proposed modeling represents the natural order of the card strengths in the game. It is
also separated into modules according to the game rules and optimized according to the game state-space. The model also learns at each game action, reinforcing decisions, and improving future responses.

3) _Mathematical Modeling and Development of an Agent based on Markovian Models_: In the last years, it is possible to see the advance of Artificial Intelligence applied to the
most diverse games, whether they are deterministic or stochastic. Many techniques, des pite achieving the expected result, require considerable computational power and are not
viable on more basic platforms (e.g., low-cost smartphones). Thus, there is a need to create light weight techniques. This work uses Markov Chains in the development of an agent
for a card game. The modeling was performed to represent the natural order of the forces and separates it into three modules according to the game’s modalities, being: Truco,
Envido and Flor. Decision making is based on games played previously, reinforcing the decisions made and improving them. To evaluate the model, several rounds of tests were made, varying
the opponent and the databases. This process resulted in learning matrices for each game mode. Thus, they were evaluated considering the main characteristics of themodel and also of the opponents.

4) _Investigating Case Learning Techniques for Agents to Play the Card Game of Truco_: Truco is a popular game in many regions of South America; however, unlike worldwide games, Truco still
requires a competitive Artificial Intelligence. Due to the limited availability of Truco data and the stochastic and imperfect information characteristics of the game, creating competitive
models for a card game like Truco is a challenging task. To approach this problem, this work investigates the generation of concrete Truco problem-solving experiences through alternative techniques of
automatic case generation and active learning, aiming to learn with the retention of cases in case bases. From this, these case bases guide the playing actions of the implemented Truco bots
permitting to assess the capabilities of each bot, all implemented with Case-Based Reasoning (CBR) techniques.

5) _Solving Coup as an MDP/POMDP_ :We modeled the card game Coup as a Markov Decision Process and attempted to solve it using various methods learned in CS238. Due to our large state space, we focused on online methods. Since Coup is a multi-agent game we generated optimal policies against players with specific strategies. We first modeled the game as an MDP where we knew everything about the game state and
developed policies against a player doing random actions. We used forward search, sparse sampling, and monte carlo tree search. We then modeled the game as a POMDP with state uncertainty where we did not
know our opponents cards. We implemented Monte Carlo Tree Search, sparse sampling and forward search with both incomplete and complete information. Finally, to try and beat our Monte Carlo Tree Search
player, we implemented Forward Search with Discrete State Filtering for updating our belief.
