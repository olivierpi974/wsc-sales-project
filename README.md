# Analyse des ventes d'une PME

Projet d'admission Wild Code School — Formation Data Engineer

## Description

Pipeline de données end-to-end pour analyser les ventes d'une PME sur 30 jours.
Architecture deux services Docker : exécution des scripts Python + stockage SQLite.

## Architecture

![Architecture](assets/Schéma_architecture.png.png)

- **Service app** : conteneur Python — collecte, transformation et ingestion
- **Service db** : conteneur SQLite — héberge le volume de stockage
- **Volume partagé** : pas de communication réseau — SQLite est un fichier

## Modèle de données

![MCD](assets/Schéma_donnée.png)

## Stack technique

- Python 3.12
- SQLite3
- Docker / Docker Compose
- pandas, requests

## Lancer le projet

    docker compose up --build

Le pipeline s'exécute automatiquement :

1. Création de la base de données et des tables
2. Collecte des CSV depuis les URLs client via HTTP
3. Ingestion des données (idempotente pour les ventes via INSERT OR IGNORE)
4. Analyses SQL et stockage des résultats

## Structure

    wcs-sales-project/
    ├── Dockerfile
    ├── compose.yml
    ├── requirements.txt
    ├── src/
    │   ├── main.py        # Ingestion
    │   └── analysis.py    # Analyses SQL
    ├── sql/
    │   ├── create_table.sql
    │   ├── total_ca.sql
    │   ├── vente_produit.sql
    │   └── vente_region.sql
    └── assets/
        ├── Schéma_architecture.png
        └── Schéma_donnée.png

## Résultats d'analyse

Le chiffre d'affaires du client s'élève à 5 268,78 € sur la période de 30 jours. La région qui vend le mieux est l'Auvergne-Rhône-Alpes. Le produit qui rapporte le plus est REF004 avec un total de 1 679 € sur 21 articles. Néanmoins les clients achètent plus le produit REF005 avec une quantité totale de 35 articles.
Projet d'admission Wild Code School — Formation Data Engineer

## Description

Pipeline de données end-to-end pour analyser les ventes d'une PME sur 30 jours.
Architecture deux services Docker : exécution des scripts Python + stockage SQLite.

## Architecture

![Architecture](assets/Schéma_architecture.png)

- **Service app** : conteneur Python — collecte, transformation et ingestion
- **Service db** : conteneur SQLite — héberge le volume de stockage
- **Volume partagé** : pas de communication réseau — SQLite est un fichier

## Modèle de données

![MCD](assets/Schéma_donnée.png)

## Stack technique

- Python 3.12
- SQLite3
- Docker / Docker Compose
- pandas, requests

## Lancer le projet

    docker compose up --build

Le pipeline s'exécute automatiquement :

1. Création de la base de données et des tables
2. Collecte des CSV depuis les URLs client via HTTP
3. Ingestion des données (idempotente pour les ventes via INSERT OR IGNORE)
4. Analyses SQL et stockage des résultats

## Structure

    wcs-sales-project/
    ├── Dockerfile
    ├── compose.yml
    ├── requirements.txt
    ├── src/
    │   ├── main.py        # Ingestion
    │   └── analysis.py    # Analyses SQL
    ├── sql/
    │   ├── create_table.sql
    │   ├── total_ca.sql
    │   ├── vente_produit.sql
    │   └── vente_region.sql
    └── assets/
        ├── Schéma_architecture.png
        └── Schéma_donnée.png

## Résultats d'analyse

Le chiffre d'affaires du client s'élève à 5 268,78 € sur la période de 30 jours. 
La région qui vend le mieux est l'Auvergne-Rhône-Alpes. 
Le produit qui rapporte le plus est REF004 avec un total de 1 679 € sur 21 articles. 
Néanmoins les clients achètent plus le produit REF005 avec une quantité totale de 35 articles.
