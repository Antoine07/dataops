import numpy as np
import urllib.request
import pandas as pd 
"""

1. Donnez le nombre de femmes qui ont survécu.

2. Donnez le pourcentage de femmes qui ont survécu.

"""

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
data = urllib.request.urlopen(url)
# print(data)

# DataFrame
titanic_data =  pd.read_csv(data)

# # Afficher les premières lignes pour vérifier le chargement
# print(titanic_data[:5])

total = titanic_data['PassengerId'].count()
mask =  titanic_data['Sex'] =='female' 

# print(titanic_data[mask])

female_survived = sum( titanic_data[mask]['Survived'] )

# nombre de survivantes femmes
print(female_survived)

nbFemale = sum( mask )
print(nbFemale)

print(f"pourcentage de femmes survivantes : {round( female_survived/nbFemale * 100, 2 ) } %")

# Par rapport 
mask =  titanic_data['Sex'] =='male' 
nbMale = sum(mask)
male_survived = sum( titanic_data[mask]['Survived'] )

print(f"pourcentage de hommes survivants : {round( male_survived/nbMale * 100, 2 ) } %")
