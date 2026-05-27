---
type: gpt_conversation_source
status: historical_to_review
created: 2026-05-27
tags: [#Fruits, #FX, #debt, #hedge, #finance]
may_be_obsolete: true
---

# Conversation GPT - Dette devise, FX, hedge

## Résumé source

La conversation explore l'idée d'emprunter dans une devise moins chère, puis de couvrir le risque FX pour obtenir un coût total inférieur à un prêt EUR.

Conclusion conversationnelle :

```text
Oui, possible, mais seulement si le coût total après hedge bat vraiment le prêt EUR simple.
```

## Formule centrale

Coût total réel :

- taux du prêt étranger ;
- coût du hedge ;
- frais FX ;
- marge banque ;
- complexité opérationnelle ;
- coût de documentation ;
- coût d'unwind / roll.

Comparer au prêt EUR simple, pas au taux affiché.

## Outils discutés

### Dette locale / natural hedge

- Actif local + revenus locaux = dette locale en priorité.
- Exemple : actif au Chili, revenus CLP, dette CLP.

### Dette non couverte

- Peut être rentable si FX favorable.
- Mais c'est un pari FX.
- À éviter comme base Fruits.

### Forward / NDF

- Fixe un taux futur.
- Utile pour flux prévisibles.
- Bon outil de stabilisation, pas d'upside.

### Option FX

- Assurance + upside.
- Plus chère.
- Bon outil offensif si on accepte la prime.

### Collar

- Option achetée + option vendue.
- Souvent meilleur compromis terrain.
- Peut être zero-cost upfront, mais pas gratuit économiquement.

### CCS

- Très propre et institutionnel.
- Stabilise mais enlève une grande partie du potentiel de gain.
- Outil de stabilité, pas d'alpha.

## Classement conversationnel

Rentabilité pure :

1. JPY non couvert.
2. JPY + option FX.
3. JPY + collar.
4. JPY + couverture principal final seulement.
5. JPY + CCS.
6. Prêt EUR simple.

Robustesse / usage réel :

1. JPY + collar.
2. JPY + option FX.
3. EUR simple.
4. JPY + CCS.
5. JPY non couvert.

## Devises

- EUR : base propre.
- DKK : défensif quasi-euro.
- CHF : défensif premium.
- JPY : meilleure devise offensive théorique.
- USD : structuration, pas forcément meilleure pour battre EUR après hedge.
- CNH : niche si angle Chine / Hong Kong.
- KRW / MYR / BRL / CLP / MXN : plutôt dette locale + forward / NDF.

## Traduction Fruits

Règle prudente :

```text
Phase 1 Fruits = dette simple, lisible, EUR.
FX structuré = outil later stage, seulement si ticket et conseil suffisants.
```

Sections impactées :

- `06_FX_Funding_Framework.md`
- `03_Levier_Financier.md`
- `04_Strategie_Currency.md`

## À valider

- seuil de ticket minimum ;
- banques capables de coter ;
- coût advisor ;
- fiscalité / comptabilité du hedge ;
- stress tests FX ;
- interdiction de présenter le gain FX comme rendement garanti.

