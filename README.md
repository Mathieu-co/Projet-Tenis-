# 8INF867_Projet

---

# Sommaire
I. [English version](#i-english-version)

II. [Version française](#ii-version-française)
   
   1. [Traitement en binaire](#a-traitement-en-binaire)

       a. [Prétraitement des données](#1-prétraitement-des-données)
       
       b. [Analyse des données](#2-analyse-des-données)
    
   1. [Traitement en multiclass](#b--traitement-en-multiclass)

       a. [Prétraitement des données](#1-prétraitement-des-données)
       
       b. [Analyse des données](#2-analyse-des-donnc3a9es-1)
    

# I. English version

This project uses data from [tennis-data.co.uk][1], a website that provides statistics on professional tennis matches. The goal of the project is to predict the outcome of the matches using different machine learning models.

.....

# II. Version française

Ce projet utilise les données de [tennis-data.co.uk][1], un site qui fournit des statistiques sur les matchs de tennis professionnels. Le but du projet est de prédire l'issue des matchs en utilisant différents modèles d'apprentissage automatique.

## A. Traitement en binaire

Dans cette partie, on considère le problème de prédiction comme un problème de classification binaire, où on cherche à prédire si le joueur 1 gagne ou perd le match.

### 1.  Prétraitement des données

Pour prétraiter les données, on exécute le fichier `prepocessing_ATP.ipynb`. Ce fichier permet de filtrer les données, car beaucoup de données sont inutiles ou manquantes. Une fois exécuté, ce fichier crée un fichier CSV nommé `all_matches_ATP.csv`, qui contient les données nettoyées.

### 2. Analyse des données

Pour analyser les données, on exécute le fichier `main_ATP.ipynb` ou `main_CNN.ipynb`. Ces fichiers permet de voir les résultats pour différents modèles de classification binaire, comme la régression logistique, les arbres de décision, les forêts aléatoires, etc. Il affiche également des graphiques et des mesures de performance, comme la précision, le rappel, le F1-score, etc.

## B . Traitement en multiclass

Dans cette partie, on considère le problème de prédiction comme un problème de classification multiclasse, où on cherche à prédire le score exact du match, c'est-à-dire le nombre de sets gagnés par chaque joueur.

### 1. Prétraitement des données

Pour prétraiter les données, on exécute le fichier `prepocessing_ATP_multiclass.ipynb`. Ce fichier permet de créer une nouvelle variable cible qui représente le score exact du match. Il crée également un fichier CSV nommé `all_matches_ATP_multiclass.csv`, qui contient les données modifiées.

### 2. Analyse des données

Pour analyser les données, on exécute le fichier `main_ATP_multiclass.ipynb`. Ce fichier permet de voir les résultats pour différents modèles de classification multiclasse, comme le k-plus proches voisins, le naïf bayésien, le perceptron multicouche, etc. Il affiche également des graphiques et des mesures de performance, comme la précision, le rappel, le F1-score, etc.

[1]: http://www.tennis-data.co.uk/alldata.php



