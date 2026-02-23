# Separated by Degrees: The "Greek Exception" in Political Polarization

### A Multivariate Inference Study on the Stabilizing Effect of Education in Greece vs. the EU

## 1. Project Overview

This project investigates the **"Stabilizer Hypothesis"**—the theory that higher educational attainment acts as a centrist anchor, pulling citizens toward political moderation. While international trends often show that education leads to "ideological sorting" (increased polarization), this study identifies **Greece** as a statistically significant outlier.

By applying **Multivariate OLS Regression** to the **European Social Survey (ESS) Round 10/11**, we move beyond simple data visualization to isolate the independent effect of human capital on social stability.

## 2. Key Findings: The "Greek Exception"

* **The Slope Reversal:** In the broader **EU Average**, education correlates with **increased** polarization (β=+0.0066). However, in **Greece**, the relationship is inverted; education correlates with **decreased** polarization (β=−0.0153).
* **Wealth Independence:** Using multivariate controls, we proved that the Greek moderating effect is driven by **Human Capital** (years of schooling) and is not merely a proxy for household income.
* **Statistical Outlier:** A Welch’s T-test (t=−4.86, p<0.001) confirms that the polarization gap between Greece and the EU is not due to random chance.

## 3. The Analytical Pipeline

This project demonstrates an end-to-end data engineering and science workflow:

1. **Data Ingestion & Wrangling:** * Processing raw Stata (`.dta`) metadata from the ESS.
* Cleaning non-response codes (Refusals, "Don't Know") and standardizing cross-national variables.

2. **Feature Engineering:** * Construction of the **Polarization Index**: Index = ∣Self_Placement − 5∣.
3. **Statistical Inference:** * **Welch's T-Test:** To validate the regional gap under heteroscedastic conditions.
* **Multivariate OLS Regression:** Controlling for **Income** and **Age** to satisfy the *Ceteris Paribus* condition.

4. **Model Diagnostics:** * **VIF (Variance Inflation Factor)** analysis to ensure zero multicollinearity between education and wealth.

## 4. Technical Stack

* **Statistical Engine:** **Python** (`Pandas`, `Statsmodels`, `SciPy`) for the core econometric modeling.
* **Visualization:** **Seaborn** for deep-dive regression plots.
* **Documentation:** **Jupyter Notebook** for reproducible research.

## 5. Strategic Recommendations

* **Localized Stability Policies:** Educational investment in Greece should be viewed as a critical infrastructure for **Social Cohesion**, as it directly buffers against extremist drift.
* **Risk Modeling:** Analysts should prioritize **Educational Infrastructure** over **GDP per capita** when predicting long-term political stability in the Mediterranean region.

## 6. Author & Portfolio Context

**Author:** **Ioannis Koutnas** 
**Role:** Data Analytics Portfolio Project

**Context:** This project was developed to demonstrate the application of **Inference-Oriented Analytics** to complex social problems. It highlights the ability to transform raw survey data into high-value strategic intelligence for NGOs, policy-makers, and social risk analysts.

---