def greedy_max_profit(prices, profits, budget):
    # Utiliser zip pour créer un générateur d'items
    items = sorted(((price, profit, name) for price, profit, name in zip(prices, profits, data["name"])), 
                   key=lambda x: x[1] / x[0], 
                   reverse=True)
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
