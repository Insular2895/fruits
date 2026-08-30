# Levier Financier

## Objectif

Identifier les leviers qui peuvent améliorer le rendement ou réduire le coût du capital sans rendre Fruits fragile.

## Hiérarchie des leviers

### Leviers solides

- Dette senior immobilière avec LTV prudente.
- Actions de préférence / preferred equity avec rendement prioritaire cible.
- Usufruit / nue-propriété bien documenté.
- Réserves cash et DSRA.
- Refinancement après stabilisation : baisse du coût de dette, sortie bridge, rachat partiel investisseur ou cash-out prudent.
- Placement monétaire très court terme des provisions de charges, uniquement comme optimisation de trésorerie.
- Subventions ou prêts bonifiés quand le projet est réellement éligible.

L'univers admissible, la distinction Fortress/Protection+/Growth et le calcul du rendement net sont centralisés dans [Univers d’investissement et allocation de capital Fruits](../01_Strategie/07_Univers_Investissement_Fruits.md).

### Leviers utiles mais à cadrer

- Crédit vendeur / vente à terme : Balloon ou Step sous conditions ; Zero expérimental.
- Crédit lombard : uniquement holding, LTV basse, jamais pour financer pertes opérationnelles.
- Financement vert / ESG : seulement si travaux mesurables et justificatifs.
- Quotas carbone / certificats : à traiter comme bonus potentiel, jamais comme base du business plan.
- Incubateur / association : possible pour innovation, formation, partenariats, mais ne doit pas servir à maquiller des flux commerciaux.

### Leviers à éviter au départ

- Dette courte pour financer actif long terme.
- Dette en devise non couverte.
- Cash pooling entre SPV.
- Utilisation des provisions locataires comme capital de risque.
- ETF actions dans les réserves d'un SPV financé.
- Promesse de rendement garanti à des investisseurs privés.
- Empilement senior + mezz + ADP + lombard sur le même actif au stade 1.

## Empilement prudent par stade

### Stade 1

Structure recommandée :

- dette senior 55-65% ;
- equity investisseur ou ADP 20-30% ;
- Fruits 5-15% ;
- DSRA 3-6 mois ;
- capex/vacance séparé.

Interdit en stade 1 :

- senior 70% + mezz + ADP + lombard ;
- plusieurs financeurs avec intercreditor complexe ;
- promesse de rachat obligatoire non financée.

### Stade 2

Possible :

- pool de 5-10M ;
- dette senior ou private debt structurée ;
- ADP / preferred equity ;
- reporting mensuel ;
- audit léger ;
- intercreditor si plusieurs couches.

### Stade 3

Possible :

- institutionnels ;
- assureurs ;
- fonds core/core+ ;
- dette longue ;
- JV plateforme ;
- financement vert documenté.

## Règle de solvabilité

Une stratégie est viable seulement si elle passe ces tests :

- DSCR > 1,20x en scénario bas.
- LTV post-stress acceptable pour la banque.
- Capex + vacance financés sans lever en urgence.
- Sortie possible sans vendre au pire moment.
- Le rendement investisseur est payable sans vider les réserves.

Chaque principal doit en outre avoir une source de remboursement identifiable — cash-flow, amortissement, poche réservée, vente prudente ou cash non grevé. Un refinancement futur non engagé ne peut jamais être l’unique moyen d’éviter le défaut.

Une hypothèque, un nantissement ou une caution conforte le dossier du prêteur ; aucune garantie ne remplace la capacité de remboursement démontrée par les revenus, les réserves et les scénarios de stress.

## Capital preservation et levier consolidé

Financer une partie d’un bouquet par banque, in fine ou dette privée peut conserver la liquidité brute, mais ne crée pas d’equity au closing : chaque euro préservé est compensé par un euro de passif supplémentaire.

Pour l'in fine décrit lors de l'échange SG du 20 août 2026, l'absence d'amortissement immobilier n'implique pas un capital entièrement libre : une poche financière initiale puis des versements périodiques peuvent être exigés, avec nantissement et ratio de couverture. Ces flux et actifs immobilisés doivent être inclus dans l'analyse économique.

```text
Total Group Leverage =
(banques + vendeurs + private debt + autres dettes)
/ actifs bruts ajustés

Net Debt / NAV =
(dette totale - cash non grevé - titres liquides non grevés mobilisables)
/ NAV
```

Le seuil 55–65 % reste la cible de **dette senior** au stade 1 ; il ne remplace pas la mesure de toutes les dettes. Les cas Deal 2 à 420 k€ vendeur plus 0–75 k€ banque affichent 84–99 % de dette totale avant frais. Ils sont high-leverage même si la tranche bancaire seule paraît faible.

Règles :

