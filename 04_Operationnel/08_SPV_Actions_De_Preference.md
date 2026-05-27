# Stratégie SPV + Actions De Préférence

## Idée centrale

Fruits crée une société dédiée à un bien. Des investisseurs apportent du capital dans cette société. En échange, ils reçoivent une catégorie spéciale d'actions qui leur donne une priorité économique : rendement prioritaire cible, protection sur certains flux, droits d'information et sortie prévue.

Plus tard, Fruits peut racheter ces actions de préférence selon une formule définie dès le départ, pour reprendre 100% du contrôle économique du bien.

La logique est simple :

```text
Au lieu de créer une dette investisseur à rembourser à date fixe,
Fruits crée une couche de capital patient,
rémunérée prioritairement,
mais sans mur de remboursement brutal.
```

## Montage en une phrase

Au lieu de dire :

> Prête-moi 100k, je te rembourse dans 5 ans avec intérêts.

Fruits dit :

> Entre au capital de la société qui porte le bien. Tu as une priorité économique jusqu'à atteindre ton rendement cible. Ensuite, Fruits peut te racheter selon une formule prévue à l'avance.

Différence clé :

- Dette classique : échéance fixe, remboursement obligatoire, pression de refinancement.
- Actions de préférence : capital investisseur structuré, priorité économique, sortie organisée, plus de souplesse si le bien met du temps à produire.

## Pourquoi une SPV par actif

SPV = société véhicule dédiée à une opération.

Exemple :

```text
Fruits Dreux 001 SAS
```

Cette société ne fait qu'une chose :

- acheter ou contrôler un bien ;
- encaisser les loyers ou revenus d'exploitation ;
- payer les charges ;
- rembourser la banque senior ;
- rémunérer les investisseurs selon la waterfall ;
- remonter le surplus à Fruits.

Intérêt :

- chaque actif est isolé ;
- chaque investisseur entre dans un deal précis ;
- le risque d'un bien ne contamine pas tout le groupe ;
- la banque, les investisseurs et Fruits lisent la même société dédiée.

## Pourquoi une SAS

Les actions de préférence sont naturelles dans une société par actions, donc plutôt en SAS qu'en SCI classique.

Structure type :

| Catégorie | Détenteur | Rôle |
| --- | --- | --- |
| Actions ordinaires | Fruits Holding | Contrôle, gestion, upside |
| Actions de préférence | Investisseurs privés | Rendement prioritaire cible, protection, sortie prévue |

ADP veut dire **actions de préférence**.

Dans Fruits :

- actions ordinaires = actions détenues par Fruits, avec contrôle et upside ;
- ADP = actions détenues par les investisseurs, avec droits économiques prioritaires ;
- les ADP ne sont pas une dette bancaire ;
- les ADP ne doivent pas être vendues comme capital garanti.

Point juridique :

- Les actions de préférence peuvent avoir des droits particuliers : droits financiers, droits de vote aménagés, priorité de distribution, priorité de liquidation, conversion ou rachat.
- Les droits doivent être définis dans les statuts et le pacte.
- Le rendement ne doit pas être vendu comme garanti.
- Le rachat doit être prévu proprement, avec formule et conditions juridiques.

## Exemple avec un bien à 500k

| Source de financement | Montant |
| --- | ---: |
| Banque senior | 300 000 EUR |
| Investisseurs en actions de préférence | 150 000 EUR |
| Fruits / fondateur | 50 000 EUR |
| Total | 500 000 EUR |

Lecture :

- La banque finance 60% et reste prioritaire.
- Les investisseurs ADP financent le complément.
- Fruits met 10% de capital sponsor pour montrer son alignement.
- Fruits garde les actions ordinaires, donc la gestion et l'upside.

Variante plus agressive, à éviter au premier deal sauf actif très liquide : banque 70%, ADP 20-25%, Fruits 5-10%.

## Rémunération des investisseurs

Exemple :

- investissement ADP : 150 000 EUR ;
- rendement prioritaire cible : 8% par an ;
- priorité économique cible : 12 000 EUR par an, si la société dispose de flux distribuables et si les conditions légales/sociales sont réunies.

