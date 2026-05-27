---
type: strategic_consolidation
status: draft_to_validate
created: 2026-05-27
tags: [#Fruits, #strategy, #real-estate, #btp, #investor-ready, #draft_to_validate]
---

# Consolidation stratégique Fruits - idées à intégrer sans changer la structure

## Rôle

Cette note retravaille les idées disponibles dans le vault Fruits, la note de filtrage playlists/livres et la piste récente sur crédits carbone / biodiversité.

Elle ne modifie pas la structure des sociétés. Les décisions de structure déjà validées restent inchangées :

- SPV isolée par actif ou par pool ;
- pas de cash pooling ;
- OpCo pour les fees et la rémunération ;
- dette senior prudente ;
- ADP / preferred equity avec rendement prioritaire cible, jamais garanti ;
- réserves, DSRA et reporting mensuel avant distribution ;
- waterfall et promote après priorités investisseurs.

## Limite importante - conversations GPT

Le lien ChatGPT fourni renvoie vers une page de connexion et n'est pas lisible depuis l'environnement Codex :

```text
https://chatgpt.com/g/g-p-6837729de6bc819186f035b0cc47463f-fruits/project
```

Conséquence :

- les conversations GPT non exportées ne sont pas encore analysées ;
- cette consolidation utilise uniquement le vault Fruits local, les notes déjà synchronisées et les sources locales/externes déjà consultées ;
- pour refaire une passe complète conversation par conversation, il faut exporter les conversations ou copier les transcripts dans `projects/fruits/raw/ideas/` ou `inbox/to_process/`.

## Verdict court

Fruits est déjà cohérent sur la structure financière. Ce qui manque surtout n'est pas une nouvelle structure société, mais une couche d'exécution :

- grille d'underwriting actif ;
- data room type ;
- modèles financiers vierges par produit ;
- reporting mensuel standard ;
- workflow travaux / draw requests ;
- checklist DPE / ESG / biodiversité ;
- covenants et cash trap codifiés ;
- pack prospection investisseur plus concret ;
- registre des hypothèses par deal.

La bonne direction est donc :

```text
moins d'idées nouvelles
+ plus de preuves, checklists, templates et contrôles
```

## Ce qui est déjà solide

### Socle financier

- Dette senior prudente avec LTV cible 55-65% au stade 1.
- DSCR normal cible > 1,30x.
- DSCR stress minimum > 1,20x.
- DSRA 3-6 mois.
- Réserve capex/vacance séparée.
- Cash trap si réserves ou covenants ne sont pas respectés.
- Refinancement prévu comme option, jamais comme garantie.

### Socle investisseur

- Family Offices en priorité stade 1 via NP/UF patrimonial.
- UHNWI / ADP pour preferred equity et promote encadré.
- Private debt bridge / asset-based comme outil de vitesse, pas de détention longue.
- Foncières, SCPI, OPCI, SIIC plutôt comme partenaires ou sorties après stabilisation.
- Banque des Territoires / CDC uniquement si impact territorial réel.

### Socle juridique / gouvernance

- SPV ring-fenced.
- Comptes dédiés.
- No commingling.
- Fees Fruits OpCo plafonnés, transparents et suspendables si besoin.
- Waterfall claire.
- Pacte, statuts, conventions et term sheets à faire relire.

## Concepts à intégrer proprement

### 1. Underwriting actif

Ajouter une grille standard avant toute offre.

Critères à intégrer :

- prix / m2 vs comparables ;
- loyer actuel vs loyer de marché ;
- NOI actuel ;
- NOI stabilisé ;
- cap rate d'achat ;
- cap rate stabilisé ;
- DSCR normal et stress ;
- LTV achat et LTV post-stress ;
- vacance historique ;
- travaux immédiats ;
- capex 3 ans ;
- DPE actuel / cible ;
- scénario vente ;
- scénario refinancement ;
- scénario "pas de refinancement".

Idées issues des sources :

- ne pas raisonner "immobilier" globalement : segmenter par ville, usage, qualité, demande et offre ;
- privilégier les actifs avec demande structurelle et offre limitée ;
- ne pas compter sur l'expansion des multiples ;
- exiger un rendement d'entrée solide ;
- vérifier la croissance de cash-flow possible avant de promettre une création de valeur.

Statut : `immediate_useful`.

### 2. BTP / travaux

Le vault parle déjà de VEFA et travaux, mais il manque un workflow de décaissement.

À ajouter :

- budget travaux par lots ;
- devis signés ;
- responsable travaux ;
- planning ;
- contingence ;
- réserve intérêts si revenus différés ;
- statut permis / autorisations ;
- photos avant/après ;
- inspection avant décaissement ;
- draw request signé ;
- facture + preuve paiement ;
- suivi budget réel vs budget prévu.

Principe :

```text
pas de décaissement travaux sans preuve d'avancement
```

Statut : `immediate_useful`.

### 3. DPE / ESG / biodiversité

La piste "crédits liés à la déforestation / impact construction" doit être cadrée.

Trois mécanismes distincts :

1. Défrichement : plutôt coût et obligation de compensation, pas revenu.
2. Label bas-carbone : revenu ou contribution carbone possible si projet éligible.
3. SNCRR / crédits biodiversité : outil de compensation ou contribution volontaire sur restauration/renaturation.

Usage Fruits :

- inclure DPE, coût de remise à niveau et calendrier dans chaque underwriting ;
- utiliser financement vert seulement si gains mesurables : audit, devis, DPE avant/après, reporting énergie/carbone ;
- traiter crédits carbone / biodiversité comme upside optionnel ;
- ne jamais intégrer ces revenus au cash-flow de base ;
- vérifier l'éligibilité avec bureau d'études environnemental, avocat urbanisme/environnement et DREAL/DDT(M).

Statut : `to_validate`.

Sources externes utiles :

- Label bas-carbone : `https://label-bas-carbone.ecologie.gouv.fr/quest-ce-que-le-label-bas-carbone`
- SNCRR : `https://www.ecologie.gouv.fr/politiques-publiques/sites-naturels-compensation-restauration-renaturation`
- Code forestier L341-6 : `https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053564515`

### 4. Reporting mensuel SPV

Le reporting est déjà une obligation dans Fruits, mais le template doit devenir concret.

Template minimum :

- synthèse 1 page ;
- cash opening / cash closing ;
- loyers facturés ;
- loyers encaissés ;
- impayés ;
- vacance ;
- charges ;
- dette payée ;
- DSRA ;
- réserve capex/vacance ;
- travaux engagés ;
- incidents ;
- covenants : LTV, DSCR, ICR si applicable ;
- décisions à prendre ;
- photos / documents nouveaux ;
- statut de sortie : vente, refi, hold.

Statut : `immediate_useful`.

### 5. Covenants / cash trap

Le vault contient déjà les seuils, mais il faut les transformer en clauses opérationnelles.

Proposition de grille à valider :

| Indicateur | Vert | Surveillance | Cash trap |
| --- | ---: | ---: | ---: |
| DSCR | > 1,30x | 1,20x-1,30x | < 1,20x |
| DSRA | 3-6 mois pleine | baisse temporaire | non reconstituée |
| LTV | 55-65% | 65-70% | > 70% ou breach banque |
| Vacance | conforme modèle | +10-20% vs modèle | dérive durable |
| Capex | dans budget | dépassement modéré | dépassement non financé |

Effet cash trap :

- pas de distribution Fruits ;
- fees variables suspendus si prévu ;
- reconstitution réserves prioritaire ;
- plan d'action présenté investisseur / prêteur.

Statut : `to_validate`.

### 6. Data room type

Créer une data room vide, prête à remplir deal par deal.

Arborescence proposée :

```text
01_Corporate/
02_Asset/
03_Legal/
04_Finance/
05_Debt/
06_Tenants_Leases/
07_Works_BTP/
08_Insurance/
09_ESG_DPE/
10_Reporting/
11_Risks/
12_Exit_Refinancing/
```

Règle :

- aucun chiffre inventé ;
- chaque document doit avoir une date, une source et un statut ;
- les hypothèses doivent être séparées des pièces justificatives.

Statut : `immediate_useful`.

### 7. Prospection financeurs

La carte financeurs est complète, mais l'exécution commerciale doit être plus simple.

Priorité :

1. FO / UHNWI patrimonial : actif simple, NP/UF ou ADP.
2. Bridge / asset-based : actif liquide avec sortie courte.
3. Foncière privée : si elle veut acheter/stabiliser un portefeuille.
4. Banque privée : soutien sponsor ou dette prudente.
5. Banque des Territoires / CDC : uniquement impact réel.

À préparer :

- one-pager Fruits ;
- one-pager actif ;
- memo investisseur 5-10 pages ;
- data room ;
- modèle financier ;
- reporting sample ;
- term sheet draft relue ;
- liste questions/réponses.

Statut : `immediate_useful`.

## Manques par bloc du vault

### Stratégie

Manque :

- une "investment policy" Fruits en 1 page ;
- les critères d'exclusion d'actifs ;
- la règle de passage d'un produit à l'autre ;
- la limite de complexité par stade.

Proposition :

```text
Stade 1 = actif simple + structure simple + financeur simple.
Stade 2 = pool + reporting + private debt structuré.
Stade 3 = institutionnels + ESG + audit + plateforme.
```

### Investisseurs

Manque :

- un pitch court par financeur ;
- une matrice objections / réponses ;
- un ordre de prospection par pays ;
- les prérequis avant contact sérieux.

### Juridique

Manque :

- liste des clauses rouges à ne jamais promettre ;
- checklist AMF / offre au public / placement privé ;
- checklist fiscalité par produit ;
- checklist sûretés françaises par type de dette.

### Opérationnel

Manque :

- workflow acquisition ;
- workflow travaux ;
- workflow reporting ;
- workflow incident / cash trap ;
- workflow refinancement 6-9 mois avant maturité ;
- registre des hypothèses.

### Prospection

Manque :

- CRM minimal ;
- scoring financeur ;
- séquence d'approche ;
- modèles d'emails ;
- tracker des objections.

### Ressources

Manque :

- lexique Fruits ;
- index des sources longues ;
- statut de chaque source : `validated_source`, `to_review`, `draft_to_validate`, `discard_after_extraction`.

## Backlog priorisé

### 30 jours

1. Créer le modèle financier vierge par actif type.
2. Créer la data room type.
3. Créer le reporting mensuel SPV.
4. Créer checklist underwriting actif.
5. Créer checklist DPE / travaux / risques locatifs.
6. Choisir le premier actif type pour simulation.

### 60 jours

1. Préparer term sheets draft : NP/UF, ADP, bridge, crédit vendeur.
2. Préparer one-pager investisseur.
3. Préparer memo actif 5-10 pages.
4. Construire CRM financeurs cible.
5. Faire relire les clauses clés par avocat/notaire/fiscaliste.

### 90 jours

1. Tester un actif réel.
2. Remplir modèle avec chiffres réels.
3. Constituer data room complète.
4. Obtenir retours banque / FO / UHNWI.
5. Ajuster les seuils de fees, covenants et co-invest.

## Fiches réflexes / templates à créer

- `checklist_underwriting_actif_fruits`
- `template_data_room_fruits`
- `template_reporting_mensuel_spv`
- `workflow_draw_request_travaux`
- `checklist_dpe_esg_biodiversite`
- `checklist_refinancement_6_9_mois`
- `checklist_cash_trap`
- `template_one_pager_investisseur`
- `template_memo_actif`
- `lexique_fruits_capital_stack_waterfall`
- `registre_hypotheses_deal`

## Points à valider avec experts

- ADP : statut, droits financiers, rachat prévu, fiscalité, risque de dette déguisée.
- NP/UF : convention de démembrement, grosses réparations, assurances, fiscalité, valorisation économique vs barème fiscal.
- Offre investisseur : AMF, placement privé, crowdfunding/PSFP, documentation obligatoire.
- Dette : sûretés, recours, hypothèque, nantissements, covenants.
- Fiscalité : IS/IR, TVA, plus-values, amortissement, flux OpCo/SPV/Holding.
- DPE / travaux : interdictions de location, calendrier, coût réel, aides.
- Biodiversité / carbone : éligibilité Label bas-carbone, SNCRR, compensation défrichement, preuves et audits.

## Ce qu'il ne faut pas faire

- Changer la structure sociétés déjà validée.
- Ajouter une nouvelle couche de levier au stade 1.
- Vendre le refinancement comme garantie.
- Présenter crédits carbone/biodiversité comme cash-flow sûr.
- Démarcher institutionnels avant d'avoir modèle, data room et reporting.
- Remplir des modèles avec de faux chiffres non sourcés.
- Confondre source, hypothèse, idée et décision.

## Statut proposé

```text
status: draft_to_validate
```

Cette consolidation peut servir de base pour créer les fiches réflexes et templates, mais elle ne vaut pas décision d'exécution.