- calculer deal, SPV, holding et groupe consolidé ;
- séparer equity Fruits, dette banque et dette vendeur dans les sources & uses ;
- ne jamais ajouter le collatéral à la fois au capital libre et à la capacité de crédit ;
- traiter `NAV ≤ 0` ou un stress -20 % qui efface l’equity comme STOP ;
- exiger release, substitution, collatéral distinct ou intercreditor avant de réutiliser un portefeuille déjà nanti.

Cadre complet et simulation : [Capital preservation + acquisition leverage](12_Vente_A_Terme_Credit_Vendeur_Fruits.md#6-bis-capital-preservation--acquisition-leverage).

## Sources de levier à travailler

### Provisions de charges

À utiliser uniquement comme optimisation de cash management :

- compte dédié par SPV ;
- liquidité quotidienne ou maturité très courte ;
- monétaire EUR / T-Bills hedgé EUR ;
- aucune prise de risque actions, crédit long ou devise ;
- suivi précis pour régularisation locataire.

Ce n'est pas une source de rendement stratégique. C'est une manière de ne pas laisser dormir un cash de passage.

### Subventions et financements publics

À viser seulement si le projet est éligible :

- rénovation énergétique ;
- immobilier d'exploitation ;
- santé / cabinets médicaux ;
- innovation / data / optimisation BTP ;
- formation ou programme associatif réel.

### Financement vert

À documenter avec :

- audit énergétique ;
- devis travaux ;
- gains mesurables ;
- DPE avant/après ;
- reporting carbone/énergie.

### Quotas / carbone

À traiter comme upside optionnel :

- vérifier éligibilité exacte ;
- vérifier coût de certification ;
- ne pas l'intégrer comme cash-flow de base ;
- ne pas promettre ce revenu à un investisseur.

### Refinancement

À utiliser après stabilisation, pas comme hypothèse de départ fragile.

Usages acceptables :

- remplacer une dette bridge chère par dette bancaire long terme ;
- rembourser un crédit vendeur ;
- racheter partiellement des ADP si la valeur et le DSCR le permettent ;
- baisser la mensualité ou allonger la maturité ;
- libérer un cash-out prudent pour financer un nouveau deal.

Conditions minimales :

- DSCR normal > 1,30x après refinancement ;
- DSCR stress > 1,20x ;
- LTV senior 55-65% ;
- frais, pénalités et nouvelles sûretés inclus ;
- réserves reconstituées avant distribution.

Voir : [Refinancement](10_Refinancement.md).

### Crédit vendeur / vente à terme

Le crédit vendeur diffère le paiement du prix ; il ne remet pas du cash à Fruits.

Usages :

- remplacer une partie de l'equity ou de la dette bancaire ;
- adapter bouquet, durée et paiement au besoin réel du vendeur ;
- financer un actif qui reste viable en exploitation ou à la vente ;
- conserver une option de refinancement, sans en dépendre.

Règles de prudence :

- distinguer LTV bancaire, LTV vendeur et LTV totale ;
- inclure bouquet, frais, travaux et réserves dans les sources et emplois ;
- calculer le coût complet, y compris surprix, sûretés et bonus ;
- ne pas empiler une dette bancaire sur le bouquet sans accord de rang et stress DSCR ;
- traiter le financement bancaire du bouquet comme une hypothèse à tester : l'échange SG du 20 août 2026 n'a apporté aucune validation formelle du produit, du montant ou du rang ;
- ne jamais compter le solde vendeur comme cash ;
- maintenir DSRA, fiscalité et CAPEX hors du portefeuille Growth ;
- considérer toute portabilité après revente comme expérimentale.

La dette ne peut rester après la revente que si le vendeur l'accepte et si l'hypothèque est maintenue, purgée ou remplacée par une sûreté documentée. Le compte-titres nanti ne rend pas automatiquement ses arbitrages, coupons ou dividendes disponibles.

La portabilité avancée n'a pas été validée par la conseillère SG et reste à confirmer avec notaire, avocat, fiscaliste, vendeur et prêteurs. Selon le contrat, un prêt amortissable évolutif peut offrir modulation ou pause tandis que les intérêts continuent ; l'in fine décrit lors du rendez-vous n'offrait pas la même modularité. Ce constat ne doit pas être généralisé à tous les produits bancaires.

Voir : [Vente à terme / crédit vendeur — système Fruits](12_Vente_A_Terme_Credit_Vendeur_Fruits.md) et [Univers d’investissement et allocation de capital Fruits](../01_Strategie/07_Univers_Investissement_Fruits.md).

## Phrase de décision

Le bon levier est celui qui augmente la capacité d'achat sans créer de mur de remboursement, de margin call ou de dépendance à une hypothèse non maîtrisée.
