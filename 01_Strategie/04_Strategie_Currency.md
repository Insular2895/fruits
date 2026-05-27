# Stratégie Currency / FX

## Objectif

Gérer le risque de change uniquement si Fruits emprunte, investit ou reçoit des revenus dans une devise différente de ses flux naturels.

## Règle simple

Ne pas créer de dette en devise étrangère juste parce que le taux facial paraît plus bas. Le gain de taux peut être effacé par le change, les frais de couverture et la complexité juridique.

## Instruments possibles

### Forward FX

- Contrat à terme de change.
- Horizon naturel : 1-12 mois, parfois renouvelable.
- Utile pour couvrir une acquisition ou un remboursement connu.
- Risque : coût de rollover, dépendance au marché, besoin de collatéral.

### Cross-currency swap

- Échange de flux dans deux devises.
- Adapté à une dette importante et longue.
- À réserver aux deals institutionnels avec banque solide.
- Complexité : ISDA, collatéral, valorisation mark-to-market, frais.

## Quand l'utiliser

- Deal > 5-10M.
- Revenus ou actifs dans une devise différente.
- Banque internationale capable de documenter proprement.
- Spread de taux suffisant après coût de couverture.
- Stress test FX réalisé.

## Quand l'éviter

- Premiers actifs.
- Petits tickets.
- Revenus EUR avec dette hors EUR non couverte.
- Montage que l'investisseur ou la banque ne comprend pas.

## Analyse par devise

| Devise | Rôle principal | Outil prioritaire | Quand la choisir | Quand l'éviter |
| --- | --- | --- | --- | --- |
| EUR | Base propre | Crédit basique | Actif/revenus en EUR ; simplicité ; scalabilité | Si une autre devise donne un vrai edge net après hedge |
| DKK | Défensif hors euro | Crédit basique / forward léger | Quasi-EUR hors zone euro ; logique nordique ; investisseur DKK | Si tu cherches un gros upside FX |
| CHF | Défensif premium | Forward / collar | Montage prudent avec banque privée suisse ; collatéral solide | Si tu cherches une devise offensive ou du levier agressif |
| JPY | Funding currency offensive | Collar puis option FX | Seulement si deal institutionnel, hedge clair, stress test validé | Si tu refuses volatilité, complexité ou margin collateral |
| USD | Devise de structuration | Crédit local si revenus USD, sinon forward/CCS | Actif/revenus USD ; besoin de profondeur marché ; investisseur USD | Si le seul but est de battre le coût EUR après hedge |
| CNH | Niche offensive | Forward / NDF | Vrai angle Chine/Hong Kong, revenus ou investisseur RMB/HK | Si aucun lien opérationnel RMB/HK |
| KRW / MYR / BRL / CLP / MXN | Devises locales, pas funding global | Crédit local + forward/NDF | Actif et revenus locaux | Si tu veux juste remplacer un prêt EUR par une dette moins chère |

## Lecture critique du tableau

Je suis d'accord avec la logique générale, avec une nuance importante : le classement ne veut pas dire qu'il faut utiliser ces devises maintenant.

Pour Fruits :

- EUR = devise par défaut.
- CHF = éventuellement utile avec banque privée, mais à couvrir.
- DKK = défensif mais rarement nécessaire si les actifs sont en France/zone euro.
- USD = utile si investisseur, actif ou revenu en USD ; sinon le hedge ramène souvent le coût proche de l'EUR.
- JPY = séduisant en taux facial, mais dangereux : le risque de change et le coût/roll du hedge peuvent détruire l'avantage.
- CNH et devises EM = hors scope sauf actif/revenus locaux.

## Règle de décision FX

Une dette en devise étrangère est acceptable seulement si les 5 conditions sont réunies :

1. Le spread net après hedge reste positif.
2. Les flux de remboursement sont couverts ou naturellement dans la devise.
3. Le coût de hedge est modélisé sur toute la durée.
4. Le collateral/margin du hedge est financé.
5. L'investisseur et la banque comprennent le montage.

Sinon, rester en EUR.

## Règle Fruits

Phase 1 et 2 : rester principalement en EUR.

Phase 3 : étudier FX uniquement pour financement institutionnel, actifs hors zone euro ou investisseur étranger avec vraie raison économique.
