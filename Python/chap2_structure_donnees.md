# Structure de données

Nous avons déjà abordé les listes comme structure de données.

## Dictionnaire

Un autre type natif existe en Python : les dictionnaires. Ils sont indexés par des clés, qui peuvent être de n'importe quel type **immuable**, comme par exemple les chaînes de caractères ou les nombres.

Il existe une fonction de hash qui permet de liée une clé à une valeur de manière unique.

**Par contre une liste ne peut être une clé car mutable.**

Un dictionnaire est **un ensemble non ordonné** de pair clé/valeur devant être unique dans le dictionnaire.

On peut définir un dictionnaire en utilisant une paire d'accolade vide :

```python
a = {}
```

 Les principales opérations sur les dictionnaires sont de stocker une valeur pour une clé et extraire la valeur correspondante pour une clé. 
 On peut également supprimer une paire clé/valeur avec l'opérateur del de Python.
 Attenion, si vous stockez une valeur pour une clé déjà présente dans le dictionnaire l'ancienne valeur sera perdue. 

 Et si vous essayez d'accéder à une valeur pour une clé qui n'existe pas une exception sera levée.

 Comme clé unique vous pouvez par exemple utiliser un tuple qui repère de manière certaine une personne se trouvant sur un plan.

```python
persons = { (1, 2, 3) : ["Alan", "Albert" ], (3,5,7) : ["Sophie"] }
```

Un dictionnaire est un tableau de hash, ceci permet d'accéder à une valeur du dictionnaire en un temps constant et extrèmement rapide.

De même vérifier qu'une clé existe est directe :

```python
students = { 'alan' : 1, 'albert' : 2 , 'brice' : 3 }
print('albert' in students)
```

La fonction map et le mot clé hash permettent de voir les hash dans la structure de dictionnaire.

Dans un tableau de hash on implémente une fonction f(key,dict) permettant d'accéder directement à une valeur du dictionnaire. Notons que la fonction de hash de Python est très rapide.

```python
students = { 'alan' : 1, 'albert' : 2 , 'brice' : 3 }
for h in map(hash, students): 
    print(h) 
"""
1623984986049861657
-2969457881634950836
8552435218161168756
"""
```

Le constructeur dict permet de transformer une liste de tuples en dictionnaire, le tuple doit sous forme clé/valeur.

```python
l = [('alan', 1), ('albert' ,2) , ('brice', 3) ]
lDic = dict(l)
```

### Opérations sur les dictionnaires

```python
students = { 'alan' : 1, 'albert' : 2 , 'brice' : 3 }
students['alan'] = 1001
students['alan'] # 1001
del students['alan'] # supprime cet clé/valeur
students.keys() # crée une liste de clés 
students.values() # crée une liste de valeurs 

```

On peut également vouloir parcourir sous forme d'une liste de clé/valeur un dictionnaire, dans ce cas vous avez la méthode items :

```python
for (k, v) in students.items():
    print(k, v)

students.items() 
# donne une liste particulière qui vient d'un dict
# dict_items([('alan', 1), ('albert', 2), ('brice', 3)])
```

## Les tuples 

 Les tuples sont un autre type natif dit de **séquence** comme les listes et les dictionnaires, les tuples sont **non modifiables** (non mutable), ils n'ont pas de méthode. 
**Un tuple est donc protégé en écriture**. C'est un tableau de hash donc rapide pour l'accès et le parcours de ses éléments. Comme il est non mutable on peut l'utiliser comme clé d'une liste par exemple. On rappelle qu'une clé d'une liste doit être non mutable.

```python
# définition d'un tuple
t = 'a', 'b', 'c'

# de manière équivalente
p = ('a', 'b', 'c')
```

- Ils peuvent être imbriqués :

```python
# définition d'un tuple
t = 'a', 'b', 'c'
u = t, (1,2,4)
print(u)
# ('a', 'b', 'c', (1,2,4))
```

Notez que souvent on utilisera des parenthèses pour définir un tuple par exemple : (1,2,3). Dans certains cas ils seront nécessaires, comme les tuples imbriqués.

## protection en écriture

 On peut accéder à une valeur d'un tuple **mais on ne peut pas modifier une de ses valeurs** :

```python
# définition d'un tuple
t = 1, 2
# accès
t[0]
```

Par contre un tuple est immuable donc on peut pas ré-assigner une valeur :

```python
# définition d'un tuple
t = 1, 2
# accès
t[0] = 8 # TypeError 'tuple' object does not support item assigment
```

- Déballage de séquence. 

L'opération suivante permet de déballer des valeurs d'un tuple dans des variables :

