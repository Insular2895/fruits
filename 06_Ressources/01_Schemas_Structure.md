# SCHÉMAS DE STRUCTURE

## Code couleur standard Fruits

Ce code couleur doit être repris dans tous les schémas pour se repérer vite.

| Élément | Couleur | Code | Rôle |
| --- | --- | --- | --- |
| Investisseurs / FO / UHNWI | Rose | `#FF2D95` | Apport de capital, NP, ADP, prêt privé |
| Fruits / SPV opérateur | Jaune | `#FFD400` | Véhicule qui porte ou exploite l'actif |
| OpCo / gestion Fruits | Vert | `#36D88A` | Gestion, reporting, travaux, fees |
| Banque / dette senior | Bleu foncé | `#2563EB` | Dette bancaire, bridge, crédit senior |
| Holding / trésorerie / ETF | Bleu clair | `#38BDF8` | Holding, surplus, portefeuille financier |
| Réserves / DSRA / capex | Violet | `#A855F7` | Cash sécurisé, réserves, comptes dédiés |
| Actifs immobiliers | Gris | `#E5E7EB` | Biens, lots, portefeuille |
| Flux de cash / loyers | Vert foncé | `#15803D` | Cash entrant, loyers, exploitation |
| Flux de dette / remboursement | Bleu | `#1D4ED8` | Service de dette, refinancement |
| Flux investisseur / capital | Rose foncé | `#DB2777` | Apport, remboursement investisseur |

Règle de lecture :

```text
rose = argent investisseur
jaune = SPV Fruits
vert = opération / gestion
bleu = dette / banque
violet = réserves
gris = actif immobilier
```

## Schéma 1 - Usufruit / nue-propriété avec FO

```mermaid
flowchart TD
    FO[Family Office / investisseur patrimonial]
    NP[SPV investisseur détient NP]
    BANK[Banque finance UF si possible]
    SPV[SPV Fruits achète UF]
    ASSET[Bien immobilier]
    OPCO[Fruits OpCo gestion / reporting]
    RES[DSRA + réserve capex / vacance]
    CASH[Loyers nets d'exploitation]

    FO -->|apport capital NP| NP
    NP -->|détient nue-propriété| ASSET
    BANK -->|prêt UF éventuel| SPV
    SPV -->|détient usufruit temporaire| ASSET
    ASSET -->|loyers| CASH
    CASH -->|charges + dette + réserves| RES
    CASH -->|service dette UF| BANK
    OPCO -->|gestion, travaux, reporting| ASSET
    SPV -->|fees plafonnés| OPCO
    SPV -->|remembrement à terme : FO récupère pleine propriété| NP

    classDef investor fill:#FFE4F1,stroke:#FF2D95,color:#111827,stroke-width:2px;
    classDef spv fill:#FFF7CC,stroke:#FFD400,color:#111827,stroke-width:2px;
    classDef bank fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef opco fill:#DCFCE7,stroke:#36D88A,color:#111827,stroke-width:2px;
    classDef reserve fill:#F3E8FF,stroke:#A855F7,color:#111827,stroke-width:2px;
    classDef asset fill:#F3F4F6,stroke:#6B7280,color:#111827,stroke-width:2px;
    classDef cash fill:#DCFCE7,stroke:#15803D,color:#111827,stroke-width:2px;

    class FO,NP investor;
    class SPV spv;
    class BANK bank;
    class OPCO opco;
    class RES reserve;
    class ASSET asset;
    class CASH cash;
```

## Schéma 2 - SPV avec actions de préférence

```mermaid
flowchart TD
    INV[Investisseurs ADP / UHNWI]
    HOLD[Fruits Holding actions ordinaires]
    BANK[Banque senior]
    SPV[SPV par actif]
    ASSET[Bien immobilier]
    OPCO[Fruits OpCo]
    RES[DSRA + capex + vacance]
    RENT[Loyers]
    SALE[Vente / refinancement]
    UPSIDE[Surplus / promote Fruits]

    INV -->|capital ADP prioritaire| SPV
    HOLD -->|equity sponsor + contrôle| SPV
    BANK -->|dette senior| SPV
    SPV -->|achète / porte| ASSET
    ASSET -->|loyers| RENT
    RENT -->|1 charges| SPV
    SPV -->|2 dette senior| BANK
    SPV -->|3 réserves| RES
    SPV -->|4 rendement prioritaire cible| INV
    SPV -->|5 fees plafonnés| OPCO
    SPV -->|6 surplus| UPSIDE
    SALE -->|rembourse dette + ADP puis surplus| SPV
    UPSIDE -->|dividendes / promote| HOLD

    classDef investor fill:#FFE4F1,stroke:#FF2D95,color:#111827,stroke-width:2px;
    classDef spv fill:#FFF7CC,stroke:#FFD400,color:#111827,stroke-width:2px;
    classDef bank fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef opco fill:#DCFCE7,stroke:#36D88A,color:#111827,stroke-width:2px;
    classDef reserve fill:#F3E8FF,stroke:#A855F7,color:#111827,stroke-width:2px;
    classDef asset fill:#F3F4F6,stroke:#6B7280,color:#111827,stroke-width:2px;
    classDef holding fill:#E0F2FE,stroke:#38BDF8,color:#111827,stroke-width:2px;
    classDef cash fill:#DCFCE7,stroke:#15803D,color:#111827,stroke-width:2px;

    class INV investor;
    class SPV spv;
    class BANK bank;
    class OPCO opco;
    class RES reserve;
    class ASSET asset;
    class HOLD,UPSIDE,SALE holding;
    class RENT cash;
```

## Schéma 3 - Bridge-to-term / refinancement

```mermaid
flowchart LR
    BUY[Achat rapide]
    BRIDGE[Dette bridge courte]
    STAB[Stabilisation : travaux + loyers]
    VALUE[Nouvelle valeur prudente]
    BANK[Dette bancaire long terme]
    REPAY[Remboursement bridge]
    CASHOUT[Cash-out net si DSCR OK]

    BUY --> BRIDGE
    BRIDGE --> STAB
    STAB --> VALUE
    VALUE --> BANK
    BANK --> REPAY
    BANK --> CASHOUT

    classDef action fill:#FFF7CC,stroke:#FFD400,color:#111827,stroke-width:2px;
    classDef debt fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef op fill:#DCFCE7,stroke:#36D88A,color:#111827,stroke-width:2px;
    classDef reserve fill:#F3E8FF,stroke:#A855F7,color:#111827,stroke-width:2px;

    class BUY action;
    class BRIDGE,BANK,REPAY debt;
    class STAB,VALUE op;
    class CASHOUT reserve;
```

## Images originales

![Pasted Graphic 3.png](../Attachments/C74045CC-21CD-490B-991A-222090015E76.png)

![Pasted Graphic 4.png](../Attachments/0DC0621F-C8D5-4FD0-92B8-AB7E5B7A14BD.png)
