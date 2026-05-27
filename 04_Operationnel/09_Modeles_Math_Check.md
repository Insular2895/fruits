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
