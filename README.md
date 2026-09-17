# 🐰 Evolution Simulation

Une petite simulation d'évolution en Python/Pygame : des **villageois** évoluent dans un
monde peuplé de **carottes**, avec l'objectif (à terme) de simuler des comportements
émergents — recherche de nourriture, survie, reproduction, sélection naturelle.

> Projet pédagogique pour apprendre à construire une simulation d'évolution simple.

## Aperçu

- Fenêtre Pygame de 1200x600
- Une population de villageois placés aléatoirement sur la carte
- Des carottes disséminées comme ressource
- Boucle de simulation à 60 FPS

## Prérequis

- Python >= 3.14

## Installation

Le projet utilise un `Makefile` pour automatiser la création de l'environnement virtuel
et l'installation des dépendances.

```bash
make
```

Cette commande va :
1. Créer un environnement virtuel dans `.venv`
2. Installer le projet en mode développement (`pip install -e .`)

## Lancer la simulation

```bash
make run
```

Contrôles :
- `Échap` ou fermer la fenêtre : quitter la simulation

## Nettoyage

Pour supprimer les fichiers temporaires, le cache Python et l'environnement virtuel :

```bash
make clean
```

Pour tout réinstaller proprement (`clean` + `install`) :

```bash
make re
```

## Structure du projet

```
.
├── Makefile            # Commandes d'installation / exécution / nettoyage
├── pyproject.toml       # Métadonnées du projet et dépendances
└── src/
    ├── main.py          # Point d'entrée, boucle principale et rendu Pygame
    ├── Villager.py       # Classe représentant un villageois
    ├── Carrot.py         # Classe représentant une carotte
    └── Point.py          # Utilitaire de coordonnées 2D
```

## Auteur

Hugo Chartier