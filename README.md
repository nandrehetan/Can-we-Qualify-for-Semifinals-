
# Can We Still Qualify For Semifinals?

The Cricket World Cup is a highly anticipated event, captivating fans worldwide. During the tournament, a common curiosity arises: Can a specific team still qualify for the semifinals, i.e., the top 4? This problem aims to address such queries.

A total of 10 teams are participating in the Cricket World Cup: India, Australia, England, New Zealand, Pakistan, South Africa, Sri Lanka, Afghanistan, Bangladesh, and the Netherlands. We number the teams 1 to 10, with India being number 1. 😉

The tournament follows a round-robin format, where each team plays against every other team exactly once, spread across a series of phases/rounds. In each round, every team participates in one game. The match selection process ensures that each team faces every other team exactly once, resulting in a total of 45 games.

The rounds of the tournament can be systematically structured using a mathematical approach, described below.

The method for generating the fixtures would be a round-robin method. In phase 1, the teams are initially arranged in ascending order (e.g., [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]). Matches are then formed by pairing the first team with the last team, the second team with the second-to-last team, and so on, until the middle teams meet. In other words, in this phase, the matches would be team 1 vs team 10, 2 vs 9, 3 vs 8, 4 vs 7, 5 vs 6

The subsequent phases involve a circular rotation of the team list, keeping the position of the first team fixed at the start. In each phase, teams are matched with their counterparts in a mirrored fashion. For example, in the second phase, the teams are arranged as [1, 10, 2, 3, 4, 5, 6, 7, 8, 9], where the first team faces the second-to-last team, the second team faces the second-to-second-last team, and so forth. In the third phase, the teams would be arranged as [1, 9, 10, 2, 3, 4, 5, 6, 7, 8].

## How to run ?

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Can-we-Qualify-for-Semifinals.git
cd Can-we-Qualify-for-Semifinals

```

2. Run the script and provide the binary string of match results as input:
```bash
streamlit run icpc.py

```

## Flowchart
![flowchart](https://github.com/nandrehetan/Can-we-Qualify-for-Semifinals-/assets/97376783/d84387a6-87c6-40df-a640-a9a7389b2a1e)



