# Stratégie Lombard / Anti-Crash

## Objectif

- Ne pas vendre les ETF long terme sous stress.
- Ne pas subir de liquidation forcée.
- Garder une crédibilité bancaire et investisseur.
- Utiliser le lombard comme outil de liquidité, pas comme revenu.

## Règle de base

Le lombard est une dette mark-to-market : si le collatéral baisse, la banque peut demander du cash ou vendre le collatéral.

Donc Fruits doit traiter le lombard comme une ligne de flexibilité courte/moyenne durée, jamais comme le moteur principal du modèle.

## Architecture cible

- Portefeuille collatéral liquide : ETF larges, fonds monétaires, T-Bills/monétaire UCITS selon banque.
- LTV interne cible : 20-25%.
- LTV interne maximum : 30% sur portefeuille actions diversifié.
- LTV plus élevée uniquement sur collatéral monétaire/obligataire très court terme, si la banque l'accepte.
- Réserve cash dédiée : au moins 30-50% du montant lombard.
- Deuxième source de liquidité préparée : banque 2, refinancement, actif vendable, cash-flow locatif.

## Pourquoi 40-50% LTV est trop agressif

Exemple simple :

| LTV initial | Baisse portefeuille | LTV après baisse |
| ---: | ---: | ---: |
| 20% | -40% | 33% |
| 30% | -40% | 50% |
| 40% | -40% | 67% |
| 50% | -40% | 83% |

Conclusion : sur ETF actions, 40-50% peut devenir dangereux dans un vrai crash. La zone défendable pour Fruits est 20-30% maximum.

## Règles fixes

- Ne pas vivre sur le lombard.
- Ne pas financer l'exploitation courante avec le lombard.
- Ne pas financer une dette longue avec une dette mark-to-market.
- Ré-emprunter seulement après hausse et baisse de LTV.
- Rembourser avant l'appel de marge.
- Garder une réserve dédiée séparée du cash opérationnel.

## Déclencheurs opérationnels

### Marché normal

- LTV < 20-25% : aucune action.
- LTV < 20% durablement : possibilité de réutiliser une petite partie, seulement si use of proceeds défendable.

### Baisse -10% à -15%

- Recalcul LTV.
- Pas d'action automatique.
- Interdiction d'augmenter le lombard.

### Baisse -20% à -25%

- Si LTV > 30% : remboursement volontaire partiel.
- Source : réserve cash dédiée.
- Objectif : revenir sous 25-30%.

### Baisse -30% à -35%

- Stop total du levier.
- Remboursement ciblé via réserve cash et flux disponibles.
- Objectif : réduire la dette avant que la banque ne force une action.

### Baisse -40% à -50%

- Remboursement massif si possible.
- Activation de la dette non mark-to-market seulement si déjà négociée.
- Vente d'un actif non stratégique en dernier recours.
- Objectif : zéro liquidation forcée du portefeuille long terme.

## Ce qu'il faut préparer avant d'utiliser le lombard

- Deux banques privées/lombard identifiées.
- Conditions de margin call comprises par écrit.
- Haircuts par actif.
- Seuils internes de remboursement.
- Réserve cash isolée.
- Interdiction interne de financer dépenses personnelles ou pertes opérationnelles.
- Reporting mensuel : valeur collatéral, dette, LTV, réserve, stress -20/-30/-40%.

## Règle d'or

On rembourse une dette volatile avec des flux stables ou du cash disponible. On ne finance pas un actif long terme avec une dette qui peut être rappelée brutalement.