Waterfall simple :

| Ordre | Paiement |
| ---: | --- |
| 1 | Charges du bien |
| 2 | Banque senior |
| 3 | Réserve de sécurité |
| 4 | Investisseurs ADP : rendement prioritaire cible |
| 5 | Fees Fruits OpCo prévus et plafonnés |
| 6 | Fruits : surplus / promote |

Formulation propre :

> Les ADP donnent droit à un rendement prioritaire cible, payable selon les flux disponibles, les règles de distribution, les statuts et le pacte.

Formulation à éviter :

> Rendement garanti sans risque.

## Rémunération Fruits dans une SPV ADP

Fruits peut être rémunéré à deux niveaux.

### 1. Fees opérateur

Fruits OpCo peut facturer :

- gestion ;
- reporting ;
- asset management ;
- suivi travaux ;
- sourcing / structuration si prévu.

Ces fees doivent être :

- annoncés dès le départ ;
- raisonnables ;
- plafonnés ;
- suspendables ou réduits si covenants / réserves ne sont pas respectés.

### 2. Promote / upside

Le promote ne commence qu'après :

- paiement des charges ;
- service de la dette ;
- réserves pleines ;
- priorité économique ADP ;
- retour du capital ou formule de sortie prévue.

Exemple de split possible :

```text
capital ADP remboursé
+ rendement prioritaire cible payé
+ surplus partagé 70/30 ou 80/20
```

Attention :

- au stade 1, 70/30 veut plutôt dire 70% investisseur / 30% Fruits ;
- 70% en faveur de Fruits est possible seulement si l'investisseur est plafonné ou si la surperformance dépasse un hurdle élevé.

Voir : [Rémunération Fruits / waterfall / promote](11_Remuneration_Fruits_Waterfall.md).

## Exemple sur 5 ans

Hypothèses :

- bien acheté : 500 000 EUR ;
- banque : 300 000 EUR ;
- investisseurs ADP : 150 000 EUR ;
- Fruits : 50 000 EUR ;
- cash disponible après charges et banque : 25 000 EUR par an.

Distribution annuelle :

| Flux annuel | Montant |
| --- | ---: |
| Cash disponible | 25 000 EUR |
| Rendement prioritaire cible ADP, 8% sur 150k | -12 000 EUR |
| Cash restant pour Fruits | 13 000 EUR |

Résultat :

- l'investisseur est servi avant Fruits ;
- Fruits capte le surplus ;
- le bien est contrôlé avec 50k de capital sponsor initial ;
- le rachat peut être organisé quand le bien est stabilisé.

Stress test rapide :

- cash disponible normal : 25 000 EUR ;
- rendement prioritaire cible : 12 000 EUR ;
- couverture ADP : 2,08x ;
- si cash disponible baisse de 40% : 15 000 EUR ;
- couverture ADP stressée : 1,25x.

Conclusion : la structure reste lisible, mais elle ne supporte pas un endettement senior trop haut ou une vacance longue sans réserve.

## Option de rachat

L'option de rachat est la pièce stratégique.

Dès le départ, les statuts et le pacte doivent prévoir :

- à partir de quand Fruits peut racheter ;
- qui peut initier le rachat ;
- la formule de prix ;
- la méthode de valorisation ;
- les conditions de paiement ;
- les cas de rachat obligatoire ou accéléré ;
- les conséquences en cas de défaut, vente ou refinancement.

Exemple indicatif :

| Moment | Formule possible |
| ---: | --- |
| Année 3 | capital investi + rendement prioritaire dû |
| Année 5 | prix fixe ou capital + prime |
| Année 7 | prix majoré ou formule valeur de marché |
| Vente du bien | priorité de sortie + bonus éventuel |

Point juridique important :

- Le rachat d'actions de préférence doit être organisé dans les statuts avant la souscription si c'est une action rachetable.
- La société ne peut pas traiter le rachat comme un simple remboursement de dette.
- Le prix, la prime, les réserves distribuables et les modalités doivent être validés juridiquement.

