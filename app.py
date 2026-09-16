import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

ASSETS = Path(__file__).parent / "assets"

st.set_page_config(
    page_title="Separated by Degrees",
    page_icon="🗳️",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {font-size: 40px; color: #1f2937; text-align: center; font-weight: 700;}
    .sub-header {font-size: 18px; color: #6b7280; text-align: center;}
    .section-title {font-size: 26px; color: #1f2937; font-weight: 600;}
</style>
""", unsafe_allow_html=True)

# ====================== SIDEBAR ======================
st.sidebar.title("🗳️ Separated by Degrees")
st.sidebar.caption("Education & Political Polarization — Greece vs. EU")
page = st.sidebar.radio("Go to:", [
    "🏠 Overview",
    "🧹 Data & Sample",
    "📊 Descriptive Statistics",
    "🧮 Regression Model",
    "🔁 Robustness Check",
    "🎯 Key Finding"
])

st.sidebar.markdown("---")
st.sidebar.caption("Author: Ioannis Koutnas · Junior Data Analyst")
st.sidebar.caption("Data: European Social Survey (ESS) Round 11")

# ====================== OVERVIEW ======================
if page == "🏠 Overview":
    st.markdown('<p class="main-header">Separated by Degrees</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">A Comparative Study of Educational Impact on Political '
        'Polarization in Greece and the EU</p>',
        unsafe_allow_html=True
    )
    st.caption("Testing the 'Stabilizer Hypothesis' using European Social Survey (ESS) Round 11 data")
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Pooled Sample (N)", "34,218")
    with col2:
        st.metric("Greece Sample (N)", "1,309")
    with col3:
        st.metric("Europe Comparison (N)", "32,909")
    with col4:
        st.metric("Interaction Effect (β₃)", "-0.0218", "p = 0.010")

    st.markdown("### The Research Question")
    st.info(
        "When people spend more years in school, does it change how extreme their "
        "political views are — and does education act differently in Greece than in "
        "the rest of Europe?"
    )

    col1, col2 = st.columns(2)
    with col1:
        st.success(
            "**In the Rest of Europe:** More years of education is linked to slightly "
            "*more* firm, distinct political positioning (β₁ = +0.0096)."
        )
    with col2:
        st.warning(
            "**In Greece:** Education acts as an ideological *stabilizer*. The interaction "
            "term flips the trend, producing a net negative slope of **-0.0072** — "
            "more schooling is associated with *less* political extremity."
        )

    st.markdown("### The Bottom Line")
    st.markdown(
        "In Greece, higher education appears to act as a bridge toward the political "
        "center rather than pushing people toward opposite political ends — a pattern "
        "not observed in the rest of the European comparison group."
    )

# ====================== DATA & SAMPLE ======================
elif page == "🧹 Data & Sample":
    st.title("🧹 Data & Sample Construction")

    st.markdown("#### Pipeline")
    st.markdown(
        "- **Source:** ESS Round 11 raw Stata file, ingested with `convert_categoricals=False` "
        "to preserve numeric missing-value codes (e.g. `77`, `88`, `99`).\n"
        "- **Outcome variable:** `ideological_extremity` = |`lrscale` − 5|, the absolute "
        "distance from the ideological center on the 0–10 left–right scale.\n"
        "- **Key predictor:** `eduyrs` (years of formal education).\n"
        "- **Controls:** household income decile (`hinctnta`), age (`agea`).\n"
        "- **Groups:** Greece (`cntry == 'GR'`) vs. all other European countries (comparison group)."
    )

    st.markdown("### Sample Attrition & Retention")
    retention_df = pd.DataFrame({
        "Analytical Group": ["Greece (GR)", "Europe (Non-GR)"],
        "Initial Sample (N)": [2757, 47359],
        "Complete-Case Sample (N)": [1309, 32909],
        "Dropped": [1448, 14450],
        "Missingness %": ["52.52%", "30.51%"],
        "Retention Rate": ["47.48%", "69.49%"]
    })
    st.dataframe(retention_df, use_container_width=True, hide_index=True)

    st.caption(
        "A drop of over half the Greek sample warranted a data-hygiene check — "
        "see the item-nonresponse audit below."
    )

    st.markdown("### Item-Nonresponse Breakdown (Greece Raw Sample, N = 2,757)")
    missing_df = pd.DataFrame({
        "Variable": ["hinctnta", "ideological_extremity (lrscale)", "eduyrs", "agea", "anweight"],
        "Missingness Rate": ["46.97%", "14.83%", "0.47%", "0.07%", "0.00%"],
        "Conceptual Domain": [
            "Household Income Decile", "Left–Right Ideology", "Education Years",
            "Respondent Age", "ESS Analysis Weight"
        ],
        "Primary Driver": [
            "Refusal / 'Don't know' on sensitive financial items",
            "Non-placement on the 0–10 scale",
            "Minimal non-response on objective demographic items",
            "Minimal non-response on objective demographic items",
            "Complete coverage across all completed interviews"
        ]
    })
    st.dataframe(missing_df, use_container_width=True, hide_index=True)

    st.error(
        "**Household income (`hinctnta`) is the primary bottleneck** — almost half of "
        "Greek respondents (46.97%) declined to report income, which almost single-handedly "
        "drives the 52.52% total sample drop. This is why Stage 7 re-runs the model without "
        "the income control, as a robustness check."
    )

# ====================== DESCRIPTIVE STATISTICS ======================
elif page == "📊 Descriptive Statistics":
    st.title("📊 Weighted Descriptive Statistics")
    st.caption("Population-representative statistics using the ESS analysis weight (anweight)")

    stats_df = pd.DataFrame({
        "Metric": ["Ideological Extremity Mean", "Ideological Extremity SE",
                   "Years of Education Mean", "Years of Education SE"],
        "Greece (GR)": [1.513, 0.042, 12.235, 0.139],
        "European Comparison Group": [1.638, 0.015, 13.669, 0.041],
        "Point Difference (Δ)": [-0.125, "—", -1.434, "—"]
    })
    st.dataframe(stats_df, use_container_width=True, hide_index=True)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Extremity Gap (GR − EU)", "-0.125", "Greece less extreme")
    with col2:
        st.metric("Education Gap (GR − EU)", "-1.434 yrs", "Greece less educated")

    st.markdown("#### Supplementary Welch's t-test (Ideological Extremity)")
    c1, c2 = st.columns(2)
    c1.metric("T-Statistic", "-4.862")
    c2.metric("P-Value", "< 0.001")
    st.caption("The difference in ideological extremity between Greece and the European comparison group is statistically significant.")

    st.markdown("---")
    st.markdown("### Figure 1: Weighted Density Distribution of Ideological Extremity")
    st.image(str("density_plot.png"), use_container_width=True)
    st.markdown(
        "- Both distributions show sharp peaks at integer values (0–5), a byproduct of "
        "`lrscale` being measured on an integer 0–10 scale.\n"
        "- The **European comparison group** has a notably higher peak at pure centrism "
        "(≈0.52 vs. ≈0.36 for Greece).\n"
        "- **Greece** shows fatter density at intermediate extremity levels (1–2), suggesting "
        "Greek respondents cluster moderately close to the center rather than at the poles."
    )

    st.markdown("### Figure 2: Education vs. Ideological Extremity (Bivariate Trend)")
    st.image(str("bivariate_plot.png"), use_container_width=True)
    st.markdown(
        "The raw linear trends already hint at the core finding: Greece's trend line "
        "slopes **downward** with more years of education, while Europe's trend line "
        "slopes **upward** — this divergence is what the regression model in the next "
        "section formally tests."
    )

# ====================== REGRESSION MODEL ======================
elif page == "🧮 Regression Model":
    st.title("🧮 Pooled Interaction Model")
    st.caption("OLS Regression with Heteroskedasticity-Consistent Robust Standard Errors (HC1)")

    st.markdown(
        "All complete-case respondents (**N = 34,218**) were pooled into a single OLS model "
        "predicting `ideological_extremity`, with an interaction term (`eduyrs × is_greece`) "
        "testing whether the effect of education differs between Greece and the rest of Europe."
    )

    reg_df = pd.DataFrame({
        "Predictor": ["const (β₀)", "eduyrs (β₁)", "is_greece (β₂)",
                      "eduyrs_x_greece (β₃)", "hinctnta (β₄)", "agea (β₅)"],
        "Coefficient": [1.3208, 0.0065, 0.1023, -0.0218, 0.0107, 0.0038],
        "Std Error": [0.046, 0.002, 0.112, 0.008, 0.003, 0.000],
        "z-statistic": [28.641, 2.838, 0.912, -2.593, 3.091, 7.762],
        "p-value": ["< 0.001", "0.005", "0.362", "0.010", "0.002", "< 0.001"],
        "95% CI": ["[1.230, 1.411]", "[0.002, 0.011]", "[-0.118, 0.322]",
                   "[-0.038, -0.005]", "[0.004, 0.017]", "[0.003, 0.005]"]
    })
    st.dataframe(reg_df, use_container_width=True, hide_index=True)

    st.markdown("### Interpreting the Coefficients")

    with st.expander("📈 Education in the Rest of Europe — eduyrs = +0.0065", expanded=True):
        st.write(
            "Across the European baseline, each extra year of schooling is tied to a small "
            "*increase* in political extremity. In most European countries, more education is "
            "linked to holding a more firm, distinct political position — not necessarily a more moderate one."
        )

    with st.expander("🇬🇷 The Greek Interaction Effect — eduyrs_x_greece = -0.0218 (p = 0.010)", expanded=True):
        st.write(
            "This is the key result. It is negative and statistically significant, meaning the "
            "slope of education's effect on extremity is significantly *more negative* in Greece "
            "than in the rest of Europe. Combined with the Europe baseline slope, the **net effect "
            "of education in Greece is -0.0072** — extra schooling pulls Greek respondents "
            "*toward* the political center."
        )

    with st.expander("⚖️ Baseline Country Difference — is_greece = +0.1023 (p = 0.362)", expanded=False):
        st.write(
            "Not statistically significant. This means Greeks are not inherently more or less "
            "politically extreme than the rest of Europe at baseline (zero years of education) — "
            "the divergence emerges specifically *through* education."
        )

    with st.expander("💰 Controls — hinctnta & agea", expanded=False):
        st.write(
            "Both household income (β₄ = +0.0107, p = 0.002) and age (β₅ = +0.0038, p < 0.001) "
            "are positively and significantly associated with ideological extremity, "
            "independent of education and country."
        )

# ====================== ROBUSTNESS CHECK ======================
elif page == "🔁 Robustness Check":
    st.title("🔁 Stage 7: Sensitivity & Robustness Audit")

    st.markdown(
        "Because household income (`hinctnta`) had **46.97% missingness in Greece**, the main "
        "model in Stage 6 excluded a large share of Greek respondents. This check re-runs the "
        "model **without** the income control to see if the finding survives."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Model 1: Full Sample (no income control)", "N = 41,745")
        st.caption("Greek N restored to 2,341 (+1,032 respondents)")
    with col2:
        st.metric("Model 2: Restricted (with income control)", "N = 34,218")
        st.caption("Greek N = 1,309 — this is the Stage 6 model")

    robust_df = pd.DataFrame({
        "Parameter": ["const", "eduyrs (β₁)", "is_greece (β₂)", "eduyrs_x_greece (β₃)",
                      "agea (β₅)", "hinctnta (β₄)"],
        "Model 1: Full Sample (N=41,745)": [
            "1.32698 (p < 0.001)", "0.00961 (p < 0.001)", "0.10863 (p = 0.252)",
            "-0.01683 (p = 0.019)", "0.00378 (p < 0.001)", "Omitted"
        ],
        "Model 2: Restricted (N=34,218)": [
            "1.32075 (p < 0.001)", "0.00645 (p = 0.005)", "0.10234 (p = 0.362)",
            "-0.02180 (p = 0.010)", "0.00383 (p < 0.001)", "0.01070 (p = 0.002)"
        ]
    })
    st.dataframe(robust_df, use_container_width=True, hide_index=True)

    st.success(
        "**The Greek education effect holds up.** In both models, the interaction term "
        "(eduyrs_x_greece) stays negative and statistically significant "
        "(β₃ = -0.01683, p = 0.019 in Model 1 vs. -0.02180, p = 0.010 in Model 2). "
        "Whether using the smaller income-reporting group or the full 41,745-person sample, "
        "more education in Greece consistently pulls people away from political extremes."
    )

    st.markdown(
        "- **Education in the rest of Europe** stays positive across both specifications "
        "(β₁ = +0.00961 vs. +0.00645) — education does not act as a moderating force there.\n"
        "- **Baseline country difference** (`is_greece`) is not statistically significant in "
        "either model (p = 0.252 and p = 0.362) — Greeks are not inherently more or less "
        "extreme absent the education effect."
    )

# ====================== KEY FINDING ======================
elif page == "🎯 Key Finding":
    st.title("🎯 The Stabilizer Hypothesis")

    st.markdown(
        "Combining the pooled model's coefficients into predicted ideological-extremity "
        "lines (holding age at its sample mean, ~50 years) makes the divergence visible directly."
    )

    # Recreate the notebook's final chart exactly from the model's own coefficients
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))

    edu_years = np.linspace(4, 20, 100)

    b0 = 1.32698
    b1 = 0.00961
    b2 = 0.10863
    b3 = -0.01683
    b5_mean = 0.00378 * 50

    y_europe = (b0 + b5_mean) + (b1 * edu_years)
    y_greece = (b0 + b2 + b5_mean) + ((b1 + b3) * edu_years)

    ax.plot(edu_years, y_europe, color="#1f77b4", linewidth=2.5,
            label="Rest of Europe (Positive Slope: β = +0.0096)")
    ax.plot(edu_years, y_greece, color="#d62728", linewidth=2.5, linestyle="--",
            label="Greece (Stabilizing Slope: Net β = -0.0072)")

    ax.set_title("The Stabilizer Hypothesis: Education vs. Ideological Extremity",
                 fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Years of Education (eduyrs)", fontsize=11)
    ax.set_ylabel("Predicted Ideological Extremity", fontsize=11)
    ax.legend(loc="upper right", frameon=True)
    ax.annotate(
        "Higher Education Reduces\nExtremity in Greece",
        xy=(15.2, 1.51), xytext=(11.5, 1.40),
        fontsize=10, fontweight="bold", color="#d62728",
        ha="center",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#d62728", lw=1.5),
        arrowprops=dict(arrowstyle="->", color="#d62728", lw=1.5)
    )

    st.pyplot(fig)

    st.markdown("---")
    st.markdown("### Why We Can Trust This Result")
    st.markdown(
        "1. **The missing income check (Stage 7):** the effect survives with and without "
        "the income control, and with the full restored Greek sample.\n"
        "2. **Robust standard errors (HC1):** the model uses heteroskedasticity-consistent "
        "standard errors, guarding against unequal variance across groups.\n"
        "3. **A statistically significant interaction term:** the Greece-specific slope "
        "difference is not attributable to chance (p = 0.010)."
    )

    st.markdown("### Takeaway")
    st.info(
        "In the rest of Europe, more schooling is linked to slightly firmer political "
        "positioning. In **Greece**, education works in the opposite direction — each "
        "additional year of schooling is associated with **lower** political extremity, "
        "consistent with education acting as an ideological stabilizer rather than a "
        "polarizing force."
    )

# ====================== FOOTER ======================
st.markdown("---")
st.caption("🗳️ Separated by Degrees | Data: European Social Survey (ESS) Round 11 | Built with Streamlit")
