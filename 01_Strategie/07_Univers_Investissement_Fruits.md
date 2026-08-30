# Univers d’investissement et allocation de capital Fruits

> **Statut :** politique interne canonique — `conditional_recommendation`
> **Décision d’exécution :** aucune ; chaque investissement reste soumis à la checklist et aux validations applicables
> **Périmètre :** trésorerie et capitaux propres de Fruits gérés pour compte propre, hors fonds de tiers
> **Snapshot de marché vérifié :** 19 août 2026, avec dernières publications disponibles indiquées par ligne
> **Prochaine revue :** avant toute première exécution, puis au minimum trimestrielle et à chaque changement matériel de passif, de taux ou de covenant

## Executive Summary — résumé exécutif

Fruits sépare quatre fonctions qui ne doivent pas être confondues : **Fortress** rembourse les engagements, **Protection+** améliore avec prudence le rendement de la partie défensive, **Growth** construit le patrimoine et **International** n’est utilisé que si son avantage survit à la couverture de change et à tous les coûts.

Le rendement n’est jamais le premier filtre d’une somme affectée à une dette. La date, le montant certain, la liquidité et les droits contractuels passent avant le coupon. Un ETF actions appartient exclusivement à Growth : il ne constitue ni une réserve de sécurité, ni un DSRA, ni la poche de remboursement d’un vendeur ou d’une banque.

Les fourchettes de ce document sont des **ordres de grandeur**, pas des promesses. Les décisions se prennent sur un ISIN, une maturité, un prix, un rendement actuariel net, une enveloppe et un contrat de nantissement effectivement vérifiés. Les modèles d’allocation et limites proposés sont des **hypothèses à tester et à valider**, non des mandats automatiques.

> **Fortress rembourse les engagements. Protection+ améliore le rendement prudent. Growth construit le patrimoine. Fruits Growth cherche l’alpha opérationnel.**

> **Une même poche ne doit pas simultanément garantir une dette certaine et rechercher un rendement spéculatif.**

## 1. Philosophie, périmètre et gouvernance

### 1.1 Ordre des priorités

1. préserver la solvabilité de chaque entité et respecter l’isolement des SPV ;
2. rendre disponible à temps l’argent correspondant aux passifs connus ;
3. préserver une liquidité adaptée aux charges, impôts, travaux, covenants et aléas ;
4. améliorer le rendement prudent sans masquer le risque de crédit, de taux ou de liquidité ;
5. investir uniquement le surplus réel dans Growth ;
6. préférer une architecture simple, vérifiable et portable à un rendement facial plus élevé.

### 1.2 Ce que cette politique autorise — et ce qu’elle n’autorise pas

Cette note définit l’univers **admissible à l’étude** et la méthode de décision. Elle ne vaut ni conseil en investissement, ni mandat de gestion, ni validation fiscale, comptable, juridique, bancaire ou réglementaire. `CORE` signifie « composant central possible après contrôle », pas « achat autorisé sans analyse ».

La politique vise les actifs détenus pour compte propre par l’entité qui en est juridiquement propriétaire. Toute mise en commun de capitaux de tiers, gestion pour autrui ou politique d’investissement au bénéfice d’investisseurs externes exige une analyse réglementaire séparée, notamment au regard de la qualification éventuelle de FIA.

Les réserves d’une SPV financée restent dans la SPV si les contrats ou la prudence l’exigent. Il n’existe ni cash pooling implicite, ni remontée automatique vers la holding, ni droit automatique d’utiliser un collatéral nanti.

### 1.3 Règle de disponibilité

Avant toute allocation :

```text
capital réellement allocable
= trésorerie juridiquement disponible
- charges, fiscalité et CAPEX provisionnés
- DSRA et réserves minimales
- cash restreint ou nanti
- déficit de financement des échéances certaines
```

Si le résultat est négatif ou incertain, aucune poche Growth supplémentaire n’est financée.

## 2. Univers d’investissement filtré Fruits

### 2.1 Lecture de la matrice

- `🟢` ne signifie pas sans risque : une obligation souveraine longue peut baisser fortement avant son échéance.
- la sécurité d’un titre obligataire suppose l’émetteur solvable, le bon rang, la bonne devise et, pour une somme certaine, une détention jusqu’à une maturité correctement appariée ;
- les rendements de marché sont bruts, avant frais, fiscalité, éventuel hedge et pertes ;
- les cibles non cotées et actions sont des hypothèses Fruits de simulation, non des taux actuels.

> **Les taux indiqués ne sont ni garantis ni permanents. Ils servent à illustrer l’ordre de grandeur observé au moment de la rédaction. Toute décision d’investissement doit utiliser le rendement disponible au moment du deal.**

