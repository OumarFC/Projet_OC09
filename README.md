# Projet 9 : Développez une application Web en utilisant Django

![logo.png](logo.png)


## Sommaire

+ [Objectif du projet ](#Objectif)
+ [Installation du projet](#Installation)
+ [Installation des packages](#Packages)
+ [Le fichier .gitignore](#gitignore)
+ [Lancement](#Démarrage)
+ [Flake8](#Rapport flake8)


## Objectif

Projet consistant à créer un site web pour la start-up LITReview. Son objectif est de créer un site web permettant à une communauté de passionnés de livres de pouvoir échanger des avis.

La conception du site doit utiliser le framework Django, les contraites seront plutot basées sur la réalisation du backend.
Le projet utilise les langages HTML, CSS et Python.

Le site doit pouvoir réaliser les point ci-desous listés :
 - L'utilisateur doit pouvoir créer un compte et se connecter.
 - L'utilisateur doit pouvoir demander et poster des critiques.
 - L'utilisateur doit pouvoir suivre d'autres d'utilisateurs, et avoir accès à une page où il peut vérifier les utilisateurs suivis ainsi que ceux qui le suivent.
 - L'utilisateur doit avoir accès à une page où sont situés toutes ses critiques et demandes de critiques.
 - L'utilisateur doit avoir accès à une page de flux, affichant les différentes critiques et demandes. 


## Installation
  
1- Télécharger et installer la dernière version de Python à cette adresse :
	https://www.python.org/downloads/
		 
2 - Depuis votre terminal sous windows ( cmd )  

Verifiez que vous avez pip installer sur la machine
pour cela lancer la commande 

```pip --help```

- Créer votre dossier projet sous windows
	     
```
mkdir < MyProject09 > 
```
où MyProject09 est le nom de votre projet,
placez-vous dans le repertoire projet
```
cd < MyProject09 > 
```
Créer votre environnement virtuel
```
pip -m venv < myenv > 
```
Où myenv est le nom pour votre environnement virtuel.
Activez votre environnement virtuel.
```
cd < myenv\scripts\ctivate.bat
```

##packages

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont répertoriés dans le fichier ```requirements.txt```
Sous windows lancer la commande:

pip install -r requirement.txt

```
afin d'installer toutes les librairies.

```
## gitignore

Exclure l'environnement virtuel des commits sur le serveur distant 
	
Créez le fichier .gitignore à la racine de votre projet:   

```~\MyProject09\.gitignore ```

Editez le fichier .gitignore et ajouter les fichiers et repertoire que vous souhaitez exclure   

## Démarrage 

Le programme est écrit en Python, copier tous les fichiers et répertoires du repository, 
aviguer vers le répertoire MyProject09 et entrez dans la commande suivante dans le terminal pour lancer le serveur :

``` ~\MyProject09
manage.py runserver
```

Entrez l'adresse suivante dans le navigateur : http:/127.0.0.1:8000/ 
Vous pouvez vous connecter à l'interface d'administration via le compte admin "itecglobalservices"  mot de passe "dyste222" (sans les doubles quotes).


## Rapport flake8

