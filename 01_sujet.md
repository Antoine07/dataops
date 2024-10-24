
### Objectif du TP

L'objectif de ce TP est de créer un service API avec FastAPI qui interagira avec une base de données MySQL. Les étudiants devront charger des données depuis un fichier CSV, insérer ces données dans une table SQL, et permettre la récupération et l'ajout de nouvelles transactions via des endpoints API.

### Prérequis

- Docker et Docker Compose installés
- Connaissances de base en Python et FastAPI
- Connaissances de base en SQL et MySQL

### Étapes à suivre

#### 1. Créer l'arborescence du projet

Créez la structure de fichiers suivante :

```
/dataops_tp
├── app
│   ├── __init__.py
│   ├── main.py
├── data.csv
├── Dockerfile
└── docker-compose.yml
```

#### 2. Fichier CSV

Créez un fichier `data.csv` dans le dossier `dataops_tp` avec le contenu suivant :

```csv
id,name,amount,date
1,John Doe,1000.50,2023-10-01
2,Jane Smith,1500.75,2023-10-02
3,Bob Johnson,750.00,2023-10-03
4,Alice Davis,1300.25,2023-10-04
5,Charlie Brown,1100.90,2023-10-05
```

#### 3. Fichier Dockerfile

Créez un fichier `Dockerfile` dans le dossier `dataops_tp` :

```dockerfile
# Utiliser l'image de base Python
FROM python:3.12

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code dans le conteneur
COPY ./app /app

# Exposer le port pour FastAPI
EXPOSE 8001

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
```

#### 4. Fichier requirements.txt

Créez un fichier `requirements.txt` dans le dossier `dataops_tp` :

```
fastapi
uvicorn
pandas
numpy
mysql-connector-python
```

#### 5. Fichier docker-compose.yml

Créez un fichier `docker-compose.yml` dans le dossier `dataops_tp` :

```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8081:8000"  # Expose le port 8000 de l'application sur le port 8081 de l'hôte
    volumes:
      - ./app:/app
      - ./data.csv:/data.csv  # Monte le fichier CSV si nécessaire
    environment:
      - MYSQL_HOST=db
      - MYSQL_DATABASE=marketing_db
      - MYSQL_USER=user
      - MYSQL_PASSWORD=password
    command: uvicorn main:app --reload --host 0.0.0.0 --port 8000

  db:
    image: mysql:5.7
    environment:
      MYSQL_DATABASE: marketing_db
      MYSQL_USER: user
      MYSQL_PASSWORD: password
      MYSQL_ROOT_PASSWORD: root_password
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql  # Monte un volume pour la persistance de la base de données

  adminer:
    image: adminer
    ports:
      - "8082:8080"

volumes:
  db_data:  # Déclaration du volume pour la base de données
```

#### 6. Fichier main.py

Créez un fichier `main.py` dans le dossier `app` :

```python
from fastapi import FastAPI, HTTPException
import pandas as pd
import mysql.connector
import logging
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configuration des logs
logging.basicConfig(filename='pipeline.log', level=logging.INFO)

# Connexion à MySQL
def get_db_connection():
    return mysql.connector.connect(
        host='db',
        database='marketing_db',
        user='user',
        password='password'
    )

# Modèle pour ajouter de nouvelles données via API
class Transaction(BaseModel):
    id: int
    name: str
    amount: float
    date: str

# Récupération des données depuis le fichier CSV
@app.get("/load-csv")
def load_csv_data():
    try:
        df = pd.read_csv('data.csv')
        df = clean_data(df)
        store_data_to_mysql(df)
        return {"message": "Données CSV chargées avec succès", "data": df.to_dict(orient='records')}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors du chargement du fichier CSV : {e}")

# Récupération des données depuis MySQL
@app.get("/data")
def get_all_data():
    try:
        df = fetch_data_from_mysql()
        return df.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des données : {e}")

# Endpoint pour ajouter de nouvelles données via POST
@app.post("/data")
def add_new_data(data: List[Transaction]):
    try:
        df = pd.DataFrame([d.dict() for d in data])
        clean_df = clean_data(df)
        store_data_to_mysql(clean_df)
        return {"message": "Données ajoutées avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'ajout des données : {e}")

# Endpoint pour récupérer des statistiques basiques
@app.get("/stats")
def get_stats():
    try:
        df = fetch_data_from_mysql()
        stats = {
            "total_rows": len(df),
            "average_amount": df["amount"].mean(),
            "total_amount": df["amount"].sum(),
        }
        return stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des statistiques : {e}")

# Nettoyage et traitement des données
def clean_data(df: pd.DataFrame):
    df.dropna(inplace=True)  # Supprime les lignes avec des valeurs manquantes
    df['date'] = pd.to_datetime(df['date'])  # Conversion du format de date
    df.drop_duplicates(inplace=True)
    logging.info("Données nettoyées")
    return df

# Stocker les données dans MySQL
def store_data_to_mysql(df: pd.DataFrame):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO transactions (id, name, amount, date)
                VALUES (%s, %s, %s, %s)
            """, (row['id'], row['name'], row['amount'], row['date']))
        connection.commit()
        logging.info("Données stockées dans MySQL")
    except mysql.connector.Error as e:
        logging.error(f"Erreur lors de l'insertion des données MySQL : {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Récupération des données depuis MySQL
def fetch_data_from_mysql():
    try:
        connection = get_db_connection()
        query = "SELECT * FROM transactions"
        df = pd.read_sql(query, connection)
        logging.info("Données récupérées depuis MySQL")
        return df
    except mysql.connector.Error as e:
        logging.error(f"Erreur MySQL : {e}")
    finally:
        if connection.is_connected():
            connection.close()
```

### 7. Création de la table SQL

Avant de lancer l'application, il faut s'assurer que la table SQL existe. Vous pouvez le faire via Adminer ou un client MySQL en exécutant la requête suivante :

```sql
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    date DATE NOT NULL
);
```

### 8. Lancer l'application

Ouvrez un terminal et naviguez jusqu'au dossier `dataops_tp`. Exécutez la commande suivante pour construire et démarrer les conteneurs :

```bash
docker-compose up --build
```

### 9. Tester l'API

Une fois que l'application est en cours d'exécution, vous pouvez accéder à l'API à l'adresse suivante :

- **FastAPI** : [http://localhost:8081](http://localhost:8081)
- **Adminer** : [http://localhost:8082](http://localhost:8082) (pour gérer la base de données)

### 10. Utilisation des endpoints

- **Charger les données depuis le CSV** : Envoyez une requête GET à `/load-csv`.
- **Récupérer toutes les données** : Envoyez une requête GET à `/data`.
- **Ajouter de nouvelles données** : Envoyez une requête POST à