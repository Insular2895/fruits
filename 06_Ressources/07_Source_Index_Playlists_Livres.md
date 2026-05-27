---
type: source_index
status: draft_to_validate
created: 2026-05-27
tags: [#Fruits, #sources, #books, #playlists, #videos, #draft_to_validate]
---

# Source index - playlists, livres, vidéos

## Rôle

Index de provenance pour les sources utilisées ou repérées dans le travail Fruits du 2026-05-27.

Cette note ne conserve pas les sources longues dans le vault. Elle trace :

- les livres consultés par extraits / tables des matières ;
- les playlists et vidéos filtrées ;
- les sources externes déjà mentionnées ;
- le statut de traitement.

## Statuts

- `used_excerpt` : utilisé par extraits courts ou table des matières ;
- `candidate_priority` : source prioritaire à traiter plus tard ;
- `local_corpus_filtered` : corpus local filtré mécaniquement ;
- `external_reference` : source externe citée pour cadrer un sujet ;
- `to_review` : à vérifier avant usage comme source validée.

## Livres utilisés / repérés

Source locale :

```text
/Users/insular/Desktop/book 📙/
```

| Livre | Sujet utile Fruits | Statut |
| --- | --- | --- |
| `Commercial-real-estate-analysis-investments-2nd-ed-Edition-Geltner.pdf` | underwriting immobilier, cap rate, NOI, valuation | `used_excerpt` |
| `The Book On Rental Property Investing PDF.pdf` | gestion locative, screening, exploitation résidentielle | `used_excerpt` |
| `Brandon_Turner_Heather_Turner_The_Book_on_Managz-lib.org_.pdf` | property management, locataires, prestataires | `used_excerpt` |
| `Asset-Based-Lending-The-Complete-Guide-to-Originating-Evaluating-and-Managing-Asset-Based-Loans-Leasing-and-Factoring-3rd-Edition-Peter-Clarke.pdf` | borrowing base, collateral, secured lending | `used_excerpt` |
| `Asset-BasedLendingAPracticalGuidetoSecuredFinancing8.pdf` | financement adossé à actifs, garanties | `candidate_priority` |
| `private-debt-yield-safety-and-the-emergence-of-alternative-lending-wiley-finance-2nbsped-1119944392-9781119944393_compress.pdf` | private debt, covenants, risque | `used_excerpt` |
| `Valuation-Workbook-7th-Edition-Mckinsey-Company-Inc.pdf` | valorisation, modèles, sanity checks | `used_excerpt` |
| `Rosenbaum Investment Banking.pdf` | capital stack, valuation, M&A | `used_excerpt` |

Limite : les livres ont été lus par extraits ciblés, pas en extraction exhaustive. Ils ne sont pas classés comme `validated_source`.

## Playlists / vidéos locales

Corpus local :

```text
/Users/insular/transcripts/playlists/
```

Filtrage effectué sur les titres et extraits avec des mots-clés liés à :

```text
real estate, immobilier, commercial real estate, private credit, private debt,
asset-backed finance, asset-based lending, bridge, construction lending,
valuation, cap rate, NOI, LTV, DSCR, lease, tenant, capex, reserve,
reporting, underwriting, collateral, covenant, refinancing
```

Résultat :

- 95 transcripts candidats après filtrage strict ;
- sources dominantes repérées : Blackstone, Brookfield, Apollo, Ares, Oaktree, CAIA, TMBA, MSCI ;
- les vidéos sont des sources secondaires ou opinions professionnelles, donc `to_review` avant usage fort.

## Vidéos prioritaires à traiter ensuite

| Source locale | Sujet utile Fruits | Statut |
| --- | --- | --- |
| `playlists/Playlist 33/27 - Commercial Real Estate Amid Inflation ｜ 1x1 with Blackstone’s Nadeem Meghji.en.txt` | inflation, cash-flow growth, baux, pricing power | `candidate_priority` |
| `playlists/Playlist 33/21 - You Can’t Paint Real Estate with a Broad Brush ｜ 1x1 with Blackstone’s Kathleen McCarthy.en.txt` | dispersion par segment, demande/offre, qualité actifs | `candidate_priority` |
| `playlists/Playlist 20/49 - 2024 Real Estate Investing Outlook with Brian Kingston and Lowell Baron.en.txt` | outlook immobilier, going-in yield, flight to quality | `candidate_priority` |
| `playlists/Playlist 17/16 - 021524 TMBA Webinar：  Strategies to Grow and Expand Your Construction Lending Program.en.txt` | construction lending, draw requests, budgets, réserves | `candidate_priority` |
| `playlists/Playlist 23/15 - Conversations： The Evolution of Asset-Backed Finance with Armen Panossian, Brendan Beer, and Jenn....en.txt` | asset-backed finance, cash-flows contractuels | `candidate_priority` |
| `playlists/Playlist 31/03 - Private Credit： What You Need to Know.en.txt` | private credit, senior secured loans, risque | `candidate_priority` |
| `playlists/Playlist 31/05 - Michael Zawadzki on Private Credit Opportunities in Europe.en.txt` | private credit Europe | `candidate_priority` |
| `playlists/Playlist 1/77 - Real Estate Investing： Inflation, Location, and Valuation.en.txt` | inflation, location, valuation lag | `candidate_priority` |
| `playlists/Playlist 17/13 - 111623 TMBA Webinar：  Equitable Appraisal Practices： Insights from Residential Property Appraisers.en.txt` | appraisal process, biais de valorisation | `candidate_priority` |
| `playlists/Playlist 37/15 - 🏡 Ce que votre banquier ne dit pas sur l'immobilier....en.txt` | banque, DPE, financement immobilier FR | `candidate_priority` |

## Sources externes déjà mentionnées

| Source | Sujet | Statut |
| --- | --- | --- |
| Label bas-carbone - Ministère | crédits carbone volontaires / certification | `external_reference` |
| SNCRR - Ministère | biodiversité, restauration, renaturation | `external_reference` |
| Code forestier L341-6 - Légifrance | défrichement, compensation | `external_reference` |

Ces sources sont à relire directement avant d'être utilisées dans un pitch, un modèle financier ou une décision.

## Notes Graphipy liées

- [Filtrage playlists et livres - immo / BTP / Fruits](04_Filtrage_Playlists_Livres_Immo_BTP_Fruits.md)
- [Consolidation stratégique Fruits - idées à intégrer](05_Consolidation_Strategique_Fruits_Draft.md)
- [Intégration conversations GPT - Fruits ready](06_Integration_Conversations_GPT_Fruits_Ready.md)
- [Sections à compléter / revoir](../07_A_Completer_A_Revoir/INDEX.md)

## À faire

- choisir 3 à 5 vidéos prioritaires à traiter en détail ;
- créer une fiche par vidéo réellement utile ;
- créer une fiche par livre seulement si le livre devient source centrale ;
- séparer les sources US / UK / internationales des règles applicables en France ;
- demander validation avant de passer une source en `validated_source`.
