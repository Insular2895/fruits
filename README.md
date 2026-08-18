# Fruits

Vault de travail pour structurer le projet Fruits : stratégie immobilière, financement par SPV, investisseurs, refinancement, gouvernance, prospection et modèles de risque.

Le projet part d'une idée simple : construire un opérateur immobilier discipliné, actif par actif, avec des SPV isolées, des réserves dédiées, des financeurs adaptés à chaque stade et une logique de rendement prioritaire sans promesse garantie.

> Document de travail. Les montages juridiques, fiscaux et financiers doivent être validés par avocat, notaire, fiscaliste, expert-comptable et financeurs avant exécution.

## Source de vérité

La branche `main` de ce dépôt est la source canonique du projet Fruits.

Pour éviter la duplication inutile :

- les décisions et règles structurantes vivent dans les dossiers `00` à `05` ;
- les ressources, backlog et sources historiques synthétiques vivent dans `06_Ressources` ;
- les anciens dossiers `07_A_Completer_A_Revoir` et `08_Conversations_GPT_Sources` ont été fusionnés pour éviter la dispersion.

Les sources historiques servent de mémoire et de matière première. Elles ne remplacent pas les décisions validées dans le diagnostic, les packs investisseurs ou les notes opérationnelles.

## Lecture rapide

- [Index complet du vault](fruits.md)
- [Diagnostic 360](00_Diagnostic_360.md)
- [Chassis standard Fruits](04_Operationnel/00_Chassis_Standard_Fruits.md)
- [Plan global 1M et execution](01_Strategie/02_Plan_Global_1M_Et_Execution.md)
- [Capital stack / financeurs](02_Investisseurs/00_Capital_Stack.md)
- [Modeles math check](04_Operationnel/09_Modeles_Math_Check.md)
- [Refinancement](04_Operationnel/10_Refinancement.md)
- [Vente à terme / crédit vendeur — système Fruits](04_Operationnel/12_Vente_A_Terme_Credit_Vendeur_Fruits.md)
- [Remuneration Fruits / waterfall](04_Operationnel/11_Remuneration_Fruits_Waterfall.md)
- [Finance playbooks - extraction Fruits](06_Ressources/10_Finance_Playbooks_Extraction_Fruits.md)

## Structure du projet

```text
.
├── 00_Diagnostic_360.md
├── 01_Strategie/
├── 02_Investisseurs/
├── 03_Juridique/
├── 04_Operationnel/
├── 05_Prospection/
├── 06_Ressources/
├── Attachments/
└── fruits.md
```

## Axes principaux

### Strategie

- Lombard prudent : LTV cible 20-25%, maximum interne 30%, reserve cash 30-50% du lombard.
- ETF / T-Bills / monetaire : reserve et allocation encadrees, sans confondre tresorerie de securite et moteur de rendement.
- FX / currency : financement en devise seulement si le risque est compris, couvert et coherent avec les flux.
- Strategies empilables : distinction entre ce qui peut etre combine et ce qui doit rester separe.

### Investisseurs

Le dossier couvre les principaux financeurs possibles :

- Family Offices
- Private debt bridge / asset-based
- UHNWI
- Foncieres privees
- Banques privees
- Private debt structure
- Fonds immobiliers core / core+
- BPI, Banque des Territoires, CDC
- Assureurs, mutuelles, caisses de retraite
- Institutions, fonds souverains, large allocators
- Banque d'affaires / arranger
- Private credit / LBO
- Crowdfunding PSFP
- SCPI / OPCI / SIIC
- Credit vendeur
- Credit-bail immobilier / leaseback

Chaque pack vise a definir :

- le produit compatible avec le financeur ;
- le ticket cible et l'horizon ;
- la structure juridique / economique ;
- le package contractuel ;
- les points qui facilitent la decision ;
- les limites et risques a ne pas masquer.

### Juridique

Les notes juridiques structurent les blocs de base :

- SPV ring-fenced par actif ou par pool ;
- co-invest opérateur comme châssis standard ;
- conventions de gestion avec Fruits OpCo ;
- waterfall, reserves, DSRA, covenants ;
- usufruit / nue-propriete comme outil spécifique, pas structure par défaut ;
- actions de preference ;
- templates et sujets a faire relire.

### Operationnel

Le bloc operationnel detaille :

- châssis standard Fruits ;
- produits Fruits ;
- strategie groupe ;
- levier financier ;
- assurances ;
- gestion des frais ;
- roadmap ;
- VEFA / travaux dans le neuf ;
- SPV avec actions de preference ;
- refinancement ;
- remuneration Fruits et promote.

### Prospection

La prospection separe :

- les zones geographiques ;
- les canaux d'acces aux financeurs ;
- les plateformes et bases utiles ;
- les strategies par pays et type de financeur.

### Sources GPT historiques

La note `06_Ressources/09_Sources_Historiques_GPT.md` contient la synthèse des conversations GPT importées pour garder la trace de l'origine des idées.

Règles :

- statut `historical_to_review` ou `draft_to_validate` ;
- aucune décision automatique ;
- chaque idée utile doit être transformée dans une note opérationnelle, juridique, investisseur ou stratégie ;
- les points obsolètes doivent rester identifiables au lieu d'être mélangés aux règles validées.

## Regles de prudence validees

- Pas de cash pooling entre SPV.
- Pas de rendement presente comme garanti.
- Pas de salaire personnel finance par dette lombard ou argent investisseur.
- Pas de remboursement d'exploitation courant finance par lombard.
- Pas d'ETF actions dans les reserves de securite d'une SPV.
- Refinancement modelise des l'achat, mais jamais presente comme garanti.
- Fruits se remunere apres charges, dette, reserves et priorites investisseurs.
- Fruits capte des revenus nets d'exploitation, pas des loyers bruts.
- Bridge / portage = outil de vitesse, pas modèle permanent.

## Statut

Le vault est une base de strategie et de structuration. Il reste a completer par :

- modeles financiers par actif type ;
- term sheets relues ;
- data room standard ;
- validation juridique et fiscale ;
- premieres hypotheses bancaires reelles ;
- choix du pays et du premier type d'actif.
