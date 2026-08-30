# Math Check - Modèles Fruits

## Objectif

Vérifier rapidement si une structure tient debout avant de la présenter à un investisseur.

## 1. Exemple ADP sur bien à 500k

Structure prudente :

| Source | Montant | % actif |
| --- | ---: | ---: |
| Banque senior | 300 000 EUR | 60% |
| ADP investisseurs | 150 000 EUR | 30% |
| Fruits | 50 000 EUR | 10% |
| Total | 500 000 EUR | 100% |

Rendement prioritaire cible ADP :

```text
150 000 x 8% = 12 000 EUR / an
```

Si cash disponible après charges et banque = 25 000 EUR :

```text
Couverture ADP = 25 000 / 12 000 = 2,08x
Surplus Fruits = 13 000 EUR
```

Si cash disponible baisse de 40% :

```text
Cash stress = 15 000 EUR
Couverture ADP = 15 000 / 12 000 = 1,25x
Surplus Fruits = 3 000 EUR
```

Conclusion : viable si réserves pleines, vacance maîtrisée et dette senior pas trop haute.

## 2. Exemple ADP agressif à éviter au stade 1

| Source | Montant | % actif |
| --- | ---: | ---: |
| Banque senior | 350 000 EUR | 70% |
| ADP investisseurs | 120 000 EUR | 24% |
| Fruits | 30 000 EUR | 6% |

Problème :

- la banque est déjà à 70% LTV ;
- Fruits a peu de vrai coussin ;
- si valeur baisse de 15%, LTV banque = 350 / 425 = 82,4% ;
- rachat ADP dépend fortement du refinancement.

Conclusion : utile comme exemple pédagogique, trop agressif pour un premier deal.

## 3. Lombard

Si portefeuille = 1 000 000 EUR.

| Dette lombard | LTV initiale | LTV après -40% marché |
| ---: | ---: | ---: |
| 200 000 | 20% | 33% |
| 300 000 | 30% | 50% |
| 400 000 | 40% | 67% |
| 500 000 | 50% | 83% |

Conclusion : 40-50% LTV est trop agressif sur ETF actions. Fruits doit rester à 20-30%.

## 4. VEFA / intérêts intercalaires

Hypothèses :

- prêt : 250 000 EUR ;
- taux : 3,40% ;
- chantier : 18 mois ;
- appels de fonds simplifiés : 35%, 70%, 95%.

Calcul :

```text
M0-M6 : 87 500 x 3,40% x 6/12 = 1 487,50 EUR
M6-M12 : 175 000 x 3,40% x 6/12 = 2 975 EUR
M12-M18 : 237 500 x 3,40% x 6/12 = 4 037,50 EUR
Total = 8 500 EUR hors assurance
```

Conclusion : le calcul est cohérent, mais le calendrier réel dépend du contrat VEFA et des appels de fonds.

### Comparaison du différé — hypothèse post-livraison 20 ans à 3,40 %

```text
Option A — intérêts intercalaires payés :
cash avant livraison = 8 500 EUR hors assurance
capital amorti après livraison = 250 000 EUR
mensualité = 1 437,09 EUR hors assurance
intérêts post-livraison = 94 900,59 EUR
coût total hors assurance = 103 400,59 EUR

Option B — capitalisation simplifiée des 8 500 EUR :
cash d'intérêts avant livraison = 0 EUR hors assurance
capital amorti après livraison = 258 500 EUR
mensualité = 1 485,95 EUR hors assurance
intérêts post-livraison = 98 127,21 EUR
coût total rapporté aux 250 000 EUR initiaux = 106 627,21 EUR
```

L'option B préserve 8 500 EUR avant livraison, mais ajoute 8 500 EUR au solde, 48,86 EUR à la mensualité et 3 226,62 EUR au coût total dans cette simplification. Une capitalisation périodique peut ajouter davantage d'intérêts sur intérêts. L'assurance restait au moins payée dans le montage décrit lors de l'échange SG du 20 août 2026 ; seule l'offre fixe le traitement exact.

## 5. DSCR

Formule :

```text
DSCR = NOI / service annuel de dette
```

Seuils Fruits :

- > 1,30x : confortable ;
- 1,20x-1,30x : acceptable mais surveillé ;
- < 1,20x : pas de distribution Fruits, cash trap ;
- < 1,00x : shortfall, activation DSRA.

## 6. Règle avant pitch investisseur

Chaque deal doit afficher :

- LTV senior ;
- DSCR normal ;
- DSCR stress ;
- rendement prioritaire cible ;
- couverture du rendement prioritaire ;
- DSRA ;
- réserve capex/vacance ;
- scénario de sortie ;
- scénario où Fruits ne peut pas racheter à la date cible.

## 7. Refinancement

Formule :

```text
 dette max refinance = valeur prudente x LTV cible
 cash-out net = nouvelle dette - dette existante - frais - réserves à reconstituer
```

Exemple :