## Pourquoi l'investisseur accepte

L'investisseur n'obtient pas tout l'upside, mais il est mieux protégé que les actions ordinaires.

Il voit :

- un bien identifié ;
- une SPV dédiée ;
- une banque senior ;
- des statuts ;
- un pacte ;
- une waterfall ;
- une réserve de sécurité ;
- une formule de rachat ;
- un reporting.

Discours investisseur :

> Vous n'avez pas à gérer le bien. Vous avez une priorité économique sur un actif identifié, avec une sortie prévue, et Fruits ne touche le surplus qu'après vous.

## Pourquoi ce n'est pas une dette

L'investisseur est actionnaire de préférence, pas simplement créancier.

Conséquences :

- il prend un risque equity ;
- son rendement est prioritaire mais pas garanti ;
- la distribution dépend des règles légales, des statuts, des flux et du résultat distribuable ;
- le rachat suit une mécanique de titres, pas un remboursement bancaire classique.

Risque à éviter :

- créer une ADP tellement fixe et obligatoire qu'elle ressemble économiquement à une dette déguisée ;
- promettre un rendement certain ;
- promettre un rachat obligatoire sans capacité financière réelle ;
- lever auprès de trop d'investisseurs sans cadre AMF / offre au public.

## Comment parler du rendement sans dire garanti

Le bon mécanisme est une priorité économique contractuelle.

Phrase interdite :

> Je vous garantis 8% par an, sans risque.

Phrase correcte :

> Les actions de préférence donnent droit à un rendement prioritaire cible de 8% par an, payé avant toute distribution à Fruits, sous réserve des flux disponibles, des règles légales de distribution, des covenants et des réserves obligatoires.

## Les 5 protections qui remplacent le mot garanti

### 1. Waterfall

Ordre de paiement :

```text
1. charges obligatoires
2. banque senior
3. réserves DSRA / capex / vacance
4. rendement prioritaire ADP
5. Fruits
```

L'investisseur est payé avant Fruits, mais après la banque et les charges.

### 2. Rendement cumulatif ou non cumulatif

Option plus protectrice :

- si le cash ne suffit pas une année, le rendement prioritaire non payé est cumulé ;
- il doit être payé plus tard avant toute distribution à Fruits ;
- mais il ne devient pas automatiquement une dette exigible immédiatement.

Formulation :

> Le rendement prioritaire cible est cumulatif et prioritaire, mais payable selon les flux disponibles et les règles de distribution.

Option plus souple pour Fruits :

- rendement non cumulatif ;
- si une année ne paie pas, il n'est pas reporté.

À utiliser seulement si le rendement cible est plus bas ou si l'investisseur accepte le risque.

### 3. Cash trap

Si les covenants ne sont pas respectés :

- pas de distribution Fruits ;
- pas de fees non essentielles ;
- cash bloqué dans la SPV ;
- reconstitution des réserves d'abord ;
- ADP prioritaire quand le cash revient.

### 4. Rachat prévu, pas garanti

Bonne formulation :

> Fruits peut racheter les ADP à partir de l'année 5 selon une formule prévue dans les statuts et le pacte.

Formulation dangereuse :

> Fruits rachètera obligatoirement les ADP à telle date quoi qu'il arrive.

Le rachat doit être une option ou un mécanisme encadré, pas une promesse de remboursement bancaire déguisée.

### 5. Droits de contrôle protecteurs

Les investisseurs ADP peuvent recevoir :

- droit d'information mensuel ;
- veto sur dette additionnelle ;
- veto sur vente de l'actif ;
- veto sur changement de manager ;
- veto sur capex majeur ;
- audit en cas d'incident ;
- interdiction de distributions si réserves non pleines.

## Résumé de la bonne formule

```text
ADP = rendement prioritaire cible
+ waterfall
+ cumul éventuel
+ cash trap
+ reporting
+ droits de veto
+ rachat possible
- garantie de rendement
- garantie de capital
```

## Structure finale recommandée

