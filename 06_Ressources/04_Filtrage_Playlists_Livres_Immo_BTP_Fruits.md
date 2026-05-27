---
type: source_research
status: draft_to_validate
created: 2026-05-27
tags: [#Fruits, #real-estate, #btp, #private-credit, #source-research, #to_validate]
---

# Filtrage playlists et livres - immo / BTP / Fruits

## Role

Filtrage des anciennes playlists locales et des livres du dossier Desktop pour extraire les termes, techniques, methodes et sources qui peuvent servir au projet Fruits.

Cette note ne cree aucune decision. Elle sert de base de recherche et de triage pour enrichir ensuite les modeles financiers, la data room, les term sheets et les workflows operationnels.

## Corpus observe

### Playlists locales

Source locale :

```text
/Users/insular/transcripts/playlists/
```

Filtrage mecanique effectue sur les titres et extraits avec mots-cles :

```text
real estate, immobilier, rental, commercial real estate, private credit,
private debt, asset-backed finance, asset-based lending, bridge,
construction lending, appraisal, valuation, cap rate, NOI, LTV, DSCR,
lease, tenant, rent, capex, reserve, reporting, underwriting, collateral,
covenant, refinancing, affordable housing, logistics, data center
```

Resultat brut :
- 95 transcripts candidats apres filtrage strict.
- Sources dominantes : Blackstone, Brookfield, Apollo, Ares, Oaktree, CAIA, TMBA, MSCI.

### Livres Desktop

Source locale :

```text
/Users/insular/Desktop/book 📙/
```

Livres les plus pertinents observes en premier :
- `Commercial-real-estate-analysis-investments-2nd-ed-Edition-Geltner.pdf`
- `The Book On Rental Property Investing PDF.pdf`
- `Brandon_Turner_Heather_Turner_The_Book_on_Managz-lib.org_.pdf`
- `Asset-Based-Lending-The-Complete-Guide-to-Originating-Evaluating-and-Managing-Asset-Based-Loans-Leasing-and-Factoring-3rd-Edition-Peter-Clarke.pdf`
- `Asset-BasedLendingAPracticalGuidetoSecuredFinancing8.pdf`
- `private-debt-yield-safety-and-the-emergence-of-alternative-lending-wiley-finance-2nbsped-1119944392-9781119944393_compress.pdf`
- `Valuation-Workbook-7th-Edition-Mckinsey-Company-Inc.pdf`
- `Rosenbaum Investment Banking.pdf`

## Extraction utile pour Fruits

### Underwriting immobilier

| Terme / methode | Usage possible Fruits | Source | Statut |
| --- | --- | --- | --- |
| Cash-flow growth | Verifier que la croissance de NOI / loyers compense taux plus hauts et multiples plus bas. | Blackstone - `Commercial Real Estate Amid Inflation` | immediate_useful |
| Short-duration leases | Preferer les baux permettant repricing plus rapide si l'actif a du pricing power. | Blackstone - `Commercial Real Estate Amid Inflation` | immediate_useful |
| Pricing power | Filtrer les actifs capables de hausser les loyers sans casser l'occupation. | Blackstone - `Commercial Real Estate Amid Inflation` | immediate_useful |
| Long-duration bond analogy | Eviter les actifs a baux longs sans croissance, qui reagissent comme obligations longues en hausse de taux. | Blackstone - `Commercial Real Estate Amid Inflation` | immediate_useful |
| Dispersion of performance | Ne pas raisonner "immo" globalement ; segmenter par usage, ville, demande, offre, qualite. | Blackstone - `You Can't Paint Real Estate with a Broad Brush` | immediate_useful |
| Demand tailwinds | Prioriser les actifs avec demande structurelle et offre insuffisante. | Blackstone - `You Can't Paint Real Estate with a Broad Brush` | immediate_useful |
| Going-in yield | Exiger un rendement d'entree plus robuste avant de compter sur expansion de multiple. | Brookfield - `2024 Real Estate Investing Outlook` | immediate_useful |
| Flight to quality | Integrer la qualite de l'actif et les attentes locataires dans l'analyse de vacance. | Brookfield - `2024 Real Estate Investing Outlook` | useful |
| Valuation lag | Les valorisations privees peuvent reagir en retard ; prudence dans les comparables. | CAIA - `Real Estate Investing: Inflation, Location, and Valuation` | immediate_useful |
| Cap rate vs taux sans risque | Comparer cap rate, OAT/Treasury, spread de risque et croissance attendue. | CAIA - `Real Estate Investing: Inflation, Location, and Valuation` | immediate_useful |

### BTP / travaux / construction

| Terme / methode | Usage possible Fruits | Source | Statut |
| --- | --- | --- | --- |
| Construction lending program | Si Fruits finance ou pilote des travaux, formaliser politique, process, roles et systeme de suivi. | TMBA - `Strategies to Grow and Expand Your Construction Lending Program` | useful |
| Draw request | Creer un workflow de deblocage travaux : devis, avancement, inspection, facture, reserve. | TMBA - construction lending | immediate_useful |
| Builder budget | Exiger budget travaux detaille, lots, planning, contingence, responsable, justificatifs. | TMBA - construction lending | immediate_useful |
| Contingency reserve | Ajouter reserve travaux/imprevus distincte de DSRA et reserve vacance. | TMBA - construction lending | useful |
| Interest reserve | Pour operation avec travaux lourds, prevoir reserve interets si revenus differes. | TMBA - construction lending | useful |
| Permit status | Verifier permis/autorisations avant closing ou decaissement. | TMBA - construction lending | immediate_useful |
| Fixed-price vs cost-plus contract | Comparer contrat prix fixe et regie/cost-plus selon risque, taille et controle. | TMBA - construction lending | to_validate |
| DPE / renovation energetique | En France, integrer DPE, interdictions de location, cout et calendrier de remise a niveau. | Playlist FR - `Ce que votre banquier ne dit pas sur l'immobilier` | to_validate |

### Dette / credit / collateral

| Terme / methode | Usage possible Fruits | Source | Statut |
| --- | --- | --- | --- |
| Senior secured loan | Confirmer la dette senior prudente et la priorite de remboursement. | Blackstone - `Private Credit: What You Need to Know` | immediate_useful |
| Loan-to-value | Garder LTV comme KPI central par actif et par structure. | Blackstone / TMBA / ABL sources | immediate_useful |
| Asset-backed finance | Penser certains financements comme flux contractuels + collateral, pas seulement valeur de revente. | Oaktree - `Evolution of Asset-Backed Finance` | useful |
| Contractual cash flows | Qualifier loyers, baux, creances, garanties, durees et concentration. | Oaktree - ABF | immediate_useful |
| Borrowing base certificate | Inspirer un reporting collateral : valeur eligible, haircuts, limites, exclusions. | Peter Clarke - `Asset-Based Lending` | useful |
| Collateral margin / haircut | Appliquer decotes par qualite d'actif, liquidite, vacance, travaux, concentration. | Peter Clarke - ABL | useful |
| Cash collateral / block accounts | Inspirer comptes dedies, controle paiements et prevention commingling. | Peter Clarke - ABL | useful |
| Covenants and loan agreement | Traduire les covenants Fruits : LTV, DSCR, reserves, reporting, no cash pooling. | Stephen Nesbitt - `Private Debt` | useful |
| Covenant stripping | Risque a surveiller : dette trop souple qui masque le risque. | Stephen Nesbitt - `Private Debt` | to_validate |

### Capital stack / waterfall

| Terme / methode | Usage possible Fruits | Source | Statut |
| --- | --- | --- | --- |
| Capital stack construction | Decomposer clairement dette senior, reserve, ADP/preferred equity, common equity, promote. | CAIA - real estate valuation | immediate_useful |
| Preferred equity | Confirmer le vocabulaire ADP / preferred return / rachat prevu mais non garanti. | Private credit / real estate sources | immediate_useful |
| Waterfall | Documenter l'ordre : charges, dette, DSRA, capex/vacance, retour capital, preferred return, promote. | Fruits + sources private markets | immediate_useful |
| Mezzanine / junior debt | Garder pour stade 2+, pas au demarrage sans track record et intercreditor. | Oaktree / Apollo ABF | later |
| Bridge-to-term | Utile pour actifs a stabiliser, mais sortie alternative obligatoire. | Private credit / Fruits existing | immediate_useful |

### Operations / reporting

| Terme / methode | Usage possible Fruits | Source | Statut |
| --- | --- | --- | --- |
| System of record | Sortir du tableur seul pour les workflows travaux, investisseurs, reporting et preuves. | TMBA - construction lending | immediate_useful |
| Monthly reporting | Standardiser rent roll, vacance, impayes, DSRA, capex, incidents, covenants. | Fruits + ABL reporting logic | immediate_useful |
| Tenant screening | Creer checklist locataire : revenus, historique, references, scoring, pieces. | BiggerPockets - managing rentals | useful |
| Lease file | Dossier bail complet : bail, etat des lieux, depot, assurances, communications. | BiggerPockets - managing rentals | useful |
| Contractor management | Liste prestataires, devis, licences/assurances, paiement par jalons, inspection. | BiggerPockets + TMBA | useful |
| Property manager oversight | Meme si delegation, Fruits doit auditer le gestionnaire et ses KPI. | BiggerPockets - managing rentals | useful |

### Legal / compliance / points France

| Terme / methode | Usage possible Fruits | Source | Statut |
| --- | --- | --- | --- |
| Appraisal process | Encadrer valorisation initiale, comparables, biais et conflit d'interet. | TMBA - appraisal practices | to_validate |
| Perfection of security interest | Principe utile en ABL US, a traduire en droit FR : hypotheque, nantissement, cession, garanties. | Peter Clarke - ABL | to_validate |
| Zoning / permitting | Risque local majeur pour travaux, densification, division, changement d'usage. | Affordable housing / construction sources | to_validate |
| DPE rental bans | Important pour France : verifier seuils, calendrier et couts par actif. | Playlist FR immobilier | to_validate |
| Fair housing / anti-discrimination | Source US, mais rappelle de formaliser criteres locataires objectifs. | BiggerPockets / TMBA | to_validate |

## Sources prioritaires a traiter ensuite

1. `playlists/Playlist 33/27 - Commercial Real Estate Amid Inflation ｜ 1x1 with Blackstone’s Nadeem Meghji.en.txt`
2. `playlists/Playlist 33/21 - You Can’t Paint Real Estate with a Broad Brush ｜ 1x1 with Blackstone’s Kathleen McCarthy.en.txt`
3. `playlists/Playlist 20/49 - 2024 Real Estate Investing Outlook with Brian Kingston and Lowell Baron.en.txt`
4. `playlists/Playlist 17/16 - 021524 TMBA Webinar：  Strategies to Grow and Expand Your Construction Lending Program.en.txt`
5. `playlists/Playlist 23/15 - Conversations： The Evolution of Asset-Backed Finance with Armen Panossian, Brendan Beer, and Jenn....en.txt`
6. `playlists/Playlist 31/03 - Private Credit： What You Need to Know.en.txt`
7. `playlists/Playlist 31/05 - Michael Zawadzki on Private Credit Opportunities in Europe.en.txt`
8. `playlists/Playlist 1/77 - Real Estate Investing： Inflation, Location, and Valuation.en.txt`
9. `playlists/Playlist 17/13 - 111623 TMBA Webinar：  Equitable Appraisal Practices： Insights from Residential Property Appraisers.en.txt`
10. `playlists/Playlist 37/15 - 🏡 Ce que votre banquier ne dit pas sur l'immobilier....en.txt`
11. `/Users/insular/Desktop/book 📙/Commercial-real-estate-analysis-investments-2nd-ed-Edition-Geltner.pdf`
12. `/Users/insular/Desktop/book 📙/The Book On Rental Property Investing PDF.pdf`
13. `/Users/insular/Desktop/book 📙/Brandon_Turner_Heather_Turner_The_Book_on_Managz-lib.org_.pdf`
14. `/Users/insular/Desktop/book 📙/Asset-Based-Lending-The-Complete-Guide-to-Originating-Evaluating-and-Managing-Asset-Based-Loans-Leasing-and-Factoring-3rd-Edition-Peter-Clarke.pdf`
15. `/Users/insular/Desktop/book 📙/private-debt-yield-safety-and-the-emergence-of-alternative-lending-wiley-finance-2nbsped-1119944392-9781119944393_compress.pdf`

## Prochaines fiches reflexes possibles

- `checklist_underwriting_actif_fruits`
- `checklist_data_room_actif_fruits`
- `workflow_draw_request_travaux`
- `template_reporting_mensuel_spv`
- `lexique_capital_stack_waterfall_fruits`
- `checklist_dpe_travaux_louabilite`
- `checklist_borrowing_base_collateral_fruits`

## Limites

- Les videos sont des sources secondaires ou opinions professionnelles ; elles ne valident pas une strategie Fruits.
- Les livres PDF ont ete lus par extraits courts / tables des matieres, pas en extraction exhaustive.
- Les points juridiques US comme UCC Article 9 et perfection of security interest doivent etre traduits avec avocat/notaire/fiscaliste avant usage en France.
- Les informations de marche 2024-2025 peuvent etre obsoletes ou sensibles au pays ; verifier avec sources primaires avant pitch investisseur.
