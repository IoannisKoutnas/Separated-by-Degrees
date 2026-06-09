# Separated by Degrees: The "Greek Exception" in Political Polarization

### A Multivariate Inference Study on the Stabilizing Effect of Education in Greece vs. the EU

## 1. Project Overview

This project investigates the **"Stabilizer Hypothesis"** — the theory that higher educational attainment acts as a centrist anchor, pulling citizens toward political moderation. While international trends often show that education leads to "ideological sorting" (increased polarization), this study identifies **Greece** as a statistically significant outlier.

By applying **Multivariate OLS Regression** to the **European Social Survey (ESS) Round 10/11**, we move beyond simple data visualization to isolate the independent effect of human capital on social stability.

## 2. Key Findings: The "Greek Exception"

- **The Slope Reversal:** In the broader **EU Average**, education correlates with **increased** polarization (β = +0.0066). However, in **Greece**, the relationship is inverted; education correlates with **decreased** polarization (β = −0.0153).
- **Wealth Independence:** Using multivariate controls, we proved that the Greek moderating effect is driven by **Human Capital** (years of schooling) and is not merely a proxy for household income.
- **Statistical Outlier:** A Welch’s T-test (t = −4.86, p < 0.001) confirms that the polarization gap between Greece and the EU is not due to random chance.

## 3. The Analytical Pipeline

This project demonstrates an end-to-end data engineering and science workflow:

1. **Data Ingestion & Wrangling:** Processing raw Stata (`.dta`) files from the ESS, cleaning non-response codes, and standardizing cross-national variables.
2. **Feature Engineering:** Construction of the **Polarization Index** = |lrscale − 5|.
3. **Statistical Inference:** Welch’s T-Test + Multivariate OLS Regression (controlling for Income and Age).
4. **Model Diagnostics:** VIF analysis to ensure zero multicollinearity.

## 4. Interactive Dashboard

**Live Streamlit App** – Explore the results interactively:

- Executive summary and key metrics
- Polarization gap analysis (Welch’s t-test)
- Full multivariate OLS regression tables
- Side-by-side regression plots (Greece vs EU)
- Institutional trust correlations and VIF diagnostics
  
---

## 5. Technical Stack

- **Core Analysis:** Python (`Pandas`, `Statsmodels`, `SciPy`)
- **Visualization:** Seaborn + Matplotlib
- **Interactive Dashboard:** **Streamlit**
- **Original Work:** Jupyter Notebook

## 6. Strategic Recommendations

- Educational investment in Greece functions as **social cohesion infrastructure**.
- Policy approaches should be **context-aware** rather than one-size-fits-all.
- Educational attainment is a stronger predictor of long-term political stability than GDP per capita in the Mediterranean region.

## 7. Author & Portfolio Context

**Author:** **Ioannis Koutnas**  
**Role:** Data Analytics Portfolio Project  

This project was developed to demonstrate the application of **Inference-Oriented Analytics** to complex social problems. It highlights the ability to transform raw survey data into high-value strategic intelligence for NGOs, policymakers, and social risk analysts.