```text
Fruits Holding
     |
     | actions ordinaires
     v
Fruits Dreux 001 SAS
     |
     | détient / exploite le bien
     v
Bien immobilier

Investisseurs privés
     |
     | actions de préférence
     v
Fruits Dreux 001 SAS

Banque senior
     |
     | dette senior + sûretés
     v
Fruits Dreux 001 SAS / Bien
```

## Package contractuel minimal

### Statuts de la SAS

- catégories d'actions ;
- droits financiers des ADP ;
- droits de vote ou absence/aménagement de vote ;
- priorité de distribution ;
- priorité en cas de liquidation ;
- mécanisme de rachat ;
- méthode de prix ;
- clauses d'agrément et transfert.

### Pacte d'associés

- waterfall ;
- reporting ;
- reserved matters ;
- droit d'information ;
- cas de défaut ;
- clauses de sortie ;
- rachat volontaire / obligatoire ;
- drag/tag si nécessaire ;
- non-dilution ou droits anti-dilution si prévu.

### Term sheet investisseur

- montant investi ;
- rendement prioritaire cible ;
- durée cible ;
- formule de rachat ;
- droits de contrôle ;
- risques ;
- frais Fruits ;
- ordre de paiement.

### Gouvernance

- Fruits garde la gestion opérationnelle.
- Les investisseurs ont des droits de veto sur décisions majeures.
- La banque reste prioritaire.
- Les fees Fruits sont plafonnés et conditionnels.

## Cas d'usage dans Fruits

### Cas 1 - Complément d'equity sous dette senior

- Banque : 55-65%.
- ADP investisseurs : 20-30%.
- Fruits : 5-15%.
- Objectif : acheter plus vite sans dette junior dure.

### Cas 2 - Alternative au prêt investisseur

- L'investisseur voulait prêter.
- Fruits propose ADP avec rendement prioritaire cible et rachat.
- Objectif : éviter une échéance de remboursement brutale.

### Cas 3 - Bridge vers refinancement

- ADP finance l'equity initial.
- Le bien est stabilisé.
- Fruits refinance ou fait entrer un FO/foncière.
- Fruits rachète les ADP.

## Lien avec la logique MSTR / STRC

Fruits ne copie pas juridiquement Strategy/MSTR. Fruits reprend seulement la logique financière :

| MSTR | Fruits |
| --- | --- |
| Achète du BTC | Achète / contrôle des biens |
| Émet des preferred shares | Émet des actions de préférence |
| Évite certaines échéances de dette | Évite une dette investisseur à remboursement fixe |
| Paie un dividende prioritaire | Paie un rendement prioritaire cible |
| Garde l'actif long terme | Garde le bien long terme |
| Peut refinancer ou racheter | Peut refinancer ou racheter les investisseurs |

La vraie stratégie :

> Utiliser des investisseurs comme une couche de capital patient, rémunérée prioritairement, mais sans leur donner le contrôle total ni créer un mur de remboursement.

## Garde-fous

- Ne jamais promettre un rendement garanti.
- Ne jamais vendre le produit comme sans risque.
- Vérifier le cadre AMF si plusieurs investisseurs ou communication large.
- Valider les statuts, le pacte et le rachat avec avocat.
- Valider fiscalité et comptabilité avec expert-comptable.
- Prévoir la banque senior avant de promettre l'économie finale.
- Prévoir une vraie réserve capex/vacance.
- Prévoir un scénario où Fruits ne peut pas racheter à la date cible.

## Phrase propre à retenir

> Les investisseurs apportent du capital dans la SPV du bien via actions de préférence. Ils ont une priorité économique cible et une sortie organisée. Fruits garde les actions ordinaires, la gestion et l'upside, puis peut racheter les investisseurs quand l'actif est stabilisé ou refinancé.

## Sources juridiques

- Code de commerce, article L228-11 : actions de préférence avec ou sans droit de vote et droits particuliers définis par les statuts. https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049720022
- Code de commerce, article L228-12 : émission, conversion et rachat des actions de préférence. https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038612729
