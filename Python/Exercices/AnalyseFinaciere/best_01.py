import pandas as pd
import numpy as np
from itertools import combinations

# Charger les données
data = pd.read_csv('data.csv', na_values=['NA', 'NULL'])
prices = np.array(data["price"])
profits = np.array(data["profit"])

# 1. Méthode Brute Force optimisée avec budget
def brute_force_max_profit(prices, profits, budget):
    max_profit = 0
    best_combination = []
    n = len(prices)

    # Tester toutes les combinaisons de parts
    for r in range(1, n + 1):
        for combo in combinations(range(n), r):
            total_price = sum(prices[list(combo)])  # Calculer le prix total de la combinaison
            if total_price <= budget:  # Ne considérer que si c'est dans le budget
                total_profit = sum(profits[list(combo)])
                if total_profit > max_profit:
                    max_profit = total_profit
                    best_combination = combo

    return max_profit, [data["name"].iloc[i] for i in best_combination]

# Définir le budget
budget = 300  # Par exemple, un budget de 300 unités

# Résultat de la méthode brute force avec budget
max_profit_brute, best_combination_brute = brute_force_max_profit(prices, profits, budget)
print(f"Brute Force - Maximum Profit: {max_profit_brute}")
print(f"Brute Force - Best Combination: {best_combination_brute}")
