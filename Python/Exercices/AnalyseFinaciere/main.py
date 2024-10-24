import numpy as np
from itertools import combinations

# Données fournies

data = pd.read_csv('data.csv', na_values=['NA', 'NULL'])

# Convertir en tableau NumPy
prices = np.array(data["price"])
profits = np.array(data["profit"])

# 1. Méthode Brute Force
def brute_force_max_profit(prices, profits):
    max_profit = 0
    best_combination = []
    
    # Tester toutes les combinaisons de parts
    for r in range(1, len(prices) + 1):
        for combo in combinations(range(len(prices)), r):
            total_profit = np.sum(profits[list(combo)])
            if total_profit > max_profit:
                max_profit = total_profit
                best_combination = combo
    
    return max_profit, [data["name"][i] for i in best_combination]

# Résultat de la méthode brute force
max_profit_brute, best_combination_brute = brute_force_max_profit(prices, profits)
print(f"Brute Force - Maximum Profit: {max_profit_brute}")
print(f"Brute Force - Best Combination: {best_combination_brute}")

# 2. Méthode Optimisée (Approche Greedy)
def greedy_max_profit(prices, profits, budget):
    items = sorted(zip(prices, profits, data["name"]), key=lambda x: x[1]/x[0], reverse=True)
    total_profit = 0
    selected_items = []

    for price, profit, name in items:
        if budget >= price:
            budget -= price
            total_profit += profit
            selected_items.append(name)

    return total_profit, selected_items

# Exécuter la méthode optimisée
budget = 300  # Exemple de budget à définir
max_profit_greedy, best_combination_greedy = greedy_max_profit(prices, profits, budget)
print(f"Greedy Approach - Maximum Profit: {max_profit_greedy}")
print(f"Greedy Approach - Best Combination: {best_combination_greedy}")