```text
 coût initial actif = 500 000 EUR
dette existante = 300 000 EUR
valeur après stabilisation = 620 000 EUR
LTV refinance = 60%
nouvelle dette = 372 000 EUR
cash brut = 372 000 - 300 000 = 72 000 EUR
frais/réserves = 15 000 EUR
cash-out net = 57 000 EUR
```

Conclusion :

- le refinancement libère seulement 57k dans cet exemple ;
- il ne rembourse pas 150k d'ADP ;
- il faut vérifier le DSCR après la nouvelle dette.

Valeur nécessaire pour racheter 150k d'ADP par dette seule :

```text
 dette existante : 300 000 EUR
ADP à racheter : 150 000 EUR
frais/réserves : 15 000 EUR
nouvelle dette nécessaire : 465 000 EUR

valeur requise à 60% LTV = 775 000 EUR
valeur requise à 65% LTV = 715 385 EUR
```

Conclusion : le rachat complet des ADP par refinancement exige une vraie création de valeur. Il ne faut pas le promettre.

## 8. Waterfall de vente / promote

Exemple :

```text
Prix de vente : 620 000 EUR
Dette restante : -280 000 EUR
Frais / fiscalité : -30 000 EUR
Capital ADP : -150 000 EUR
Rendement prioritaire dû : -10 000 EUR
Surplus avant promote : 150 000 EUR
```

Split prudent stade 1 :

```text
80% investisseur / 20% Fruits
Investisseur : 120 000 EUR
Fruits : 30 000 EUR
```

Split plus ambitieux :

```text
70% investisseur / 30% Fruits
Investisseur : 105 000 EUR
Fruits : 45 000 EUR
```

Split très favorable Fruits :

```text
30% investisseur / 70% Fruits
Investisseur : 45 000 EUR
Fruits : 105 000 EUR
```

Conclusion :

- 70/30 en faveur investisseur est crédible au début ;
- 70/30 en faveur Fruits est agressif ;
- pour l'obtenir, l'investisseur doit déjà avoir reçu capital + priorité + protection forte, ou être plafonné dans son rendement.

## 9. Vente à terme / crédit vendeur

Source et hypothèses complètes : [Vente à terme / crédit vendeur — système Fruits](12_Vente_A_Terme_Credit_Vendeur_Fruits.md).

### Sources et emplois

```text
cash initial Fruits =
bouquet
+ frais d'acquisition
+ travaux
+ réserves initiales
- financements externes effectivement obtenus
```

Cas standard :

```text
500 k€ d'actif
- 400 k€ de dette vendeur
= 100 k€ d'equity hors frais

100 k€ de bouquet + 40 k€ de frais
= 140 k€ de cash initial avant travaux et réserves
```

### Échéancier

```text
intérêt_t = solde_début_t × taux_période
principal_t = max(0, paiement_t - intérêt_t)
solde_fin_t = solde_début_t + intérêt_t - paiement_t

ballon à mensualité constante =
P(1+r)^n - M × ((1+r)^n - 1) / r
```

Résultats recalculés sur 400 k€, 1,5 %, 120 mois :

| Produit | Paiements courants | Ballon | Intérêts totaux |
| --- | ---: | ---: | ---: |
| Zero, 500 €/mois | 60 000 € | 400 000 € | 60 000 € |
| Balloon, 1 500 €/mois | 180 000 € | 270 620 € | 50 620 € |
| Step, 500 / 1 000 / 2 000 €/mois | 150 000 € | 306 307 € | 56 307 € |

### Couverture et spread

```text
LTV totale = toutes dettes financières / valeur prudente
DSCR = NOI / service annuel de dette

valeur collatérale ajustée =
cash + somme(valeur de marché × (1 - haircut))

couverture vendeur =
valeur collatérale ajustée / dette vendeur

coverage ratio in fine =
valeur de marché du portefeuille / capital à couvrir

coverage shortfall =
max(0, couverture contractuelle minimale - valeur de couverture reconnue)

spread net =
rendement net du capital conservé
- coût complet annualisé du crédit vendeur
```

Le coût complet inclut intérêts, surprix, sûretés, assurance/garantie, bonus, frais et capital immobilisé.

### Poche de remboursement in fine — retour SG et hypothèses Fruits

```text
capital initial nanti
+ versements périodiques
+ rendement net réellement constaté
= capital attendu
```

**Information confirmée par la conseillère SG :** exemple de 250 k€ sur environ quinze ans, 20 % initiaux soit 50 k€, puis versements réguliers ; une couverture proche de 100 % sur support sûr ou 130 % sur une poche plus risquée a été évoquée. **Hypothèse Fruits :** rendement net régulier de 3 % utilisé ci-dessous. Les ratios 20 % et 130 % ne sont pas des règles universelles.

| Couverture | Capital cible | Mensuel à 3 % net | Mensuel à 0 % | Écart de cible vs 100 % |
| ---: | ---: | ---: | ---: | ---: |
| 100 % | 250 000 € | 756,16 € | 1 111,11 € | 0 € |
| 110 % | 275 000 € | 866,31 € | 1 250,00 € | 25 000 € |
| 120 % | 300 000 € | 976,45 € | 1 388,89 € | 50 000 € |
| 130 % | 325 000 € | 1 086,60 € | 1 527,78 € | 75 000 € |

