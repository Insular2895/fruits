# Stratégies Empilables Ou Non

## Objectif

Définir quelles stratégies peuvent coexister dans Fruits sans créer une structure fragile.

## Matrice rapide

| Stratégie | Stade 1 | Stade 2 | Stade 3 | Commentaire |
| --- | --- | --- | --- | --- |
| Dette senior immobilière | Oui | Oui | Oui | Base du modèle si LTV prudente |
| Co-invest operateur | Oui | Oui | Oui | Chassis standard Fruits |
| Usufruit / NP | Exception | Oui | Oui | Outil specifique pour FO patrimoniaux, actif stable et fiscalite validee |
| Actions de préférence | Oui | Oui | Oui | Bon complément d'equity, pas une dette garantie |
| Private debt bridge | Oui | Oui | Opportuniste | Pour vitesse / track record, pas long terme |
| Crédit vendeur Balloon / Step | Opportuniste | Oui | Oui | Paiement différé, coût complet et ballon à sécuriser |
| Crédit vendeur Zero | Experimental | Experimental | Oui sous matching | Mur de remboursement intégral |
| Refinancement | Oui | Oui | Oui | Sortie / optimisation après stabilisation, pas hypothèse magique |
| Lombard | Très limité | Limité | Oui | Holding uniquement, LTV basse |
| ETF/collar | Holding seulement | Holding | Holding | Jamais réserve risquée dans SPV financée |
| FX / dette devise | Non | Rare | Oui | Seulement si besoin économique réel |
| BPI / subventions | Opportuniste | Oui | Oui | Si activité éligible, pas immo pur passif |
| Financement vert | Si travaux réels | Oui | Oui | Mesure et preuves obligatoires |
| BTP / acquisitions sociétés | Non | Rare | Oui | Après cash-flow, équipe, audit |
| Santé / cliniques | Non | Test | Oui | Besoin exploitation dédiée |

## Combinaisons recommandées

### Deal 1-3

```text
SPV
+ dette senior 55-65%
+ Fruits 10%
+ ADP/UHNWI/FO 25-35%
+ DSRA
+ capex reserve
```

### Deal FO patrimonial

Version recommandee : co-invest operateur patrimonial.

```text
FO / investisseur apporte le capital patrimonial majoritaire
+ banque apporte un levier prudent
+ Fruits co-investit minoritairement
+ Fruits OpCo exploite / asset manage
+ droit de preference, option ou streaming si possible
+ reporting
```

Lecture :

- Le FO finance l'exposition patrimoniale.
- Fruits porte l'exploitation et capte les revenus nets apres charges, dette et reserves.
- Le FO est prioritaire a l'exit.
- Le reporting rassure le FO : loyers, vacance, impayes, travaux, etat du bien, reserves.

Pourquoi c'est propre :

- le FO a une priorite patrimoniale ;
- Fruits ne promet pas un rendement garanti ;
- la dette reste prudente ;
- le risque operationnel reste chez Fruits ;
- la structure reste plus flexible qu'un demembrement strict.

Exception : usufruit juridique.

```text
FO achete NP
+ Fruits achete UF
+ banque finance UF si possible
+ convention demembrement
+ reporting
```

A utiliser seulement si actif stable, duree longue, FO patrimonial et fiscalite validee.

Variante plus complexe : portage d'usufruit.

```text
FO achète NP
+ FO prête à Fruits pour financer UF
+ Fruits exploite le bien
+ Fruits rembourse le prêt UF au FO
+ FO garde la NP
```

Point économique :

- l'emprunt auprès d'un privé/FO est souvent plus cher qu'une dette bancaire ;
- en échange, il peut être plus flexible : interest-only, différé partiel, remboursement bullet, covenant plus sur-mesure, rachat négocié ;
- cette flexibilité a un prix et doit être absorbée par les loyers ou par la sortie.

À utiliser seulement si :

- la banque ne finance pas l'UF ;
- le FO veut un rendement contractuel pendant la durée ;
- le deal supporte le service de dette supplémentaire ;
- le pacte et les sûretés sont très bien documentés.

### Deal bridge

Le bridge est une stratégie de vitesse.

```text
SPV pleine propriété
+ dette senior bridge
+ vente occupée / refinancement prévu
+ lockbox
+ DSRA 3-6 mois
```

Lecture :

- La SPV achète le bien en pleine propriété.
- Un prêteur bridge finance l'acquisition avec une dette senior courte.
- La durée est courte : souvent 6-36 mois.
- Le prêteur veut surtout une sortie claire : vente occupée, vente libre ou refinancement.
- Les loyers passent dans une lockbox ou un compte contrôlé.
- La DSRA garde 3-6 mois de service de dette en réserve.

Logique économique :

- acheter un bien ;
- le stabiliser, le louer ou l'améliorer ;
- créer un historique d'encaissement ;
- revendre ou refinancer sous 12-36 mois.

Sources de gain possibles :

- plus-value de revente si achat décoté ou travaux créateurs de valeur ;
- hausse de valeur par stabilisation locative : bien loué, rent roll propre, impayés faibles, vacance réduite ;
- refinancement : remplacement d'une dette bridge chère par une dette long terme moins chère une fois l'actif stabilisé.

