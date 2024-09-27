
# Agricultural Cooperative Coalition Formation Model

## Overview

This project presents a **Coalitional Game-Based Modeling** approach for forming agricultural cooperatives of smallholder farmers. Smallholder farmers face significant challenges in entering the market due to small production sizes, price pressures from large producers, and difficulties in reducing production costs and increasing productivity. By forming cooperatives, these farmers can work together to optimize their revenue and productivity through joint cultivation.

Our approach models each individual farmer as an **agent** in a coalition formation problem and uses social constraints to transform this agent-based model into a coalition formation model.

### Key Features

- **Coalition Formation**: The model organizes smallholder farmers into cooperative groups to increase their market share, productivity, and revenue.
- **Coalitional Game-Based Approach**: We optimize the social welfare of the cooperative by coordinating the efforts of multiple agents (farmers).
- **Heuristic-Based Algorithm**: A custom algorithm generates a disjoint partition of farmers to form coalitions.
- **Payoff Division**: The model ensures that payoffs are divided among agents based on their contribution to the cooperative.
  
The model was evaluated using four metrics: runtime comparison, solution quality, scalability, and individual gain, providing efficient and scalable results even for hundreds of agents.

## Steps of Coalition Formation

1. **Coalition Value Calculation**: 
   - We define a characteristic function as:
     \
     v(C) = v(C^+) - v(C^-)
     \
     where the value v(C) increases as v(C^-) decreases.
   
2. **Coalition Structure Generation**: 
   - A heuristic-based algorithm finds disjoint partitions of the agent set based on similarity.
   
3. **Payoff Division**: 
   - The payoff is divided among the agents according to their contributions to the cooperative.

## Dataset

The project includes a dataset that contains the **landholding values** and **resource requirement values** of agents (farmers). This dataset helps calculate the similarity among agents and finds the optimal coalition structure.

## Evaluation

- **Runtime Efficiency**: For 500 agents, the algorithm takes 95 seconds to find solutions.
- **Solution Quality**: In the worst case, for 16 agents, the solution is 64% of the optimal value.
- **Scalability**: The algorithm handles up to 500 agents efficiently.
- **Revenue Distribution**: The model consistently provides positive revenue for agents based on their contributions to the cooperative.

## Key Insights

- **Coalition Size**: Larger coalitions tend to increase coalition values.
- **Similarity Among Agents**: Greater similarity within a coalition results in higher revenue for its agents.
- **Landholding Size**: Profitability is directly regulated by the size of landholdings.
- **Price Discounts**: Larger coalitions may benefit from price discounts.

## UN Sustainable Development Goals Contribution

This project contributes to several UN SDGs by empowering smallholder farmers through efficient coalition formation:

- **#1 No Poverty**
- **#2 Zero Hunger**
- **#8 Decent Work and Economic Growth**
- **#10 Reduced Inequalities**
- **#16 Peace and Justice**

## Future Work

We plan to extend this project in the following directions:

1. **Graph-Based Modeling**: Explore graph-based approaches for modeling the cooperative with geospatial land data.
2. **Parallelism**: Implement parallel processing to find solutions more quickly.
3. **Stability**: Investigate techniques to ensure the stability of coalitions and improve solution quality over time.

## How to Run

1. Clone the repository:
   \
   git clone https://github.com/HarshVardhan12102002/Coalition_CLuster_Analysis.git

2. Install dependencies (if any):
   \
   pip install -r requirements.txt

3. Run the simulation:
   \
   python coalition_simulation.py

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was inspired by the challenges faced by smallholder farmers and aims to contribute to their empowerment and the improvement of the global informal economy.

---

Thank you for checking out this project! Contributions and feedback are welcome.
