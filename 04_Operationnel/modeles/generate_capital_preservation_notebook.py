"""Génère le notebook auditable de la stratégie capital preservation Fruits."""

from pathlib import Path

import nbformat as nbf


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "01_Capital_Preservation_Multi_Deals.ipynb"


def markdown(text: str):
    return nbf.v4.new_markdown_cell(text.strip())


def code(text: str):
    return nbf.v4.new_code_cell(text.strip())


nb = nbf.v4.new_notebook()
nb["metadata"] = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    },
    "language_info": {"name": "python", "version": "3.9"},
}

nb["cells"] = [
    markdown(
        """
# Fruits — capital preservation + acquisition leverage

Notebook de contrôle pour la simulation Deal 1 → Deal 5. Il ne constitue ni une
recommandation d'investissement, ni une offre bancaire, ni une validation juridique.

**Question testée :** la dette bancaire utilisée pour une partie du bouquet conserve-t-elle
de la liquidité sans détruire la solvabilité consolidée ?

**Réponse du modèle pédagogique :** elle conserve de la liquidité brute, mais ajoute un
passif de même montant. À la date de closing, elle ne crée donc pas de NAV. Le montage ne
devient économiquement meilleur que si le spread net, le NOI et la création de valeur
compensent durablement les coûts, les risques et les sûretés supplémentaires.
"""
    ),
    markdown(
        """
## Périmètre et hypothèses

- Le point de départ est **post-monétisation réelle** du Deal 1 : 400 k€ de portefeuille
  et 400 k€ de dette vendeur. Aucun cash n'est réputé créé à l'achat.
- Pour isoler la mécanique demandée, le bien 1 est sorti du périmètre immobilier après
  une vente. Un refinancement/OBO devrait conserver le bien à l'actif **et** enregistrer
  toute nouvelle dette de cash-out ; ce cas exige un sources & uses distinct.
- Deals 2 à 5 : valeur 500 k€, bouquet 80 k€, nouveau crédit vendeur 420 k€.
- Stratégies A/B/C : respectivement 80/0, 40/40 et 20/60 k€ de Fruits/dette bancaire
  par nouveau deal.
- Cas central : vendeur 1,5 %, banque in fine 4 %, rendement net de portefeuille 5 %,
  NOI 30 k€ par actif et 10 ans. Ce sont des **hypothèses de travail**, pas des quotes.
- Le retour SG du 20 août 2026 est isolé dans une simulation de poche dédiée : **information
  confirmée par la conseillère SG** lorsqu'il restitue l'échange, **règle générale à vérifier**
  lorsqu'une term sheet ou un conseil doit confirmer, et **hypothèse Fruits** pour les rendements
  et scénarios. L'indication 4,15 % sur quinze ans n'est pas une offre ferme.
- Sont exclus du cas central : frais, fiscalité, assurance, coût de garantie/nantissement,
  hedge, travaux, distributions, principal remboursé et création de valeur. Leur exclusion
  rend le spread présenté optimiste.
- La dette vendeur de 400 k€ du Deal 1 est incluse dans tous les ratios consolidés.
"""
    ),
    code(
        """
from math import isclose
import numpy as np
import pandas as pd

pd.set_option("display.max_columns", 40)
pd.set_option("display.width", 180)
pd.options.display.float_format = "{:,.2f}".format

ASSUMPTIONS = {
    "opening_portfolio_k": 400.0,
    "opening_seller_debt_k": 400.0,
    "deal_value_k": 500.0,
    "bouquet_k": 80.0,
    "new_seller_debt_k": 420.0,
    "seller_rate": 0.015,
    "bank_rate": 0.04,
    "portfolio_return": 0.05,
    "noi_per_property_k": 30.0,
    "noi_stress_k": 24.0,
    "term_years": 10,
    "seller_coverage_target": 1.20,
}

SG_MEETING = {
    # Informations confirmées oralement par la conseillère SG, non contraignantes.
    "meeting_date": "2026-08-20",
    "indicative_rate": 0.0415,
    "indicative_term_years": 15,
    "debt_eur": 250_000.0,
    "illustrative_initial_ratio": 0.20,
    "coverage_ratios": (1.00, 1.10, 1.20, 1.30),
}

FRUITS_POCKET_HYPOTHESES = {
    # Hypothèse Fruits, non fournie ni garantie par SG.
    "net_return": 0.03,
}

STRATEGIES = {
    "A — 100% Fruits": {"fruits_k": 80.0, "bank_k": 0.0},
    "B — 50/50": {"fruits_k": 40.0, "bank_k": 40.0},
    "C — 25/75": {"fruits_k": 20.0, "bank_k": 60.0},
}

pd.concat({
    "Hypothèses modèle multi-deals": pd.Series(ASSUMPTIONS),
    "Retour SG non contraignant": pd.Series(SG_MEETING),
    "Hypothèses Fruits poche": pd.Series(FRUITS_POCKET_HYPOTHESES),
}, axis=0).to_frame("Valeur")
"""
    ),
    markdown(
        """
## Fonctions et contrôles

Le DSCR consolidé ci-dessous est volontairement sévère : le numérateur ne comprend que
le NOI des biens encore détenus, tandis que le dénominateur comprend les intérêts de toutes
les dettes vendeur, y compris les 400 k€ maintenus après la sortie du Deal 1. Un prêteur peut
retenir une définition contractuelle différente ; elle devra être rapprochée de ce calcul.
"""
    ),
    code(
        """
def annual_payment(principal_k, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = years * 12
    return principal_k * monthly_rate / (1 - (1 + monthly_rate) ** (-months)) * 12


def monthly_payment_eur(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = years * 12
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** (-months))


def safe_ratio(numerator, denominator):
    return np.nan if denominator <= 0 else numerator / denominator


def monthly_contribution_to_target(initial, target, annual_return, years):
    # Versement de fin de mois nécessaire pour atteindre target, sans frais ni impôt.
    months = years * 12
    if annual_return == 0:
        return (target - initial) / months
    monthly_return = annual_return / 12
    future_initial = initial * (1 + monthly_return) ** months
    annuity_factor = ((1 + monthly_return) ** months - 1) / monthly_return
    return (target - future_initial) / annuity_factor


def simulate_strategy(name, fruits_k, bank_k, portfolio_return=None, bank_rate=None, noi_k=None):
    p_return = ASSUMPTIONS["portfolio_return"] if portfolio_return is None else portfolio_return
    b_rate = ASSUMPTIONS["bank_rate"] if bank_rate is None else bank_rate
    noi_per_property = ASSUMPTIONS["noi_per_property_k"] if noi_k is None else noi_k
    rows = []
    for deal in range(1, 6):
        new_deals = deal - 1
        portfolio = ASSUMPTIONS["opening_portfolio_k"] - new_deals * fruits_k
        bank_debt = new_deals * bank_k
        seller_debt = ASSUMPTIONS["opening_seller_debt_k"] + new_deals * ASSUMPTIONS["new_seller_debt_k"]
        property_value = new_deals * ASSUMPTIONS["deal_value_k"]
        gross_assets = portfolio + property_value
        total_debt = seller_debt + bank_debt
        nav = gross_assets - total_debt
        noi = new_deals * noi_per_property
        seller_interest = seller_debt * ASSUMPTIONS["seller_rate"]
        bank_interest = bank_debt * b_rate
        debt_service = seller_interest + bank_interest
        portfolio_income = portfolio * p_return
        cash_flow = portfolio_income + noi - debt_service

        # Sans release/substitution du nantissement vendeur, le portefeuille n'est pas libre.
        seller_pledged_mv = min(max(portfolio, 0), ASSUMPTIONS["opening_seller_debt_k"])
        free_capital = 0.0 if seller_pledged_mv > 0 else max(portfolio, 0)
        seller_adjusted_coverage = seller_pledged_mv / ASSUMPTIONS["opening_seller_debt_k"]
        reusable_without_release = free_capital > 0
        net_debt = total_debt - free_capital
        next_deal_capital_scenario = free_capital + bank_k
        acquisition_capacity_scenario = next_deal_capital_scenario + ASSUMPTIONS["new_seller_debt_k"]

        rows.append({
            "Stratégie": name,
            "Deal": deal,
            "Portefeuille restant k€": portfolio,
            "Dette banque k€": bank_debt,
            "Dette vendeur k€": seller_debt,
            "Valeur immo k€": property_value,
            "Actifs bruts k€": gross_assets,
            "Dette totale k€": total_debt,
            "NAV / richesse nette k€": nav,
            "Revenu portefeuille k€": portfolio_income,
            "NOI k€": noi,
            "Intérêts k€": debt_service,
            "Cash-flow annuel k€": cash_flow,
            "DSCR consolidé x": safe_ratio(noi, debt_service),
            "Total Group Leverage": safe_ratio(total_debt, gross_assets),
            "Net Debt / NAV": safe_ratio(net_debt, nav),
            "Debt / Equity": safe_ratio(total_debt, nav),
            "Portefeuille nanti vendeur k€": seller_pledged_mv,
            "Portefeuille nanti banque k€": 0.0,
            "Capital libre réel k€": free_capital,
            "Next Deal Capital confirmé k€": free_capital,
            "Next Deal Capital scénarisé k€": next_deal_capital_scenario,
            "Acquisition Capacity scénarisée k€": acquisition_capacity_scenario,
            "Gap prochain actif k€": ASSUMPTIONS["deal_value_k"] - acquisition_capacity_scenario,
            "Couverture nominale Deal 1": seller_adjusted_coverage,
            "Réemploi sans release ?": "OUI" if reusable_without_release else "NON",
        })
    return pd.DataFrame(rows)


multi = pd.concat([
    simulate_strategy(name, values["fruits_k"], values["bank_k"])
    for name, values in STRATEGIES.items()
], ignore_index=True)

# Contrôles sources & uses et identité de bilan du modèle pédagogique.
for values in STRATEGIES.values():
    assert isclose(values["fruits_k"] + values["bank_k"] + ASSUMPTIONS["new_seller_debt_k"], ASSUMPTIONS["deal_value_k"])
assert np.allclose(multi["Actifs bruts k€"], multi["Dette totale k€"])
assert np.allclose(multi["NAV / richesse nette k€"], 0)
assert (multi["Portefeuille restant k€"] >= 0).all()

multi
"""
    ),
    markdown(
        """
## Résumé Deal 1 → Deal 5

Cette vue compacte répond à la comparaison de liquidité. Les 400/320/240/160/80 k€ de la
stratégie A et les trajectoires B/C supposent que chaque retrait a été juridiquement autorisé.
La colonne « capital libre réel » du tableau complet reste nulle lorsque le portefeuille est
déjà nanti au vendeur : l'arithmétique de liquidité n'est donc pas, à elle seule, une capacité
d'acquisition exécutable. `Acquisition Capacity scénarisée` ajoute la banque de la stratégie
et 420 k€ de vendeur pour le prochain actif ; elle reste une hypothèse, pas un engagement.
Le gap résiduel de 80/40/20 k€ doit venir d'une release ou d'une equity distincte.
"""
    ),
    code(
        """
summary_cols = [
    "Stratégie", "Deal", "Portefeuille restant k€", "Dette banque k€",
    "Dette vendeur k€", "Valeur immo k€", "NAV / richesse nette k€",
    "Cash-flow annuel k€", "DSCR consolidé x", "Total Group Leverage",
    "Net Debt / NAV", "Debt / Equity", "Capital libre réel k€",
    "Next Deal Capital confirmé k€", "Next Deal Capital scénarisé k€",
    "Acquisition Capacity scénarisée k€", "Gap prochain actif k€",
    "Réemploi sans release ?",
]
multi[summary_cols]
"""
    ),
    code(
        """
deal5 = multi[multi["Deal"] == 5][summary_cols].copy()
deal5
"""
    ),
    markdown(
        """
## Deal 2 — cas A à D et amortissable versus in fine

Le cas D retient ici l'extrémité prudente à tester (5 k€ Fruits, 75 k€ banque). Il reste
**EXPÉRIMENTAL**. La dette service consolidée comprend les 6 k€/an d'intérêts de la dette
vendeur du Deal 1, plus 6,3 k€/an du vendeur du Deal 2.
"""
    ),
    code(
        """
DEAL2_CASES = {
    "A": {"fruits_k": 80.0, "bank_k": 0.0},
    "B": {"fruits_k": 40.0, "bank_k": 40.0},
    "C": {"fruits_k": 20.0, "bank_k": 60.0},
    "D — endpoint expérimental": {"fruits_k": 5.0, "bank_k": 75.0},
}

deal2_rows = []
for case, values in DEAL2_CASES.items():
    bank = values["bank_k"]
    bank_interest = bank * ASSUMPTIONS["bank_rate"]
    bank_annuity = annual_payment(bank, ASSUMPTIONS["bank_rate"], ASSUMPTIONS["term_years"]) if bank else 0.0
    consolidated_seller_interest = (
        ASSUMPTIONS["opening_seller_debt_k"] + ASSUMPTIONS["new_seller_debt_k"]
    ) * ASSUMPTIONS["seller_rate"]
    ds_in_fine = consolidated_seller_interest + bank_interest
    ds_amort = consolidated_seller_interest + bank_annuity
    deal2_rows.append({
        "Cas": case,
        "Equity Fruits k€": values["fruits_k"],
        "Dette banque k€": bank,
        "Dette vendeur k€": ASSUMPTIONS["new_seller_debt_k"],
        "LTV dette totale Deal 2": (bank + ASSUMPTIONS["new_seller_debt_k"]) / ASSUMPTIONS["deal_value_k"],
        "Service dette in fine k€/an": ds_in_fine,
        "DSCR in fine — NOI 30": ASSUMPTIONS["noi_per_property_k"] / ds_in_fine,
        "DSCR in fine — NOI 24": ASSUMPTIONS["noi_stress_k"] / ds_in_fine,
        "Service dette amort. k€/an": ds_amort,
        "DSCR amort. — NOI 30": ASSUMPTIONS["noi_per_property_k"] / ds_amort,
        "DSCR amort. — NOI 24": ASSUMPTIONS["noi_stress_k"] / ds_amort,
        "Ballon banque final k€": bank,
    })

deal2 = pd.DataFrame(deal2_rows)
assert np.allclose(deal2["Equity Fruits k€"] + deal2["Dette banque k€"] + deal2["Dette vendeur k€"], 500)
deal2
"""
    ),
    markdown(
        """
## Retour bancaire SG — poche in fine de 250 k€

**Informations confirmées par la conseillère SG, sans offre ferme :** indication commerciale
d'environ 4,15 % sur quinze ans au 20 août 2026 ; exemple proche de 20 % versés initialement,
puis versements réguliers ; couverture évoquée proche de 100 % sur support sûr ou 130 % sur
une poche plus risquée. **Hypothèse Fruits :** rendement net régulier de 3 %, sans frais,
fiscalité ni volatilité.

La cible de 325 k€ à 130 % est une valeur finale de couverture dans le scénario, pas une somme
présumée présente au jour 1. La mensualité de poche est une sortie économique et l'actif reste
grevé même si la banque ne l'intègre pas à sa définition contractuelle du DSCR. On ne modifie
donc pas automatiquement le DSCR sans term sheet, mais on l'intègre au cash-flow économique.
"""
    ),
    code(
        """
sg_debt = SG_MEETING["debt_eur"]
sg_initial = sg_debt * SG_MEETING["illustrative_initial_ratio"]
sg_years = SG_MEETING["indicative_term_years"]
sg_return = FRUITS_POCKET_HYPOTHESES["net_return"]

pocket_rows = []
for ratio in SG_MEETING["coverage_ratios"]:
    target = sg_debt * ratio
    monthly_3 = monthly_contribution_to_target(sg_initial, target, sg_return, sg_years)
    monthly_0 = monthly_contribution_to_target(sg_initial, target, 0.0, sg_years)
    total_contributions_3 = sg_initial + monthly_3 * sg_years * 12
    pocket_rows.append({
        "Couverture cible": ratio,
        "Capital cible €": target,
        "Versement initial €": sg_initial,
        "Mensuel — hypothèse 3% €": monthly_3,
        "Mensuel — rendement 0% €": monthly_0,
        "Versements cash cumulés à 3% €": total_contributions_3,
        "Rendement cumulé implicite €": target - total_contributions_3,
        "Écart cible vs 100% €": target - sg_debt,
    })

in_fine_pocket = pd.DataFrame(pocket_rows)
assert np.allclose(in_fine_pocket["Capital cible €"], [250_000, 275_000, 300_000, 325_000])
assert isclose(in_fine_pocket.iloc[0]["Mensuel — hypothèse 3% €"], 756.16, abs_tol=0.01)
assert isclose(in_fine_pocket.iloc[-1]["Mensuel — hypothèse 3% €"], 1_086.60, abs_tol=0.01)
in_fine_pocket
"""
    ),
    markdown(
        """
**Règles générales à vérifier avec SG :** support exact en SCI (assurance-vie d'un associé,
contrat de capitalisation, CTO ou autre), garantie réelle/Crédit Logement, actifs éligibles,
haircuts ETF, valeur reconnue, fréquence des tests, remèdes en cas de `coverage shortfall`,
processus d'arbitrage et droits de retrait. Une sous-couverture n'est pas automatiquement un
« appel de marge » juridique : la qualification dépend du contrat.

```text
capital initial nanti + versements périodiques + rendement net = capital attendu
coverage ratio = valeur de marché du portefeuille / capital à couvrir
coverage shortfall = max(0, couverture contractuelle minimale - valeur reconnue)
```
"""
    ),
    markdown(
        """
## VEFA — intérêts payés ou capitalisés

Cas pédagogique : 250 k€, taux 3,40 %, chantier de dix-huit mois, appels simplifiés à
35 % aux mois 0–6, 70 % aux mois 6–12 et 95 % aux mois 12–18, puis amortissement sur vingt
ans après livraison. La conseillère SG a décrit deux options : paiement des intérêts
intercalaires avec l'assurance pendant le chantier, ou report/capitalisation des intérêts,
l'assurance restant au moins payée dans le montage évoqué. Les modalités exactes dépendent
de l'offre.
"""
    ),
    code(
        """
vefa_principal = 250_000.0
vefa_rate = 0.034
vefa_post_delivery_years = 20  # hypothèse Fruits
draw_periods = [(0.35, 6), (0.70, 6), (0.95, 6)]
interim_interest = sum(vefa_principal * draw * vefa_rate * months / 12 for draw, months in draw_periods)

paid_balance = vefa_principal
capitalized_balance = vefa_principal + interim_interest  # simplification sans capitalisation intra-période
paid_monthly = monthly_payment_eur(paid_balance, vefa_rate, vefa_post_delivery_years)
capitalized_monthly = monthly_payment_eur(capitalized_balance, vefa_rate, vefa_post_delivery_years)
paid_post_interest = paid_monthly * vefa_post_delivery_years * 12 - paid_balance
capitalized_post_interest = capitalized_monthly * vefa_post_delivery_years * 12 - capitalized_balance
paid_total_cost = interim_interest + paid_post_interest
capitalized_total_cost = interim_interest + capitalized_post_interest

vefa = pd.DataFrame([
    {
        "Scénario": "A — intérêts payés pendant le chantier",
        "Cash intérêts avant livraison €": interim_interest,
        "Solde amorti après livraison €": paid_balance,
        "Mensualité après livraison €": paid_monthly,
        "Coût total hors assurance €": paid_total_cost,
    },
    {
        "Scénario": "B — intérêts capitalisés (simplifié)",
        "Cash intérêts avant livraison €": 0.0,
        "Solde amorti après livraison €": capitalized_balance,
        "Mensualité après livraison €": capitalized_monthly,
        "Coût total hors assurance €": capitalized_total_cost,
    },
])
assert isclose(interim_interest, 8_500.0, abs_tol=0.01)
assert isclose(paid_monthly, 1_437.09, abs_tol=0.01)
assert isclose(capitalized_monthly, 1_485.95, abs_tol=0.01)
vefa
"""
    ),
    code(
        """
vefa_impact = pd.Series({
    "Liquidité pré-livraison préservée €": interim_interest,
    "Capital supplémentaire après livraison €": capitalized_balance - paid_balance,
    "Mensualité supplémentaire €": capitalized_monthly - paid_monthly,
    "Surcoût total simplifié €": capitalized_total_cost - paid_total_cost,
}, name="Impact option B vs A")
vefa_impact
"""
    ),
    markdown(
        """
## Spread de conservation du capital

Pour 60 k€ conservés à 5 % et 60 k€ empruntés à 4 %, le spread brut maximal est 0,6 k€/an.
Ce n'est pas encore le spread net : il faut retrancher frais, assurance, garantie, nantissement,
hedge, fiscalité et coût de la poche de remboursement. Le principal de 60 k€ n'est pas une
charge de résultat, mais il doit avoir une source de remboursement identifiée.
"""
    ),
    code(
        """
capital_preserved_k = 60.0
gross_spread = capital_preserved_k * (
    ASSUMPTIONS["portfolio_return"] - ASSUMPTIONS["bank_rate"]
)
spread = pd.DataFrame({
    "Élément": [
        "Rendement net portefeuille avant dette",
        "Intérêt bancaire",
        "Spread avant coûts annexes et fiscalité",
        "Coûts annexes + fiscalité + hedge + garantie",
        "Spread net après coûts",
    ],
    "Formule / valeur k€/an": [
        capital_preserved_k * ASSUMPTIONS["portfolio_return"],
        -capital_preserved_k * ASSUMPTIONS["bank_rate"],
        gross_spread,
        np.nan,
        np.nan,
    ],
})
spread
"""
    ),
    markdown(
        """
## Collatéral, haircuts et interdiction du double comptage

Les haircuts ci-dessous sont des **stress internes illustratifs**, pas des conditions bancaires
ni des valeurs réglementaires directement applicables au prêt Fruits. Une banque doit préciser
ses actifs éligibles, haircuts, fréquence de valorisation, seuils d'appel, droits de retrait et
rang. L'emprunt réellement disponible reste le minimum entre engagement approuvé, capacité
DSCR, capacité LTV et borrowing base après rangs prioritaires.
"""
    ),
    code(
        """
HAIRCUTS = {
    "Cash": 0.05,
    "Monétaire / BTF": 0.10,
    "OAT": 0.15,
    "Corporate IG": 0.25,
    "ETF World": 0.50,
}

collateral_rows = []
for asset, haircut in HAIRCUTS.items():
    for loan_k in (60.0,):
        collateral_rows.append({
            "Actif": asset,
            "Haircut stress": haircut,
            "MV requise pour 60 k€ de borrowing base": loan_k / (1 - haircut),
            "MV requise si couverture banque 120%": (loan_k * 1.20) / (1 - haircut),
        })
collateral = pd.DataFrame(collateral_rows)
collateral
"""
    ),
    code(
        """
seller_debt = ASSUMPTIONS["opening_seller_debt_k"]
portfolio = ASSUMPTIONS["opening_portfolio_k"]
coverage_target = ASSUMPTIONS["seller_coverage_target"]
seller_coverage = pd.DataFrame({
    "Test": [
        "Couverture nominale sans haircut",
        "Actif ajusté avec haircut interne 10%",
        "Actif ajusté requis à 120%",
        "Déficit de couverture ajustée",
        "Capital libre pour banque ou bouquet sans release",
    ],
    "Valeur": [
        portfolio / seller_debt,
        portfolio * 0.90,
        seller_debt * coverage_target,
        seller_debt * coverage_target - portfolio * 0.90,
        0.0,
    ],
    "Unité": ["x", "k€", "k€", "k€", "k€"],
})
seller_coverage
"""
    ),
    markdown(
        """
## Stress Deal 5

Les tests suivants montrent la sensibilité, non une distribution de probabilités. À NAV initiale
nulle dans ce modèle de closing, toute baisse non compensée rend la NAV négative. Cela révèle
une contradiction avec la cible senior prudente 55–65 % et impose un STOP tant qu'une vraie
marge d'equity, de réserves et de couverture n'a pas été démontrée.
"""
    ),
    code(
        """
rate_stress_rows = []
for strategy, values in STRATEGIES.items():
    for shock_bps in (0, 100, 200, 400):
        stressed = simulate_strategy(
            strategy,
            values["fruits_k"],
            values["bank_k"],
            bank_rate=ASSUMPTIONS["bank_rate"] + shock_bps / 10_000,
        )
        row = stressed[stressed["Deal"] == 5].iloc[0]
        rate_stress_rows.append({
            "Stratégie": strategy,
            "Choc taux bps": shock_bps,
            "Cash-flow D5 k€": row["Cash-flow annuel k€"],
            "DSCR D5 x": row["DSCR consolidé x"],
        })
rate_stress = pd.DataFrame(rate_stress_rows)
rate_stress
"""
    ),
    code(
        """
operating_stress_rows = []
for label, noi in {
    "NOI central": 30.0,
    "Loyer/NOI -20%": 24.0,
    "Vacance 6 mois (proxy -50%)": 15.0,
    "Vacance 12 mois (proxy -100%)": 0.0,
}.items():
    stressed = simulate_strategy("C — 25/75", 20.0, 60.0, noi_k=noi)
    row = stressed[stressed["Deal"] == 5].iloc[0]
    operating_stress_rows.append({
        "Stress": label,
        "NOI par actif k€": noi,
        "Cash-flow D5 k€": row["Cash-flow annuel k€"],
        "DSCR D5 x": row["DSCR consolidé x"],
    })
operating_stress = pd.DataFrame(operating_stress_rows)
operating_stress
"""
    ),
    code(
        """
valuation_rows = []
for strategy, values in STRATEGIES.items():
    base = simulate_strategy(strategy, values["fruits_k"], values["bank_k"])
    row = base[base["Deal"] == 5].iloc[0]
    for property_shock in (0.0, -0.10, -0.20):
        stressed_assets = row["Portefeuille restant k€"] + row["Valeur immo k€"] * (1 + property_shock)
        stressed_nav = stressed_assets - row["Dette totale k€"]
        valuation_rows.append({
            "Stratégie": strategy,
            "Choc valeur immo": property_shock,
            "NAV stress k€": stressed_nav,
            "Dette / actifs stress": row["Dette totale k€"] / stressed_assets,
        })
valuation_stress = pd.DataFrame(valuation_rows)
valuation_stress
"""
    ),
    code(
        """
portfolio_rows = []
for strategy, values in STRATEGIES.items():
    base = simulate_strategy(strategy, values["fruits_k"], values["bank_k"])
    row = base[base["Deal"] == 5].iloc[0]
    for shock in (0.0, -0.20, -0.30, -0.50):
        stressed_portfolio = row["Portefeuille restant k€"] * (1 + shock)
        stressed_nav = stressed_portfolio + row["Valeur immo k€"] - row["Dette totale k€"]
        portfolio_rows.append({
            "Stratégie": strategy,
            "Choc portefeuille": shock,
            "Perte k€": row["Portefeuille restant k€"] - stressed_portfolio,
            "NAV stress k€": stressed_nav,
        })
portfolio_stress = pd.DataFrame(portfolio_rows)
portfolio_stress
"""
    ),
    markdown(
        """
## Formules décisionnelles et STOP

```text
capital libre réel
= actifs liquides non grevés
- réserves obligatoires
- fiscalité exigible
- DSRA

borrowing base
= Σ[valeur de marché_i × (1 - haircut_i)]
- expositions garanties de rang supérieur

capacité banque
= min(engagement approuvé, capacité DSCR, capacité LTV, borrowing base)

Next Deal Capital
= cash libre + equity externe confirmée + dette bouquet confirmée

Acquisition Capacity
= Next Deal Capital + crédit vendeur signé

Total Group Leverage
= (banque + vendeurs + private debt + autres dettes) / actifs bruts ajustés

Net Debt / NAV
= (dette totale - cash non grevé - titres liquides non grevés mobilisables) / NAV
```

Si la NAV est nulle ou négative, `Net Debt / NAV` et `Debt / Equity` ne sont pas des ratios
interprétables : le modèle déclenche un **STOP**, pas un chiffre rassurant. STOP également si
DSCR stress < 1,20x, couverture vendeur insuffisante, maturités non financées, double
nantissement non documenté, ou refinancement futur obligatoire comme seule issue.
"""
    ),
    code(
        """
validation = {
    "sources_uses_all_cases": bool(np.allclose(
        deal2["Equity Fruits k€"] + deal2["Dette banque k€"] + deal2["Dette vendeur k€"], 500
    )),
    "closing_nav_identity": bool(np.allclose(multi["NAV / richesse nette k€"], 0)),
    "no_negative_portfolio": bool((multi["Portefeuille restant k€"] >= 0).all()),
    "deal2_D_amortizing_stress_above_1_20": bool(
        deal2.loc[deal2["Cas"] == "D — endpoint expérimental", "DSCR amort. — NOI 24"].iloc[0] >= 1.20
    ),
    "seller_coverage_120_met_with_400k_nominal": bool(portfolio >= seller_debt * coverage_target),
    "sg_pocket_targets_100_to_130_reconciled": bool(np.allclose(
        in_fine_pocket["Capital cible €"], [250_000, 275_000, 300_000, 325_000]
    )),
    "sg_20pct_initial_equals_50k": bool(isclose(sg_initial, 50_000.0)),
    "vefa_interim_interest_reconciled": bool(isclose(interim_interest, 8_500.0, abs_tol=0.01)),
    "vefa_capitalization_increases_total_cost": bool(capitalized_total_cost > paid_total_cost),
}
pd.Series(validation, name="Résultat")
"""
    ),
    markdown(
        """
## Limites et données à obtenir avant décision

1. Term sheet bancaire : taux all-in, amortissement/in fine, durée, frais, equity minimale,
   borrowing base, actifs éligibles, haircuts, appels de marge, covenants et rang.
2. Term sheet vendeur : maintien de créance après vente, substitution de sûreté, couverture,
   releases, rang/intercreditor et événements de défaut.
3. Modèle immobilier par deal : loyers, vacance, OPEX, CAPEX, travaux, impôts, frais de cession,
   valeur conservatrice, calendrier et scénarios sans refinancement.
4. Modèle fiscal et comptable : porteur de la dette, déductibilité, traitement des placements,
   plus-values, distributions et conventions intragroupe.
5. Sources de remboursement des ballons identifiées et ségréguées.
6. Confirmation SG écrite : emprunteur SCI, support nanti exact, caution/garantie réelle,
   Crédit Logement, ratios 20 % et 100–130 %, haircuts ETF, contrôle de couverture,
   arbitrages/retraits et conséquences d'une sous-performance.
7. Financement bancaire du bouquet et portabilité avancée de la dette vendeur : non validés
   lors de l'échange SG, à traiter comme hypothèses jusqu'aux accords bancaires et juridiques.

Le notebook ne valide donc aucune stratégie A/B/C/D. Il quantifie les conditions qui doivent
être satisfaites avant qu'une variante puisse passer de `EXPERIMENTAL` à `CORE`.
"""
    ),
]

nbf.write(nb, OUTPUT)
print(OUTPUT)