| Bloc Fruits | Produit | Rendement indicatif | Risque | Liquidité | Usage Fruits | Statut |
| --- | --- | ---: | --- | --- | --- | --- |
| 🛡️ **Fortress** | **BTF France** | 2,40–2,78 % vérifié | 🟢 | 🟢🟢 | échéances < 1 an | **CORE** |
| 🛡️ | **EU-Bills** | 2,40–2,70 % vérifié | 🟢 | 🟢🟢 | trésorerie / diversification | **CORE** |
| 🛡️ | **CAT / dépôt à terme** | 2,45–2,90 % moyenne statistique entreprises | 🟢/🟡 banque | 🟡 | cash à date connue | **CORE** |
| 🛡️ | **Monétaire EUR** | €STR 2,184 % avant frais de fonds | 🟢 | 🟢🟢 | liquidité immédiate | **CORE** |
| 🛡️ | **OAT 2–7 ans** | 3,04–3,58 % vérifié | 🟢 crédit / 🟡 duration | 🟢 | paiements intermédiaires | **CORE** |
| 🛡️ | **OAT ~10 ans** | 3,86–3,95 % vérifié | 🟢 crédit / 🟡 duration | 🟢 | dette vendeur autour de 10 ans | **CORE** |
| 🛡️ | **STRIPS OAT** | 3–4 % = filtre indicatif ; cotation ISIN requise | 🟢 crédit / 🟡 duration | 🟢/🟡 | **ballon final connu** | **CORE++** |
| 🛡️ | **OAT€i / OATi** | 1,81–2,29 % réel vérifié + inflation de référence | 🟢 crédit / 🟡 indexation-duration | 🟢 | protection inflation | **CORE** |
| 🛡️ | **EU-Bonds** | 2,81–3,83 % vérifié sur 2029–2041 | 🟢 crédit / 🟡 duration | 🟢 | diversification souveraine EUR | **CORE** |
| 🛡️ | **Bund / souverains AAA EUR** | 2,93–3,29 % vérifié sur 5–15 ans | 🟢 crédit / 🟡 duration | 🟢🟢 | sécurité et diversification | **CORE** |
| 🛡️ | **Dette supranationale** | 2,42 % bill ESM ; 2,51 % à l’émission EFSF 5 ans | 🟢 crédit / 🟡 duration | 🟢🟢 | BEI / ESM / EFSF, selon ligne | **CORE** |
| ⚖️ **Protection+** | **Covered bonds** | indice EUR identifié : 3,23–3,31 % | 🟢🟡 | 🟢 | rendement > souverain | **CORE** |
| ⚖️ | **Corporate IG EUR** | indice large : 3,93 % ; filtre ISIN 3,5–5,5 % | 🟡 | 🟢 | rendement intermédiaire | **CORE avec limites** |
| ⚖️ | **Bank senior debt** | 3,5–5,5 % = filtre, pas taux universel | 🟡 | 🟢 | diversification IG | **CORE avec limites** |
| ⚖️ | **FRN EUR / CCTeu** | taux court + spread, selon formule du titre | 🟢🟡 | 🟢 | duration courte / hausse des taux | **CORE** |
| ⚖️ | **ETF obligataire à échéance cible** | 3–5 % = filtre ; YTM du portefeuille et frais à vérifier | 🟡 | 🟢🟢 | ladder / diversification | **CORE avec contrôle** |
| ⚖️ | **Infrastructure debt senior** | 4–7 % = cible Fruits, non observée comme taux unique | 🟡 | 🟡/🔴 | Yield+ long terme | **V2** |
| ⚖️ | **Real estate senior debt** | 4–7 % = cible Fruits, non observée comme taux unique | 🟡 | 🔴 | expertise immobilière à démontrer côté crédit | **V2** |
| 🚀 **Growth** | **ETF World** | 6–8 % = hypothèse de rendement total LT | 🟠 | 🟢🟢 | croissance liquide | **CORE GROWTH** |
| 🚀 | **Infrastructure cotée diversifiée** | 6–9 % = hypothèse Fruits | 🟠 | 🟢🟢 | diversification | **OPTIONNEL** |
| 🚀 | **REIT / SIIC diversifiées** | 5–9 % = hypothèse Fruits | 🟠 | 🟢🟢 | immobilier liquide, corrélation à surveiller | **OPTIONNEL** |
| 🚀 | **Nouveaux deals Fruits** | > 10 % de TRI = seuil recherché, non promis | 🟠 | 🔴 | **croissance du groupe** | **CORE GROWTH** |
| 🚀 | **Private credit senior diversifié** | 7–10 % = cible Fruits après pertes et frais | 🟠 | 🔴 | rendement supérieur | **V2/V3 seulement** |
| 🌍 **International** | **Treasuries US couverts EUR** | 3,86–4,71 % brut USD sur 3 mois–10 ans | 🟢 crédit / FX à couvrir | 🟢🟢 | si meilleur net que l’EUR | **OPPORTUNISTE** |
| 🌍 | **Treasury STRIPS couverts EUR** | rendement du STRIP/échéance coté, brut USD | 🟢 crédit / FX à couvrir | 🟢 | liability matching international | **OPPORTUNISTE** |
| 🌍 | **Gilts / autres souverains de haute qualité hedgés EUR** | Gilt 2036 : 5,04 % brut GBP vérifié | 🟢 crédit / FX à couvrir | 🟢 | si spread net EUR positif | **OPPORTUNISTE** |

### 2.2 Snapshot de taux vérifié

La colonne « différence » compare la donnée vérifiée au point de départ fourni pour cette politique. Une adjudication primaire n’est pas une cotation secondaire au 19 août : avant exécution, obtenir le prix et le YTM du jour sur la ligne exacte.

