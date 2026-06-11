---
type: project_strategy_branch
status: draft_to_validate
created: 2026-06-10
last_reviewed: 2026-06-10
project: Fruits
execution_status: deferred
tags: [#Fruits, #solar, #infrastructure, #investment, #digital_twin, #draft_to_validate]
---

# Branche d'investissement solaire

## Statut et garde-fou

Cette note conserve une branche potentielle de Fruits à reprendre plus tard.

- Statut : `draft_to_validate`.
- Ce n'est pas une décision d'exécution.
- La branche ne modifie pas la roadmap Fruits actuellement validée.
- La playlist, les pistes scientifiques et le prompt sont enregistrés, mais ne doivent pas être traités maintenant.
- La recherche documentaire, la collecte de données, la simulation et la construction du jumeau numérique commenceront uniquement après validation explicite de reprise.

## Objectif

Créer un modèle capable d'identifier automatiquement la configuration d'un parc solaire utility-scale maximisant :

- EBITDA ;
- TRI equity ;
- cash-out à la revente ;
- MWh produits ;
- MWh par hectare ;
- valeur de revente ;
- robustesse opérationnelle ;
- bancabilité.

Principe directeur :

> Maximiser la valeur nette créée par euro investi, et non la production brute.

## Thèse d'investissement à tester

La valeur ne viendrait pas seulement des panneaux, mais de la chaîne complète :

1. foncier ;
2. autorisations ;
3. raccordement ;
4. PPA ;
5. financement ;
6. construction ;
7. exploitation optimisée ;
8. revente.

Le solaire serait traité comme une opération de développement immobilier et une infrastructure énergétique.

## Stratégie cible à étudier

```text
Terrain
-> permis
-> raccordement
-> PPA
-> construction
-> 12-24 mois d'exploitation
-> revente
```

Acheteurs de sortie potentiels à vérifier :

- fonds infrastructure ;
- énergéticiens ;
- fonds de pension ;
- utilities.

## Variables à étudier

### Terrain

Variables :

- surface ;
- orientation ;
- pente ;
- altitude ;
- nature du sol ;
- coût foncier ;
- distance au raccordement ;
- disponibilité foncière.

KPIs :

- MW installables ;
- MWh/ha ;
- EBITDA/ha.

### Météo

Données historiques :

- irradiation directe et diffuse ;
- température ;
- vent ;
- humidité ;
- pluie ;
- poussière ;
- neige ;
- couverture nuageuse.

Granularités de simulation :

- horaire ;
- journalière ;
- saisonnière ;
- annuelle.

### Panneaux

Comparer monofacial et bifacial selon :

- rendement ;
- dégradation ;
- sensibilité à la température ;
- garantie ;
- bancabilité.

### Albédo et sol réfléchissant

Comparer :

- terre naturelle ;
- herbe ;
- gravier clair ;
- calcaire blanc ;
- géotextile réfléchissant ;
- membrane blanche ;
- béton clair.

Mesurer :

- coût ;
- durée de vie ;
- maintenance ;
- dégradation ;
- réflexion réelle ;
- salissure ;
- vieillissement ;
- poussière ;
- jaunissement ;
- déchirure ;
- remplacement ;
- albédo moyen réel après entretien et dégradation.

### Trackers

Comparer :

- fixe : CAPEX et OPEX faibles ;
- tracker 1 axe : gain potentiel de production à vérifier ;
- tracker 2 axes : production potentiellement supérieure, maintenance élevée.

Mesurer le gain réel, le coût réel et le ROI.

### Nettoyage

Comparer :

- manuel ;
- robot avec eau ;
- robot sans eau ;
- robot fixe ;
- robot autonome ;
- robot par rangée ;
- robot distribué.

Mesurer :

- énergie et eau consommées ;
- temps et coût de nettoyage ;
- maintenance ;
- usure des panneaux ;
- disponibilité.

Pour le bifacial, distinguer face avant et face arrière et calculer :

```text
gain bifacial brut
- coût de nettoyage
- coût de maintenance
= gain bifacial net
```

### Inspection et maintenance prédictive

Comparer inspection humaine, drone thermique et drone avec analyse IA selon :

- temps ;
- coût ;
- précision ;
- réduction de l'indisponibilité.

Cas d'usage IA à étudier :

- hotspots ;
- panneaux défaillants ;
- onduleurs ;
- trackers ;
- salissure ;
- optimisation du nettoyage ;
- maintenance prédictive ;
- disponibilité.

### Compatibilité technologique

Construire une matrice de compatibilité, notamment :

- tracker + robot ;
- tracker + bifacial ;
- vertical + robot ;
- vertical + nettoyage ;
- agrivoltaïque + robot.

Objectif : éliminer les configurations théoriquement performantes mais impossibles ou trop coûteuses à exploiter.

## Simulation envisagée

### Grid Search

Tester les combinaisons :

```text
pays
x terrain
x panneau
x sol
x tracker
x robot
x nettoyage
x financement
```

Sorties :

- production ;
- OPEX ;
- EBITDA ;
- TRI ;
- valeur de revente.

### Monte Carlo

Variables probabilistes initiales :

- météo ;
- poussière ;
- prix de l'électricité ;
- panne robot ;
- panne tracker ;
- panne onduleur ;
- coût de maintenance ;
- taux de dette.

Sorties :

- scénario pessimiste ;
- scénario central ;
- scénario optimiste.

## KPIs finaux envisagés

### Production

- MWh/an ;
- MWh/ha.

### Financiers

- EBITDA ;
- cash-flow ;
- TRI ;
- DSCR ;
- LCOE.

### Revente

- multiple EBITDA ;
- equity value ;
- cash-out.

### Exploitation

- disponibilité ;
- temps de maintenance ;
- temps de nettoyage.

## Vision à long terme

Créer un jumeau numérique capable de répondre :

> Pour ce terrain précis, dans ce pays précis, avec cette météo, quel design maximise la valeur nette créée et le cash-out à la revente ?

Le parc recherché ne serait pas nécessairement le plus gros, mais celui offrant le meilleur rendement du capital, la meilleure bancabilité, la meilleure valeur de sortie et le meilleur effet de levier.

## Sources de référence enregistrées, non traitées

### Playlist YouTube

- URL : https://youtube.com/playlist?list=PLdmGSEUW0sLLIjxj61BfLKXnzO7czeDh2&si=bpupIfnsbdDj6XS1
- Statut : `candidate_priority`
- Traitement : différé ; ne pas lancer Summarizer ou extraction avant reprise explicite.

### Pistes de littérature scientifique à retrouver et vérifier

Ces intitulés proviennent de la note source. Ils sont des pistes de recherche, pas encore des références bibliographiques validées.

| Domaine | Pistes à retrouver |
| --- | --- |
| Bifacial / albédia | `A Review of Bifacial Solar Photovoltaic Applications` ; `Value of Bifacial Photovoltaics Used with Highly Reflective Ground Materials` ; `Optimization of Rear-Side Energy Contribution in Bifacial PV Panels` |
| Trackers | `Review and Comparative Analysis of Solar Tracking Systems` |
| Soiling / nettoyage | `Effects of Soiling on Photovoltaic Modules` ; `PV Soiling Mitigation and Cleaning Techniques` |
| IA / maintenance prédictive | `AI-Based Predictive Maintenance of Solar Photovoltaic Systems` ; `AI Failure Detection and Diagnosis for Solar PV Systems` |
| Agrivoltaïsme | IEA PVPS, `Dual Land Use for Agriculture and Solar Power Production` ; `Agrivoltaic Engineering and Layout Optimization` |
| Land use | `Optimal Location for Constructing Solar PV Farms` ; `Solar Energy-Land Relationships Metrics` |
| CPV / miroirs | `What Went Wrong with CPV?` ; `Concentrated Photovoltaic Review` |

À la reprise, retrouver les références exactes, DOI, auteurs, dates, versions et liens primaires avant de les utiliser.

## Prompt différé

Le prompt suivant décrit le travail à faire plus tard. Il est conservé comme backlog et ne doit pas être exécuté maintenant.

```text
Objectif :

Construire un état de l'art mondial concernant l'optimisation des parcs photovoltaïques utility-scale.

Considérer toutes les langues (anglais, chinois, espagnol, allemand, japonais, coréen, français, portugais, italien, arabe).

Mission :

1. Identifier les meilleures vidéos YouTube, conférences, webinars, podcasts et présentations techniques.

2. Identifier les meilleurs papiers scientifiques, thèses, rapports industriels et publications gouvernementales.

3. Identifier les échecs, abandons technologiques, mauvaises pratiques et technologies non rentables.

4. Produire une cartographie complète des variables influençant :
   - production
   - rendement
   - CAPEX
   - OPEX
   - disponibilité
   - maintenance
   - bancabilité
   - valeur de revente

5. Identifier les paramètres nécessaires à la construction d'un jumeau numérique.

6. Identifier les modèles physiques existants :
   - bifacial
   - albedo
   - trackers
   - soiling
   - température
   - vieillissement
   - maintenance
   - robotique
   - IA

7. Identifier les datasets publics disponibles.

8. Identifier les simulateurs open-source ou académiques existants.

9. Construire une liste exhaustive des variables pour un Grid Search.

10. Construire une liste exhaustive des variables probabilistes pour une simulation Monte Carlo.

Requêtes à inclure à titre d'exemples uniquement :

"utility scale solar optimization"
"bifacial solar albedo"
"solar tracker ROI"
"solar farm cleaning robots"
"predictive maintenance photovoltaic"
"solar soiling losses"
"agrivoltaics economics"
"digital twin solar farm"
"solar farm O&M optimization"
"concentrated photovoltaics failure"

Ces requêtes servent uniquement de point de départ.
Elles ne sont pas exhaustives.
Explorer toutes les variantes pertinentes, synonymes, autres langues, autres juridictions et toute piste permettant d'identifier des informations supplémentaires, succès, échecs, comparables et meilleures pratiques.

Livrable final :

- Synthèse exécutive
- Base documentaire
- Liste des variables
- Modèle conceptuel du jumeau numérique
- Architecture Grid Search
- Architecture Monte Carlo
- Recommandations pour construire le simulateur Fruits
```

## Étapes quand le projet sera repris

### Étape 0 - Validation de reprise

- Confirmer que Fruits ouvre réellement cette branche.
- Définir le pays ou les juridictions prioritaires.
- Définir le budget temps, le niveau de profondeur et le livrable attendu.
- Décider si la branche reste une thèse d'investissement, devient une étude de faisabilité ou entre en roadmap.

### Étape 1 - Verrouiller la question d'investissement

- Définir le modèle économique cible : développement-revente, détention longue, ou comparaison des deux.
- Définir les contraintes de rendement, levier, bancabilité, calendrier et sortie.
- Séparer les hypothèses générales des règles propres à chaque pays.

### Étape 2 - Collecter et vérifier les sources

- Traiter la playlist YouTube avec le workflow Summarizer.
- Retrouver et vérifier les papiers scientifiques mentionnés.
- Ajouter sources primaires : IEA PVPS, NREL, organismes publics, publications académiques et documentation technique.
- Rechercher activement les échecs technologiques et les biais commerciaux.
- Classer chaque source par statut et provenance.

### Étape 3 - Construire l'état de l'art

- Cartographier variables physiques, économiques, opérationnelles et financières.
- Identifier modèles physiques, datasets et simulateurs existants.
- Construire la matrice de compatibilité technologique.
- Distinguer faits vérifiés, hypothèses, inférences et décisions.

### Étape 4 - Définir le modèle conceptuel

- Définir les entrées, équations, contraintes et sorties.
- Définir les KPI et règles de bancabilité.
- Définir le modèle de valeur de sortie.
- Documenter les hypothèses non observables et les validations nécessaires.

### Étape 5 - Prototyper

- Construire un modèle minimal sur un terrain et un pays.
- Valider les résultats contre des outils et cas réels.
- Ajouter progressivement Grid Search puis Monte Carlo.
- Ne pas industrialiser avant validation des équations et des données.

### Étape 6 - Tester la thèse d'investissement

- Comparer les configurations sur rendement du capital et robustesse, pas seulement sur production.
- Stress tester raccordement, PPA, prix, dette, dégradation, maintenance et sortie.
- Faire valider les hypothèses techniques, juridiques, réglementaires et financières avant décision d'exécution.

## Risques et validations nécessaires

- Les gains de production théoriques peuvent être annulés par CAPEX, OPEX, indisponibilité ou maintenance.
- Les titres de papiers scientifiques doivent être retrouvés et vérifiés.
- La playlist et les publications industrielles peuvent contenir des biais commerciaux.
- Le raccordement, les permis, le PPA, la fiscalité et la réglementation varient fortement par juridiction.
- La valeur de revente et la bancabilité doivent être testées avec des comparables et retours financeurs.
- Un jumeau numérique précis exige des données réelles et une validation des modèles physiques.
- Toute décision d'investissement nécessitera une revue technique, juridique, réglementaire, fiscale et financière externe.

## Décisions

Aucune décision d'exécution n'est prise dans cette note.
