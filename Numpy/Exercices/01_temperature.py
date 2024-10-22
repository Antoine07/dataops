"""
Exercice température

Nous avons relevé des températures au mois de Janvier. Répondez aux questions suivantes :

1. Donnez toutes les températures qui sont supérieures à 0.

2. Comparez les températures supérieures et inférieures à 0.

3. Donnez le pourcentage des températures positives sur le mois.

4. Créez un tableau days pour les jours du mois et donnez les jours pour lesquels la température était supérieure à 0.

5. Donnez toutes les températures supérieures à 0 à partir du dixième jour du mois.

6. Remplacez maintenant les températures négatives par la moyenne des températures positives.

```python
january = np.array([-2,  5, -5,  6, -2,  0,  6,  2,  8,  0,  6, -1,  3,  3,  7,  0, -5,
        7,  4,  7,  8, -1,  5, -2,  3, -3, -2,  7,  8,  4,  2])
```

"""
import numpy as np 

january = np.array([-2,  5, -5,  6, -2,  0,  6,  2,  8,  0,  6, -1,  3,  3,  7,  0, -5,
        7,  4,  7,  8, -1,  5, -2,  3, -3, -2,  7,  8,  4,  2], dtype='float64')

print( "1. Donnez toutes les températures qui sont supérieures à 0.")

print( january[january > 0] )

print("2. Comparez les températures supérieures et inférieures à 0.")

print( sum(january > 0 ) > sum(january <= 0 )   )

print("3. Donnez le pourcentage des températures positives sur le mois.")

print( f" { round( ( sum( january > 0 )  / len(january) ) * 100 , 2 ) } % " )

print("4. Créez un tableau days pour les jours du mois et donnez les jours pour lesquels la température était supérieure à 0.")

days = np.array( range(1, len(january) + 1))
# print(days)
print(days[january > 0])

print( "5. Donnez toutes les températures supérieures à 0 à partir du dixième jour du mois.")
# start:end:step
print( january[9:] [ january[9:] > 0 ] )

# rappels slicing
l = [1, 2, 3, 4, 5, 6]
# à partir de l'indice 3 jusqu'à la fin
print(l[3:])
# par step de 2
print(l[3::2])

print( "6. Remplacez maintenant les températures négatives par la moyenne des températures positives." )

average_positif =  round ( sum ( january[(january > 0)] ) / len(january), 2 )
print(average_positif)
january[ january < 0] = average_positif

print(january)