Attention sur la vente occupée :

- elle peut être attractive pour un investisseur rendement ;
- elle peut être moins attractive pour un acheteur particulier qui veut habiter ;
- il faut donc définir la cible de sortie dès le départ.

Pourquoi c'est différent du deal FO usufruit :

- le FO en usufruit pense long terme et patrimonial ;
- le bridge pense exécution, sûretés et remboursement rapide ;
- le bridge ne veut pas forcément garder l'actif ;
- le bridge veut pouvoir reprendre/vendre/refinancer si problème.

Quand l'utiliser :

- acquisition rapide ;
- opportunité de marché ;
- actif liquide ;
- création de track record ;
- deal avec sortie déjà crédible.

Quand l'éviter :

- actif long terme sans sortie claire ;
- travaux lourds non maîtrisés ;
- locataire/procédure compliquée ;
- refinancement incertain ;
- besoin de capital patient.

### Pool stade 2

Le pool stade 2 est une stratégie de portefeuille.

```text
SPV pool
+ dette senior/private debt
+ preferred equity
+ intercreditor
+ reporting mensuel
+ audit léger
```

Lecture :

- Une SPV ou holding de pool détient plusieurs actifs.
- La dette finance le portefeuille, pas seulement un bien isolé.
- Une couche de preferred equity peut compléter la dette senior.
- S'il y a plusieurs financeurs, l'intercreditor définit qui est prioritaire.
- Le reporting mensuel devient obligatoire : loyers, vacance, DSCR, LTV, réserves, incidents.
- L'audit léger rassure les financeurs sur les chiffres.

Pourquoi c'est différent du bridge :

- le bridge est court, deal-by-deal, orienté sortie rapide ;
- le pool stade 2 est plus long, plus institutionnel, orienté portefeuille ;
- le bridge peut fonctionner avec un seul actif ;
- le pool demande déjà du track record et plusieurs KPI ;
- le pool accepte plus de complexité, mais exige plus de reporting.

Quand l'utiliser :

- Fruits a déjà 5-10M d'actifs ou un vrai pipeline ;
- il existe 12-24 mois de KPI ;
- les process juridiques et reporting sont standardisés ;
- Fruits veut baisser le coût du capital ou augmenter la taille des deals.

Quand l'éviter :

- trop tôt ;
- pas assez d'actifs ;
- pas de reporting mensuel fiable ;
- pas de stratégie de sortie ou refinancement ;
- frais juridiques/audit disproportionnés.

Différence simple :

```text
Bridge = financer vite un actif avec sortie proche.
Pool stade 2 = financer un portefeuille avec gouvernance institutionnelle.
```

### Refinancement

Le refinancement n'est pas une stratégie autonome. C'est une sortie ou une optimisation après création de valeur.

```text
 achat / travaux / stabilisation
+ rent roll propre
+ nouvelle valeur prudente
+ dette long terme
+ remboursement ancienne dette
+ cash-out limité si DSCR OK
```

Ce que le refinancement peut faire :

- remplacer une dette bridge par dette longue ;
- rembourser un crédit vendeur ;
- réduire le coût de dette ;
- racheter partiellement des ADP ;
- financer une partie du prochain deal.

Ce qu'il ne doit pas faire :

- sauver un actif qui ne cash-flow pas ;
- financer un salaire ou une distribution ;
- racheter un investisseur si le DSCR devient fragile ;
- être présenté comme garantie de sortie.

Règle Fruits :

```text
 refinancement = option de sortie
 pas promesse de remboursement
```

## Combinaisons dangereuses

### Trop de levier sur un premier actif

```text
senior 70%
+ ADP 25%
+ Fruits 5%
+ lombard personnel
```

Risque : aucun vrai coussin sponsor, pression sur cash-flow, rachat investisseur difficile.

### Mismatch de duration

```text
dette 18 mois
+ actif long terme
+ pas de vente/refi signé
```

Risque : refinancement forcé.

### Ballons vendeur concentrés

```text
plusieurs dettes vendeur
+ mêmes années d'échéance
+ Protection insuffisante
+ refinancement supposé
```

Risque : mur de maturité groupe malgré des actifs rentables.

Voir : [Vente à terme / crédit vendeur — système Fruits](../04_Operationnel/12_Vente_A_Terme_Credit_Vendeur_Fruits.md).

### Mismatch de liquidité

```text
ETF volatile
+ lombard
+ besoin de cash fixe
```

Risque : margin call au pire moment.

### Mismatch de devise

```text
dette USD/CHF
+ loyers EUR
+ pas de couverture
```

Risque : gain de taux détruit par le change.

## Règle de décision

Une stratégie peut être empilée seulement si elle améliore au moins un point sans en dégrader deux autres :

- coût du capital ;
- durée du capital ;
- contrôle Fruits ;
- sécurité investisseur ;
- simplicité juridique ;
- liquidité de sortie ;
- résilience en stress.

## Phrase à retenir

Fruits doit empiler des protections avant d'empiler du levier.
