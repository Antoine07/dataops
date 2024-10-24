# Installation

1. Installez Docker Desktop 

2. Dans le dossier DataOps créez work, tapez la ligne de commande suivante pour installer 

```bash
# Soit directement jupyter 
# docker pull jupyter/datascience-notebook
docker run -it --rm -p 10000:8888 -v "${PWD}/":/home/jovyan/work quay.io/jupyter/datascience-notebook:2024-04-29

# Token et mot de passe
jupyter server list
# récupération du token et définition du mot de passe

```