```python
t = ('a', 'b', 'c')
x,y,z = t
```

- La fonction zip 

```python
languages = ['JS', 'Python', 'PHP'] 
versions = [6, 3, 8] 
res = zip(languages, versions)
print(list(res))
#[('JS', 6), ('Python', 3), ('PHP', 8)]
 ```

 - Déballage ou unpacking en Python

 Vous pouvez également déballer une partie dans des variables et une autre **dans une liste**

 ```python
 x, *y = ( 100, (200, 300 ), (500, 900) )   
 print(x)
 # 100
 print(y)
 # [(200, 300 ), (500, 900)]
 ```

## Les ensembles 

**Python fournit également un type de donnée pour les ensembles. Un ensemble est une collection non ordonnée sans élément dupliqué.** 

Les ensembles supportent les opérations mathématiques comme les unions, intersections, différences et différences symétriques. 
Pour définir un ensemble on peut utiliser les accolades mais attention on ne peut pas définir un ensemble vide comme suit {} (dans ce cas cela définit un dictionnaire).

Pour définir un ensemble vide on utilisera la déclaration Python suivante : set().

```python
a =set('aaabbbccc')
print(a)
# {'b', 'a', 'c'}
```

Sur les ensembles à la notion de différence :

```python
A = {'b', 'a', 'c'}
B = {'r', 'c'}
# Différence entre A et B
print(A-B)
# {'b', 'a'}

# Différence entre B et A
print(B-A)
# {'r'}
```

Sur les ensembles à la notion de l'union :

```python
A = {'b', 'a', 'c'}
B = {'r', 'c'}
print(A|B)
# {'r', 'b', 'a', 'c'}
```

Sur les ensembles intersecion :

```python
A = {'b', 'a', 'c'}
B = {'r', 'c'}
print(A&B)
# {'c'}
```

A ou B mais pas les deux 

```python
A = {'b', 'a', 'c'}
B = {'r', 'c'}
print(A^B)
# {'b', 'r', 'a'}
```

Les compréhensions de liste peuvent être utiliser sur les ensembles.

```python
a = { x for x in zip( [1,1,1], [1,1,1] ) }
# {(1, 1)}
```

## 01 Exercice mississippi

Soit la chaîne de caractères suivante : "mississippi". Comptez le nombre d'occurence de chaque lettre(s).

## 02 Entiers inversés

Nous souhaitons créer une fonction qui permet d'inverser des entiers signés ou non :

Par exemples :

-6523 donnerait -3256 

123 donnerait 321

Utilisez les notions du cours pour créer cette fonction. Notamment pensez à caster vos données afin de pouvoir les utiliser avec d'autre(s) fonction(s).


## 03 Recherche d'un mot dans un texte

Un problème récurrent en analyse de données consiste à rechercher une séquence de valeur dans un tableau.

Ci-dessous on cherche la séquence   

```python
l = [1,3,7,8,9,1,2,3,8, 1, 2, 3, 7, 8, 9, 1, 2, 3, 8, 10, 1, 2, 3]
```

1. Créez une fonction qui permette de rechercher un mot dans un texte ou une liste, notez que cette fonction sera identique pour un texte, un itérable... Il serait intéressant que cette fonction retourne le premier indice de la position de la séquence trouvée dans la liste. 

2. Retournez maintenant tous les indices de toutes les séquences trouvées dans la liste.


## 04 Calculez la longueur moyenne

1. Créez une fonction qui donne la longueur moyenne des mots et particules dans une phrase. Utilisez la fonction split sur une chaîne de caractères pour transformer la chaîne en tableau.

Remarques pour retirer les caractères de ponctuation dans la phrase vous pouvez utiliser le code suivant basé sur les expressions régulières :

```python
import re
s = "Hello World, . ; ?"
# le troisième paramètre permet d'ignorer la case
# dans des crochets cela signifie tout ce qui n'est pas un mot ou un espace sera remplacé par une chaîne de caractère vide
s = re.sub(r"[^\w\se]", "", s, flags=re.IGNORECASE)
```
Une autre fonction Python peut également être utile, permettant de remplacer certain(s) caractère(s) par autre chose :

```python
"Bonjour 'tout' le monde".replace(r'"\'', "")
```

Extrait d'un article de Wikipédia (Python) :

```python
phrase = "Le langage Python est placé sous une licence libre proche de la licence BSD6 et fonctionne sur la plupart des plates-formes informatiques, des smartphones aux ordinateurs centraux7, de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, et peut aussi être traduit en Java ou .NET. Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser."
```