| Produit / source primaire | Date de la donnée | Échéance observée | Rendement publié | Nature / devise | Différence avec le point de départ |
| --- | --- | --- | ---: | --- | --- |
| [BTF — AFT, dernières adjudications](https://www.aft.gouv.fr/fr/dernieres-adjudications) | adjudication 17 août 2026 | 4 nov. 2026 à 11 août 2027 | 2,399–2,781 % | taux moyen pondéré, nominal EUR | borne basse -0,05 pt ; borne haute +0,04 pt |
| [EU-Bills — Commission européenne](https://commission.europa.eu/news-and-media/news/results-05-08-2026-auction-eu-bills-2026-08-05_en) | adjudication 5 août 2026 | 3, 6 et 12 mois | 2,400–2,704 % | taux moyen pondéré, nominal EUR | conforme à 2,4–2,7 % |
| [€STR — BCE](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_short-term_rate/html/index.en.html) | référence 10 août, publiée 11 août 2026 | overnight | 2,184 % | taux court EUR ; avant frais du fonds | conforme à ~2,2 % |
| [CAT — Banque de France](https://www.banque-france.fr/fr/statistiques/epargne/taux-de-remuneration-des-depots-bancaires-2026-06) | juin 2026 | nouveaux dépôts SNF ≤ 2 ans / > 2 ans | 2,45 % / 2,90 % | moyenne statistique nominale EUR, pas offre Fruits | précise la fourchette 2–3 % |
| [OAT moyen terme — AFT](https://www.aft.gouv.fr/fr/publications/communiques-presse/16-juillet-2026-emission-oat) | adjudication 16 juillet 2026 | sept. 2029 à nov. 2033 | 3,04–3,58 % | taux moyen pondéré, nominal EUR | conforme à 3–3,6 % |
| [OAT long terme — AFT](https://www.aft.gouv.fr/fr/dernieres-adjudications) | adjudication 6 août 2026 | mai 2036 à juin 2037 ; juin 2044 | 3,86–3,95 % ; 4,37 % | taux moyen pondéré, nominal EUR | ~10 ans conforme à ~3,9 % ; 2044 au-dessus |
| [OAT démembrées / STRIPS — AFT](https://www.aft.gouv.fr/fr/oat-demembrees-strips) | mécanisme consulté le 19 août 2026 | ISIN et date du flux à matcher | pas de YTM universel publié | zéro-coupon nominal EUR ; prix/YTM secondaire requis | 3–4 % conservé comme filtre, pas comme cotation vérifiée |
| [OATi / OAT€i — AFT](https://www.aft.gouv.fr/fr/publications/communiques-presse/16-juillet-2026-emission-oat-indexees) | adjudication 16 juillet 2026 | 2032, 2040 et 2053 | 1,81–2,29 % réel | réel + inflation de référence, EUR | conforme à 1,8–2,3 % réel |
| [EU-Bonds — Commission européenne](https://commission.europa.eu/news-and-media/news/results-13-07-2026-auction-eu-bonds-2026-07-13_en) | adjudication 13 juillet 2026 | juillet 2029 à juillet 2041 | 2,808–3,833 % | taux moyen pondéré, nominal EUR | borne haute inférieure à 4,2 % sur cet échantillon |
| [Bund/Bobl — Finanzagentur](https://www.deutsche-finanzagentur.de/fileadmin/user_upload/Institutionelle-investoren/auktionen/emissionsergebnisse_aktuell_en.pdf) | résultats au 12 août 2026 | 2031, 2036, 2038 et 2053 | 2,93 %, 3,13 %, 3,29 %, 3,65 % | rendement d’adjudication, nominal EUR | ~3 % confirmé sur 5–10 ans ; duration longue plus élevée |
| [ESM bills — ESM](https://www.esm.europa.eu/investors/esm-and-efsf/transactions) | adjudication 4 août 2026 | 3 mois | 2,421 % | nominal EUR | inférieur au départ 3–4,5 %, qui était trop large |
| [EFSF 5 ans — ESM](https://www.esm.europa.eu/investors/esm-and-efsf/efsf-raises-eu4-billion-sale-new-5-year-bond) | émission 24 février 2026 | février 2031 | 2,51 % | reoffer yield, nominal EUR | inférieur au départ 3–4,5 % ; cotation live requise |
| [Treasury curve — US Treasury](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve) | 18 août 2026 | 3 mois à 10 ans | 3,86–4,71 % | par yield, nominal USD, avant hedge | cohérent avec 4–5 % brut, pas en net EUR |
| [Gilt 2036 — UK DMO](https://www.dmo.gov.uk/media/aj0kvllf/160726conventional.pdf) | adjudication 16 juillet 2026 | 22 oct. 2036 | 5,040 % | rendement moyen, nominal GBP, avant hedge | chiffre désormais daté et qualifié |

### 2.3 Benchmarks non souverains et hypothèses de rendement

| Produit | Observation utilisée | Interprétation Fruits |
| --- | --- | --- |
| Covered bonds | [iBoxx EUR UK Covered](https://www.spglobal.com/spdji/en/indices/fixed-income/iboxx-eur-uk-covered) : YTM 3,31 %, maturité moyenne 4,17 ans au 5 août 2026 ; [iBoxx EUR dashboard](https://www.spglobal.com/spdji/en/documents/performance-reports/iboxx-eur-dashboard.pdf) : EUR Covered 3,23 % au 31 mars 2026 | benchmarks d’indices, pas rendement de toute obligation couverte ; comparer l’ISIN, la juridiction, le rang et le prix |
| Corporate IG EUR | iBoxx EUR Corporates : rendement 3,93 %, duration 4,40 au 31 mars 2026 | le filtre 3,5–5,5 % doit être confirmé ligne par ligne ; le haut de fourchette peut signaler plus de risque ou de duration |
| Bank senior / FRN / ETF à échéance | pas de taux unique représentatif | utiliser YTM/YTW, spread, rating, duration, frais, composition et liquidité du produit exact |
| ETF World | [Factsheet MSCI ACWI incluant le comparatif MSCI World](https://www.msci.com/documents/10199/a71b65b5-d0ea-4b5c-a709-24b1213bc3c5) : MSCI World, rendement net annualisé 10 ans 12,73 % USD et drawdown maximal historique 57,82 % au 31 juillet 2026 | **6–8 % est une hypothèse Fruits de rendement total long terme pour simulation, non garantie**, pas un rendement courant ni un coupon |
| Infrastructure, dette immobilière, private credit, REIT/SIIC, nouveaux deals | aucune valeur publique unique suffisamment comparable | objectifs internes de screening seulement ; exiger cash-flows, frais, défauts/pertes, valorisation, duration, levier et scénario downside propres au véhicule/deal |

## 3. Les quatre blocs Fruits

### 3.1 Fortress — « cet argent doit être disponible quand Fruits en a besoin »

**Mission :** servir les dettes vendeurs, ballons, crédits in fine, échéances connues, réserves stratégiques et besoins de trésorerie court/moyen terme. **Prévisibilité > rendement.**

Produits centraux : BTF, EU-Bills, CAT, monétaire EUR, OAT, STRIPS, OATi/OAT€i, EU-Bonds, Bund/souverains AAA EUR et dette supranationale.

Conditions :

- montant, devise et maturité appariés au passif ;
- absence d’actions et de FX non couvert ;
- duration limitée si une vente avant échéance est possible ;
- liquidité testée en stress et non déduite d’une simple cotation ;
- risque bancaire et plafond de garantie analysés pour les dépôts ;
- cash restreint, sûretés et droits aux coupons documentés.

### 3.2 Protection+ — améliorer sans prétendre supprimer le risque

Produits centraux sous limites : covered bonds, corporate IG, dette bancaire senior, FRN/CCTeu et ETF obligataires à échéance cible. Dette senior infrastructure/immobilier : V2 seulement, après track record, gouvernance crédit et analyse juridique.

Filtres minimaux proposés, à valider avant adoption :

- rating investment grade à l’achat (`BBB-/Baa3` ou équivalent au minimum), avec analyse interne et procédure de dégradation ;
- aucune dette subordonnée, AT1/CoCo, high yield ou CLO mezzanine ;
- échéance compatible avec le passif, sans compter sur une revente forcée ;
- diversification par émetteur, groupe bancaire, secteur, maturité et dépositaire ;
- documentation du rang, des clauses de bail-in, du call, du spread, de la duration, de la liquidité et de la perte attendue ;
- aucun véhicule illiquide dans une somme nécessaire à court/moyen terme.

### 3.3 Growth — faire croître le véritable surplus

**Growth liquide :** ETF World large et diversifié en priorité. Les infrastructures cotées et REIT/SIIC ne sont que des satellites optionnels. L’ETF peut subir une perte importante et durable au mauvais moment ; il ne sécurise aucun passif certain.

**Growth opérationnel :** nouveaux deals Fruits lorsque l’équipe détient un avantage réel de sourcing, structuration, rénovation, exploitation ou sortie.

> Fruits ne cherche pas nécessairement 10 % sur les marchés financiers. Le rendement à deux chiffres doit surtout être recherché là où Fruits possède un avantage opérationnel réel.

Avant d’arbitrer `100 k€ ETF World` contre `100 k€ de bouquet sur un nouveau deal Fruits`, comparer sur le même horizon :

| Critère | ETF World | Nouveau deal Fruits |
| --- | --- | --- |
| rendement | rendement total net attendu, non garanti | TRI net du bouquet et cash réellement encaissé |
| downside | drawdown actions et durée de récupération | vacance, travaux, dette, baisse de prix, contentieux et perte totale |
| liquidité | cotée, mais prix potentiellement dégradé | faible à nulle avant refinancement ou vente |
| levier | aucun par défaut ; Lombard séparé et plafonné | dette immobilière et garanties explicites |
| concentration | milliers de titres | un actif, une ville, un exploitant, un plan de sortie |
| travail | faible, gouvernance périodique | sourcing, exécution, exploitation et reporting |
| avantage Fruits | diversification passive | alpha opérationnel possible, à prouver |

### 3.4 International — seulement après conversion en net EUR

L’International obligataire n’est pas un bloc de diversification automatique. Il doit battre une alternative EUR de risque et de maturité comparables **après** couverture, frais, fiscalité, pertes attendues et complexité opérationnelle.

```text
rendement étranger brut
- coût du hedge FX
- frais produit, courtage, conservation et enveloppe
- fiscalité
- pertes de crédit attendues
= rendement net EUR

rendement net EUR
- coût total de la dette Fruits
= spread net Fruits
```

Une obligation US à 5 % ne se compare jamais directement à une OAT EUR à 4 %.

## 4. Actif ≠ enveloppe

### 4.1 CTO professionnel — enveloppe par défaut à étudier

Le compte-titres d’une société offre l’univers le plus large : obligations directes, OAT/STRIPS, ETF et titres internationaux, sous réserve de l’offre de l’intermédiaire, du KYC, de la comptabilité, de la fiscalité et des modalités de nantissement. L’[AMF décrit le CTO](https://www.amf-france.org/fr/espace-epargnants/comprendre-les-produits-financiers/supports-dinvestissement/compte-titres) comme pouvant accueillir actions, obligations, fonds et ETF.

### 4.2 Contrat de capitalisation — comparaison nette obligatoire

À étudier pour une holding, un patrimoine financier important, un horizon long et un éventuel nantissement. Le BOFiP envisage le cas d’une [personne morale soumise à l’IS détenant un contrat de capitalisation](https://bofip.impots.gouv.fr/bofip/3743-PGP.html/identifiant%3DBOI-RPPM-RCM-30-10-20-80-20120912), mais cela ne valide ni le contrat offert, ni son coût, ni son traitement comptable/fiscal dans le cas Fruits.

Ne jamais conclure qu’il est supérieur au CTO sans simulation nette de frais, fiscalité, valorisation et contraintes de sortie.

### 4.3 Assurance-vie luxembourgeoise — later-stage seulement

C’est une enveloppe, pas un placement. Elle peut avoir une utilité pour un patrimoine important, une architecture internationale, plusieurs gestionnaires ou un nantissement. L’éligibilité de la personne morale, le type de contrat, les actifs, le dépositaire, le triangle de sécurité, les coûts et les droits du créancier nanti doivent être confirmés par assureur et conseils. Comparaison systématique avec CTO et contrat de capitalisation.

### 4.4 PEA — patrimoine personnel, pas Fruits société

Le [PEA est réservé aux personnes physiques majeures fiscalement domiciliées en France](https://www.economie.gouv.fr/particuliers/gerer-mon-argent/gerer-mon-budget-et-mon-epargne/quest-ce-que-le-plan-depargne-en-actions-pea). Il ne constitue pas l’enveloppe de Fruits société. Il peut servir au patrimoine personnel d’un associé pour des ETF éligibles, sans mélange avec les actifs sociaux.

### 4.5 Comptes bancaires et CAT

Adaptés à la trésorerie et aux dates courtes, sous réserve de la solidité de la banque, de la disponibilité contractuelle et de la concentration. Le [FGDR](https://www.garantiedesdepots.fr/fr/connaitre-mes-garanties/je-detiens-des-comptes-et-des-livrets-bancaires-quelles-sont-mes-garanties) indique un plafond général de 100 000 € par client et par établissement pour les dépôts éligibles, y compris les comptes à terme ; l’éligibilité exacte de l’entité Fruits et de la banque doit être confirmée.

### 4.6 Matrice enveloppe × actif

`Selon contrat` signifie qu’aucune compatibilité ou nantissabilité n’est présumée. Il faut une confirmation écrite de l’établissement sur le produit et, si nécessaire, l’ISIN exact.

| Produit | CTO société | Contrat capi | AV Lux | PEA perso | Nantissable | Liquidité économique |
| --- | --- | --- | --- | --- | --- | --- |
| compte bancaire / CAT | hors CTO | hors contrat | support monétaire selon contrat | non | selon convention bancaire | immédiate à bloquée jusqu’au terme |
| BTF, OAT, STRIPS, EU-Bonds, Bund, supranational | oui selon intermédiaire/ISIN | selon contrat et unités disponibles | selon contrat | non | potentiellement, avec haircut contractuel | cotée ; risque de prix avant maturité |
| fonds monétaire EUR | oui selon fonds | selon contrat | selon contrat | non en principe | selon fonds et banque | généralement J/J+1, sans garantie absolue |
| covered / corporate IG / bank senior / FRN | oui selon intermédiaire/ISIN | selon contrat | selon contrat | non | selon rating, rang, ISIN et banque | variable ; spread possible en stress |
| ETF obligataire à échéance | oui selon ETF | selon contrat | selon contrat | généralement non | selon banque et ETF | cotée, valeur non garantie à la date cible |
| ETF World | oui selon ETF | selon contrat | selon contrat | oui seulement si ETF éligible | possible avec haircut élevé et appels de marge | cotée, mais forte volatilité possible |
| infrastructure / REIT-SIIC cotées | oui selon titre/fonds | selon contrat | selon contrat | seulement si éligible | selon banque | cotée, mais volatilité actions |
| dette privée / infrastructure / immobilier non cotée | selon véhicule et accès | rarement / selon contrat | selon architecture | non | rarement, décote forte possible | illiquide, fenêtres contractuelles |
| nouveau deal Fruits | participation ou prêt selon structure juridique | non en pratique | non en pratique | non | sûretés deal-specific, pas assimilables à un titre liquide | illiquide |

## 5. Allocation Fruits

### 5.1 Prérequis communs

Les trois modèles sont des **hypothèses de politique consolidée à tester**, jamais des pourcentages automatiques par SPV. Ils s’appliquent seulement après cantonnement de chaque passif, réserve, DSRA, fiscalité, CAPEX et cash restreint. Le comité documente l’entité propriétaire, l’origine des fonds et l’absence d’interdiction contractuelle.

| Modèle indicatif | Fortress | Protection+ | ETF World | Growth Fruits | Conditions |
| --- | ---: | ---: | ---: | ---: | --- |
| **Fruits prudent** | 55 % | 15 % | 20 % | 10 % | scénario de départ proposé |
| **Fruits équilibré** | 45 % | 20 % | 25 % | 10 % | seulement avec couverture et liquidité robustes |
| **Fruits mature** | 30 % | 20 % | 30 % | 20 % | hypothèse à tester après plusieurs années, 10–20 actifs, maturités diversifiées, absence de défaut, accès bancaire et couverture consolidée robuste |

Ces modèles ne modifient pas la règle antérieure : un passif certain prime toujours sur le pourcentage global. Une échéance importante peut imposer temporairement beaucoup plus de Fortress.

### 5.2 Allocation selon la dette vendeur

#### Fruits Zero

Priorité au STRIP/zéro-coupon dont le flux contractuel et la maturité correspondent au ballon. Pour `400 k€ dus en Y10` :

```text
capital théorique aujourd’hui = 400 000 / (1 + YTM net compatible)^10
```

À titre purement pédagogique, à 3,90 % annuel et avant frais/fiscalité, le montant serait proche de 272,8 k€. Le prix réel dépend de l’ISIN, du calendrier exact, de la courbe, du bid-ask, des frais, de la fiscalité et des clauses de nantissement. **Le surplus seulement** peut rejoindre Protection+ ou Growth.

#### Fruits Step

Construire une ladder : une ligne prudente arrive avant chaque échéance Y1, Y2, Y3, etc. Les coupons ou maturités ne sont comptés que s’ils sont juridiquement disponibles. Growth peut exister loin des paiements, puis diminue à mesure que leur date approche.

#### Fruits Balloon

Les paiements périodiques et le ballon exigent davantage de liquidité Fortress qu’un Zero parfaitement matché. Le calendrier est couvert échéance par échéance ; une valeur de portefeuille globale ne remplace pas un échéancier.

La documentation produit et les statuts Zero/Step/Balloon restent dans [Vente à terme / crédit vendeur — système Fruits](../04_Operationnel/12_Vente_A_Terme_Credit_Vendeur_Fruits.md).

### 5.3 Glide path dynamique

| Temps avant l’échéance | Positionnement |
| --- | --- |
| **> 10 ans** | Growth possible uniquement au-dessus d’un plan de financement crédible ; un STRIP matché peut verrouiller dès aujourd’hui le flux terminal |
| **5–10 ans** | réduction progressive des actifs volatils ; achats échelonnés de maturités Fortress correspondant au passif |
| **2–5 ans** | montant indispensable largement sécurisé ; aucun nouveau risque de marché ne doit créer un déficit de couverture |
| **< 2 ans** | couverture de 100 % du besoin après haircuts par cash, BTF/EU-Bills, CAT ou instruments Fortress courts arrivant avant paiement ; risque actions nul |

Indicateur central :

```text
couverture échéance
= valeur mobilisable après haircuts des actifs dédiés arrivant à temps
/ montant certain restant dû
```

Une valeur terminale contractuelle matchée peut être utilisée ; une performance future espérée d’ETF ne le peut pas.

## 6. Limites de risque et de concentration

Les chiffres ci-dessous sont des **limites initiales proposées à valider** avec banque, conseils et comité ; le plus petit plafond contractuel ou réglementaire l’emporte.

### Fortress

- 0 % actions, high yield, dette subordonnée ou FX non couvert ;
- maturité au plus tard à la date utile, avec marge opérationnelle ;
- CAT : rechercher la couverture FGDR éligible, sinon décision documentée sur l’excès ; diversifier les groupes bancaires ;
- souverains/supranationaux : diversifier si cela améliore le risque sans dégrader le matching ;
- pas de dépendance à une vente anticipée d’une obligation longue pour payer une échéance courte.

### Protection+

- corporate : cible maximale proposée de **5 % par émetteur**, plafond absolu à tester de 10 % ;
- banque : cible maximale proposée de **10 % par groupe bancaire**, plafond absolu à tester de 15 %, CAT et titres agrégés ;
- rating minimum proposé : investment grade `BBB-/Baa3` ou équivalent à l’achat ;
- aucune dette subordonnée, AT1/CoCo, high yield, CLO mezz/equity ;
- une dégradation sous le minimum déclenche une revue, pas une vente mécanique au pire moment ;
- limites sectorielles, de duration et d’illiquidité décidées avant l’ordre.

### Growth liquide

- ETF Monde large, transparent, liquide et à faibles frais comme brique principale ;
- stock picking, levier, options ou satellites concentrés non centraux ;
- tout Lombard est une décision de levier séparée : cible Fruits 20–25 %, maximum 30 % d’un portefeuille actions diversifié, sous réserve d’un stress d’appel de marge.

### Growth Fruits

- aucun nouveau bouquet si le deal détériore la couverture d’une dette existante ;
- concentration consolidée par actif, ville, exploitant, prêteur, millésime et stratégie mesurée avant engagement ;
- scénario de perte totale du bouquet et de retard de sortie supportable sans refinancement forcé.

## 7. Score Fruits

### 7.1 Méthode

Chaque actif reçoit une note de `1` (défavorable) à `5` (très favorable) sur 14 critères. La preuve et la date de chaque note sont conservées.

```text
Score / 100 = somme(note de 1 à 5 × poids) / 5
```

Un score élevé ne lève jamais un veto : illégalité, absence de prix fiable, FX interdit, mauvais matching, liquidité insuffisante, documentation absente ou exposition prohibée entraînent `NO-GO`.

| Critère | Poids Score Fortress | Poids Score Growth |
| --- | ---: | ---: |
| rendement net attendu | 3 | 22 |
| sécurité du capital | 18 | 6 |
| prévisibilité | 12 | 4 |
| liquidité | 10 | 8 |
| duration | 7 | 3 |
| compatibilité avec l’échéance | 18 | 3 |
| facilité de nantissement | 7 | 3 |
| haircut probable | 7 | 2 |
| frais | 4 | 7 |
| fiscalité | 2 | 6 |
| risque FX | 5 | 7 |
| simplicité opérationnelle | 4 | 6 |
| diversification | 2 | 14 |
| corrélation avec l’immobilier Fruits | 1 | 9 |
| **Total** | **100** | **100** |

### 7.2 Décision proposée

- score calculé dans la fonction réellement visée : on ne compare pas un STRIP au World avec le même score ;
- seuil indicatif d’étude approfondie : `70/100`, à valider après calibration sur des cas réels ;
- sous `60/100` : rejet par défaut ; entre `60` et `69` : exception motivée ;
- deux validations indépendantes pour toute exception, tout produit V2/V3 et tout collatéral d’une dette.

## 8. Règle FX

| Bloc | Politique Fruits |
| --- | --- |
| Fortress | risque FX non couvert **interdit par défaut** |
| Protection+ | FX non couvert **à éviter** ; exception écrite seulement si le passif est dans la même devise |
| Growth | FX possible pour diversification intentionnelle, horizon long, allocation plafonnée et risque explicitement accepté |
| International obligataire | uniquement si le rendement net après couverture EUR dépasse l’alternative EUR équivalente avec une marge suffisante pour la complexité, les frais et le basis risk |

Le coût de hedge est obtenu sur une cotation exécutable de même horizon. Les rolling hedges ajoutent risque de renouvellement, collatéral et basis ; ils ne sont pas assimilés à un coût fixe garanti jusqu’à l’échéance.

## 9. Nantissement et haircuts

Un actif « potentiellement nantissable » n’est pas un collatéral accepté. Avant de le compter :

1. identifier propriétaire, compte, créancier et sûreté ;
2. obtenir par écrit les ISIN/supports éligibles, haircuts et fréquence de valorisation ;
3. tester appels de marge, seuils, concentration, substitution et délai de cure ;
4. vérifier arbitrages, retraits, coupons/dividendes et intérêts libérables ;
5. documenter réalisation de la sûreté, rang, événement de défaut et droit applicable ;
6. stresser taux, spreads, actions, FX et liquidité simultanément ;
7. utiliser la valeur après haircut, jamais la seule valeur de marché.

Le nantissement de compte-titres financier relève notamment de l’[article L. 211-20 du Code monétaire et financier](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036175272/), mais l’efficacité de la sûreté et les droits économiques dépendent du contrat et du montage. Validation avocat/notaire/banque requise.

### 9.1 Retour bancaire SG du 20 août 2026 — portée limitée

- **Information confirmée par la conseillère SG :** le produit in fine décrit repose sur une poche dédiée, avec un exemple proche de 20 % au départ puis des versements réguliers vers une cible de remboursement.
- **Information confirmée par la conseillère SG :** une couverture proche de 100 % sur un support jugé sûr ou d'environ 130 % sur une poche plus risquée a été évoquée. Ce ne sont ni des ratios légaux ni des conditions SG universelles.
- **Information confirmée par la conseillère SG :** gains, retraits et arbitrages ne sont pas automatiquement libres. Le processus décrit nécessitait une demande, une levée temporaire, l'arbitrage puis la remise en nantissement.
- **Règle générale à vérifier :** support exact d'une SCI — compte-titres, contrat de capitalisation, assurance-vie d'un associé ou autre —, actifs éligibles, haircuts, valorisation, seuils, fréquence de test, procédure de cure et droits sur les revenus : **À confirmer avec SG**.
- **Hypothèse Fruits :** une allocation plus dynamique au début puis sécurisée avant le terme peut être testée, mais seulement sous les contraintes de couverture et d'arbitrage du contrat. Un ETF n'est pas automatiquement préférable à un fonds sécurisé.

Une surperformance ne constitue donc pas automatiquement du capital libre. Tant que le créancier n'a pas autorisé le retrait ou la substitution, elle reste dans le périmètre grevé.

Le nantissement conforte la garantie du prêteur, mais ne remplace pas la capacité de remboursement tirée des revenus, des réserves et d'un plan de remboursement soutenable.

## 10. KPI : rendement net Fruits et spread de dette

Pour chaque actif :

```text
rendement brut ou YTM/YTW
- frais produit
- frais enveloppe, courtage et conservation
- coût hedge FX
- fiscalité société
- perte de crédit attendue
= rendement net Fruits
```

Pour une somme liée à une dette :

```text
rendement net Fruits
- coût total de la dette
= spread net Fruits
```

Le coût total de dette inclut taux, commissions, frais de sûreté, surprix vendeur, coûts de hedge, covenants et valeur des options accordées. Un spread positif ne suffit pas si le principal peut manquer à la date due.

Pour un actif illiquide, ajouter au dossier une valeur actuelle nette, un TRI net, une perte attendue, un scénario de défaut/récupération et une prime minimale d’illiquidité. Ne jamais optimiser sur le rendement brut seul.

### 10.1 Next Deal Capital et capital preservation

La poche du prochain deal n'est pas obligatoirement 100 % cash. Deux méthodes restent ouvertes :

1. conserver le `Next Deal Capital` en cash ou monétaire très court ;
2. conserver une partie investie et financer raisonnablement une partie du bouquet par dette confirmée.

```text
Next Deal Capital =
cash libre
+ equity externe confirmée
+ dette bancaire / privée confirmée pour le bouquet

Acquisition Capacity =
Next Deal Capital
+ crédit vendeur signé
```

Le collatéral mobilisable n'est pas additionné une seconde fois : il peut augmenter la `borrowing base`, qui plafonne la dette, mais reste un actif grevé. La méthode 2 exige un spread net après coûts positif, une poche de remboursement, les seuils consolidés et un scénario viable sans refinancement obligatoire.

Si le portefeuille garantit déjà une dette vendeur, `valeur de marché du portefeuille` n'est pas synonyme de `capital libre`. Avant toute réutilisation, calculer haircuts, rangs, couverture, releases et portion réellement non nantie. Voir [Capital preservation + acquisition leverage](../04_Operationnel/12_Vente_A_Terme_Credit_Vendeur_Fruits.md#6-bis-capital-preservation--acquisition-leverage).

## 11. Waterfall et rémunération

Le portefeuille ne paie pas automatiquement les dirigeants. Ordre Fruits :

1. obligations et dettes exigibles ;
2. charges, fiscalité, CAPEX et réserves ;
3. couverture minimale et covenants ;
4. financement Growth approuvé ;
5. détermination du cash juridiquement et réellement distribuable ;
6. rémunération ou distribution valablement décidée.

Si le portefeuille est nanti, vérifier contractuellement coupons, dividendes, arbitrages, seuil de couverture, substitutions et retraits. `Rendement portefeuille` n’est jamais synonyme de `cash disponible dirigeant`. La politique de rémunération détaillée reste dans [Rémunération Fruits — waterfall](../04_Operationnel/11_Remuneration_Fruits_Waterfall.md).

## 12. Univers étudié mais exclu du portefeuille central Fruits

- crypto-actifs ;
- options spéculatives et stratégies à levier ;
- venture capital et private equity classique ;
- CLO mezzanine/equity, MBS/ABS complexes ;
- AT1, CoCos et preferred shares US ;
- structured notes complexes ;
- dette émergente en devise locale ;
- high yield concentré ;
- BDC et MLP ;
- commodities comme moteur de rendement et métaux précieux comme poche centrale ;
- hedge funds ;
- municipal bonds US.

> Ils ne présentent pas actuellement un couple simplicité / liquidité / prévisibilité / risque suffisamment intéressant pour l’architecture Fruits.

Ils ne sont pas déclarés intrinsèquement mauvais. Une réétude later-stage exige un besoin précis, un avantage net démontré, une compétence de contrôle et une décision explicite modifiant cette politique.

## 13. Checklist décisionnelle

Avant tout investissement Fruits :

- [ ] Quel passif cet argent doit-il couvrir, dans quelle entité et sous quel contrat ?
- [ ] À quelle date et dans quelle devise ?
- [ ] Quelle somme minimale doit être certaine ?
- [ ] Peut-on subir -20 % sans défaut, covenant breach ou vente forcée ?
- [ ] Quelle liquidité est requise en normal et en stress ?
- [ ] Quel prix, YTM/YTW ou TRI net est disponible aujourd’hui sur le produit exact ?
- [ ] Quels frais de produit, enveloppe, courtage, conservation et sortie ?
- [ ] Quelle fiscalité et quel traitement comptable ?
- [ ] Quel risque FX, quel coût et quelle durée de hedge ?
- [ ] L’actif peut-il être nanti par contrat, avec quel haircut et quels appels de marge ?
- [ ] Le rendement net dépasse-t-il le coût total de la dette avec une marge suffisante ?
- [ ] Existe-t-il un meilleur usage : remboursement, liquidité ou nouveau deal Fruits ?
- [ ] Que se passe-t-il si l’actif baisse, devient illiquide ou est dégradé au pire moment ?
- [ ] Les limites émetteur, banque, secteur, maturité, dépositaire et bloc restent-elles respectées ?
- [ ] Les validations comité, banque, comptable/fiscaliste et avocat/notaire nécessaires sont-elles écrites ?

> **Si une réponse essentielle est inconnue : NE PAS INVESTIR AVANT VALIDATION.**

## 14. Processus de décision et revue

1. classer la somme par passif et horizon ;
2. sélectionner le bloc, puis l’actif et l’enveloppe séparément ;
3. collecter prix, YTM/YTW, rating, duration, frais, fiscalité, liquidité et termes de nantissement ;
4. calculer rendement net Fruits, spread et scores adaptés ;
5. appliquer limites, stress et veto ;
6. obtenir les validations requises ;
7. consigner décision, taille, entité, motif, sources et conditions de sortie ;
8. suivre maturités, couverture, ratings, concentrations, covenants et droits sur le cash.

Revue immédiate en cas de nouvelle dette, nouvelle sûreté, baisse de couverture, dégradation de rating, modification fiscale/réglementaire, changement d’entité détentrice ou écart matériel au glide path.

## 15. Faits, hypothèses et décisions à ne pas mélanger

### Faits sourcés au 20 août 2026

- rendements d’adjudication et indices datés des tableaux ci-dessus ;
- le PEA n’est pas une enveloppe de société ;
- le CTO peut accueillir obligations, fonds et ETF ;
- la garantie des dépôts a un plafond général, mais son applicabilité exacte se vérifie ;
- les actions et obligations longues peuvent perdre de la valeur avant la date de besoin.
- Société Générale publie un prêt locatif in fine Optis adossé à une assurance-vie ; cela ne confirme pas l'enveloppe qui serait retenue pour une SCI Fruits.

### Hypothèses à tester

- allocations prudent/équilibré/mature ;
- plafonds 5/10 % corporate et 10/15 % bancaire ;
- seuils de score ;
- cibles de rendement non coté, Growth et nouveaux deals ;
- capacité réelle de nantissement et haircuts ;
- glide path deal par deal.
- ratios 20 % initial / 100–130 % de couverture, supports SCI, processus d'arbitrage et disponibilité de la surperformance évoqués lors du rendez-vous SG.

### Décisions déjà cohérentes avec le corpus Fruits

- aucune réserve risquée dans une SPV financée ;
- l’ETF actions appartient exclusivement à Growth ;
- la dette et les réserves précèdent distributions et rémunérations ;
- Zero reste expérimental ; Step et Balloon restent des recommandations conditionnelles ;
- aucune portabilité ou substitution de sûreté n’est supposée sans accord.

## 16. Sources et validations professionnelles

Sources de marché primaires et benchmarks : AFT, BCE, Banque de France, Commission européenne, German Finance Agency, ESM/EFSF, US Treasury, UK DMO, S&P DJI et MSCI — liens et dates dans les tableaux.

Sources de règles/enveloppes : AMF, economie.gouv.fr, BOFiP, FGDR et Légifrance — liens dans les sections concernées. Pour le risque ETF, voir aussi l’[AMF — trackers/ETF](https://www.amf-france.org/fr/espace-epargnants/comprendre-les-produits-financiers/placements-collectifs/trackers-etf). Pour le produit public étudié : [Société Générale — Prêt in fine Optis](https://particuliers.sg.fr/emprunter/pret-credit-immobilier/pret-in-fine-optis) et [informations générales Optis de novembre 2024](https://particuliers.sg.fr/static/Particuliers/Medias/Home/Banque/Credit-Immobilier/Pret_in_fine_Optis/Informations-generales-prets-OPTIS-11.2024.pdf). L'échange commercial du 20 août 2026 est une source distincte, non contraignante.

Avant exécution, faire valider selon le cas :

- **banque / dépositaire / assureur :** accès produits, prix, liquidité, haircuts, nantissement, covenants, coupons/retraits et appels de marge ;
- **expert-comptable et fiscaliste :** entité détentrice, impôt, valorisation, coupons, plus-values, change, contrat de capitalisation et déductibilité ;
- **avocat / notaire :** objet social, pouvoirs, fonds de tiers/FIA, sûretés, rang, portabilité, réalisation, distribution et conflits d’intérêts ;
- **conseil en investissement habilité si nécessaire :** adéquation produit, exécution, documentation et gouvernance.

## 17. Documents liés

- [Stratégie ETF — sous-politique Growth](03_Strategie_ETF.md)
- [Stratégies empilables](05_Strategies_Empilables.md)
- [Levier financier](../04_Operationnel/03_Levier_Financier.md)
- [Crédit in fine Fruits](../04_Operationnel/11_Credit_In_Fine_Fruits.md)
- [Vente à terme / crédit vendeur — système Fruits](../04_Operationnel/12_Vente_A_Terme_Credit_Vendeur_Fruits.md)
- [Rémunération Fruits — waterfall](../04_Operationnel/11_Remuneration_Fruits_Waterfall.md)
- [Checklist réflexe — investissement pré-décision](../04_Operationnel/checklists/investissement-pre-decision.md)
