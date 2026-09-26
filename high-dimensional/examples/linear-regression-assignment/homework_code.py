"""Assignment 1, Problems 8 and 9.
Run: python homework_code.py
Place Boston.csv and water.csv beside this script.
Dependencies: numpy pandas scipy statsmodels matplotlib.
water.csv comes from the CRAN alr4 package, data/water.rda.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
out = root / "results"
out.mkdir(exist_ok=True)

def fit(data, response, columns):
    X = sm.add_constant(data[columns])
    return sm.OLS(data[response], X).fit()

def coefficient_table(model):
    return pd.DataFrame({
        "Estimate": model.params, "SE": model.bse,
        "t": model.tvalues, "p": model.pvalues})

def vif_table(data, columns):
    X = sm.add_constant(data[columns]).to_numpy()
    values = [variance_inflation_factor(X, j + 1)
              for j in range(len(columns))]
    return pd.Series(values, index=columns, name="VIF")

def scatter_matrix(data, columns, filename):
    k = len(columns)
    fig, axes = plt.subplots(k, k, figsize=(8, 8))
    for i, row in enumerate(columns):
        for j, col in enumerate(columns):
            ax = axes[i, j]
            if i == j:
                ax.hist(data[row], bins=12, color="#83a9b2",
                        edgecolor="white")
            else:
                ax.scatter(data[col], data[row], s=10,
                           alpha=.6, color="#285566",
                           edgecolors="none")
            if i == k - 1:
                ax.set_xlabel(col, fontsize=10)
            if j == 0:
                ax.set_ylabel(row, fontsize=10)
            ax.tick_params(labelsize=7)
            ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(out / filename, dpi=220)
    plt.close(fig)

# Problem 8
water = pd.read_csv(root / "water.csv")
wcols = ["OPBPC", "OPRC", "OPSLAKE"]
assert water.shape[0] == 43
assert not water[wcols + ["BSAAM"]].isna().any().any()
wm = fit(water, "BSAAM", wcols)
wc = water[wcols + ["BSAAM"]].corr()
print("WATER CORRELATION\n", wc.round(4))
print(wm.summary())
wc.to_csv(out / "water_correlations.csv")
coefficient_table(wm).to_csv(out / "water_coefficients.csv")
scatter_matrix(water, wcols + ["BSAAM"], "water_matrix.png")

# Problem 9: keep the actual column name NX from the supplied CSV.
boston = pd.read_csv(root / "Boston.csv")
cols = boston.columns.drop("MEDV").tolist()
assert boston.shape == (506, 14)
assert not boston.isna().any().any()
models = {
    "Full": fit(boston, "MEDV", cols),
    "Drop TAX": fit(boston, "MEDV", [c for c in cols if c != "TAX"]),
    "Drop RAD": fit(boston, "MEDV", [c for c in cols if c != "RAD"])}
print("BOSTON FULL MODEL\n", models["Full"].summary())
coefficient_table(models["Full"]).to_csv(out / "boston_coefficients.csv")
scatter_matrix(boston, ["RM", "LSTAT", "PTRATIO", "MEDV"],
               "boston_matrix.png")
print("RAD-TAX correlation:", boston["RAD"].corr(boston["TAX"]))
rows, vifs = [], {}
for name, model in models.items():
    used = [c for c in model.params.index if c != "const"]
    vifs[name] = vif_table(boston, used)
    h = model.get_influence().hat_matrix_diag
    # Exact leave-one-out residual formula for a fixed OLS design.
    loo_rmse = np.sqrt(np.mean((model.resid / (1 - h)) ** 2))
    rows.append({"Model": name, "RSS": model.ssr,
                 "R2": model.rsquared, "Adjusted R2": model.rsquared_adj,
                 "RSE": np.sqrt(model.mse_resid),
                 "LOOCV RMSE": loo_rmse,
                 "Max VIF": vifs[name].max()})
comparison = pd.DataFrame(rows).set_index("Model")
vif_result = pd.DataFrame(vifs)
print("VIF\n", vif_result.round(3))
print("COMPARISON\n", comparison.round(4))
vif_result.to_csv(out / "boston_vif.csv")
comparison.to_csv(out / "boston_comparison.csv")
