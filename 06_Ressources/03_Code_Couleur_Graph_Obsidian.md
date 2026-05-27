# Code Couleur - Graph Obsidian

## Objectif

Colorer le graph global Obsidian pour repérer rapidement :

- le socle validé ;
- les grands sujets ;
- les projets encore en construction ;
- les ressources annexes.

La configuration est dans :

```text
.obsidian/graph.json
```

## Légende du graph

| Couleur | Signification | Requête Obsidian |
| --- | --- | --- |
| Or | Hubs / fichiers centraux | `fruits.md`, `FRUITS 🍋‍🟩.md`, `00_Diagnostic_360.md` |
| Vert | Socle validé / décisions structurantes | plan global, stratégies empilables, capital stack, ADP, refinancement, rémunération Fruits |
| Bleu | Stratégie | dossier `01_Strategie` |
| Rose | Investisseurs / financeurs | dossier `02_Investisseurs` |
| Violet | Juridique | dossier `03_Juridique` |
| Orange | Opérationnel | dossier `04_Operationnel` |
| Turquoise | Prospection | dossier `05_Prospection` |
| Gris clair | Ressources | dossier `06_Ressources` |
| Gris foncé | Attachments | dossier `Attachments` |
| Blanc / gris par défaut | Reste non classé | aucun groupe appliqué |

## Lecture rapide

```text
or = centre du projet
vert = déjà structuré / validé comme socle
bleu = stratégie
rose = investisseurs
violet = juridique
orange = opérationnel
turquoise = prospection
gris = ressources ou pièces jointes
blanc = reste / à classer
```

## Statut validé

Un fichier n'est pas forcément “terminé” parce qu'il est vert. Vert veut dire :

```text
base structurante validée pour avancer
```

Cela inclut :

- plan global ;
- stratégies empilables ;
- capital stack ;
- SPV + actions de préférence ;
- refinancement ;
- rémunération Fruits / waterfall.

## Ajouter un fichier au socle validé

Dans `.obsidian/graph.json`, ajouter son chemin dans le groupe vert :

```text
path:"NOM_DU_DOSSIER/NOM_DU_FICHIER.md"
```

Exemple :

```text
OR path:"04_Operationnel/09_Modeles_Math_Check.md"
```

## Note pratique

Si Obsidian est déjà ouvert, il peut être nécessaire de fermer/réouvrir le vault ou de relancer le graph pour que les couleurs soient prises en compte.
