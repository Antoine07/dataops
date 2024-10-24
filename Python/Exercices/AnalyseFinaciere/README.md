# Analyse finacière

### 1. Méthode Brute Force

Nous allons générer toutes les combinaisons possibles de parts (actions) et calculer les profits totaux pour chaque combinaison.

### 2. Méthode Optimisée

Pour une version optimisée, nous allons utiliser une approche basée sur la programmation dynamique ou une approche gloutonne (greedy), selon le cas d'utilisation.

### Code Python

Voici le code qui met en œuvre les deux méthodes :

```python
import numpy as np
from itertools import combinations

# Données fournies
data = {
    "name": ["Share-DUPH", "Share-GTAN", "Share-USUF", "Share-CFOZ", "Share-QLRX",
             "Share-XJDT", "Share-HKFP", "Share-PPPH", "Share-HLJY", "Share-YKBD",
             "Share-CTCR", "Share-LMJG", "Share-IGUH", "Share-VIRY", "Share-PYDS",
             "Share-SOOE", "Share-NOIQ", "Share-QUXB", "Share-SJNY", "Share-DJNY"],
    "price": [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114],
    "profit": [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
}

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
```

### Explications

- **Méthode Brute Force**: Elle génère toutes les combinaisons d'actions possibles et calcule le profit total pour chaque combinaison. Cela peut être lent si le nombre d'actions est élevé, car la complexité est exponentielle.
  
- **Méthode Optimisée**: Elle trie les actions par rapport à leur rapport profit/prix et choisit les actions jusqu'à ce que le budget soit épuisé. Cela permet de trouver une solution rapidement.