La cible de 325 k€ n'est pas nécessairement présente au jour 1. Elle désigne ici la valeur finale recherchée lorsque le ratio de 130 % s'applique. Sous-performance, haircuts, calendrier des tests et remède contractuel restent à confirmer ; ne pas appeler automatiquement le déficit « appel de marge ».

### Vente et refinancement

```text
cash net de vente =
prix encaissé
- dette vendeur remboursée
- autres dettes
- frais de vente
- fiscalité

dette refinance maximale =
minimum(
  valeur prudente × LTV autorisée,
  dette supportable au DSCR,
  limite prêteur
)
```

La dette vendeur maintenue après revente reste une dette : le portefeuille nanti n'est pas du cash libre.

### Stress tests obligatoires

- taux vendeur : 0 %, 1 %, 1,5 %, 2 %, 3 %, 4 % ;
- durée : 5, 7, 10, 15 ans ; 20 ans uniquement en scénario expérimental ;
- NOI : 24 k€ et 30 k€ annuels ;
- valeur immobilière : -10 %, -20 % ;
- Growth : -30 %, -50 % ;
- revente : 3, 6, 12, 36, 60 mois ou aucune ;
- refinancement : taux +200 bps ou impossible 24 mois ;
- portabilité refusée ;
- couverture vendeur : 100 %, 110 %, 120 %, 130 % ;
- rémunération : 0, Growth First, équilibrée, confort.

### Garde-fous

- DSCR normal > 1,30x ;
- DSCR stress > 1,20x ;
- DSRA et réserves pleines ;
- aucun double comptage de l'equity, des intérêts, du portefeuille nanti ou de la rémunération ;
- aucun scénario GO si le seul remboursement du ballon est un refinancement non engagé.

## 10. Capital preservation + acquisition leverage

Source canonique : [section 6 bis du modèle crédit vendeur](12_Vente_A_Terme_Credit_Vendeur_Fruits.md#6-bis-capital-preservation--acquisition-leverage). Calcul reproductible : [notebook Deal 1 → Deal 5](modeles/01_Capital_Preservation_Multi_Deals.ipynb).

### Sources & uses du bouquet

```text
equity Fruits + dette banque + dette vendeur = prix d'acquisition
```

Exemple Deal 2 :

```text
20 k€ equity Fruits
+ 60 k€ dette banque
+ 420 k€ dette vendeur
= 500 k€
```

La dette banque n'est ni « apport » ni equity.

### Capital libre et borrowing base

```text
capital libre réel =
actifs liquides non grevés
- réserves obligatoires
- fiscalité exigible
- DSRA

borrowing base disponible =
max(0,
  somme[valeur de marché_i × (1 - haircut_i)]
  - expositions garanties de rang supérieur
)

capacité banque = minimum(
  engagement approuvé,
  capacité DSCR,
  capacité LTV,
  borrowing base disponible
)
```

Ne pas soustraire deux fois un même actif et ne pas additionner le collatéral à l'emprunt qu'il garantit. Si 400 k€ de portefeuille sont déjà affectés à 400 k€ de dette vendeur, le capital libre peut être nul malgré 400 k€ de liquidité comptable.

### Capacité d'acquisition

```text
Next Deal Capital =
cash libre + equity externe confirmée + dette bouquet confirmée

Acquisition Capacity =
Next Deal Capital + crédit vendeur signé
```

Ces KPI sont des capacités contractuelles, pas une mesure de richesse.

### Levier et solvabilité consolidés

```text
Total Group Leverage = dette financière totale / actifs bruts ajustés
NAV = actifs prudents - passifs et provisions
Net Debt / NAV = (dette totale - liquidités non grevées mobilisables) / NAV
Debt / Equity = dette totale / NAV ajustée
```

Si `NAV ≤ 0`, les deux derniers ratios sont non significatifs et le modèle déclenche un STOP. Calculer à chaque niveau : deal, SPV, holding et groupe.

### Spread net du capital conservé

```text
spread net après coûts =
rendement du capital conservé après frais et impôt
- intérêt bancaire
- assurance et frais annualisés
- garantie / nantissement
- hedge éventuel
- pertes attendues et coût de liquidité
```

À 60 k€, 5 % de rendement et 4 % de banque, le spread avant coûts n'est que 600 €/an. À 0 % de rendement, la stratégie perd 2 400 €/an avant frais supplémentaires.

### Contrôles automatiques minimum

- sources = uses pour chaque deal ;
- aucune poche utilisée deux fois ;
- total dettes = banque + vendeurs + private debt + autres dettes ;
- échéanciers et ballons rapprochés des poches dédiées ;
- stress taux +100/+200/+400 bps ;
- in fine refusé et dette amortissable recalculée ;
- loyers -20 %, vacance 6/12 mois, travaux +20 % ;
- immobilier -10/-20 %, portefeuille 0 % et -20/-30/-50 % selon poche ;
- haircut augmenté, second rang et portabilité refusés ;
- refinancement impossible deux puis cinq ans.
