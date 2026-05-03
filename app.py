"""
FrameCheck Streamlit app.

Run with:
    streamlit run app.py
"""

from __future__ import annotations

import pandas as pd
import streamlit as st

from analysis_engine import analyze_text, compare_texts


st.set_page_config(
    page_title="FrameCheck",
    page_icon="📰",
    layout="wide",
)


EXAMPLES = {
    "Choose an example": "",
    "High sensationalism": "SHOCKING: Radical leaders destroy the economy in devastating policy disaster!!!",
    "Medium framing": "Critics say new education policy could create serious problems for local schools",
    "Low framing": "City council approves new transportation budget after public hearing",
    "Weak sourcing example": "People are saying a secret cover-up caused the sudden collapse of the program",
}


def score_badge(score: int) -> str:
    if score >= 70:
        return "🔴"
    if score >= 40:
        return "🟠"
    if score >= 15:
        return "🟡"
    return "🟢"


def render_report(report: dict, label: str = "Analysis") -> None:
    score = int(report["score"])
    st.subheader(label)

    col1, col2, col3 = st.columns(3)
    col1.metric("Framing / sensationalism score", f"{score}/100")
    col2.metric("Risk label", f"{score_badge(score)} {report['risk_label']}")
    col3.metric("Word count", report["word_count"])

    st.progress(score / 100)

    st.markdown("### Flagged wording")
    flags = report["flags"]
    if flags:
        flag_rows = [
            {
                "Flagged term": item["term"],
                "Category": item["category"],
                "Weight": item["weight"],
                "Why it matters": item["explanation"],
            }
            for item in flags
        ]
        st.dataframe(pd.DataFrame(flag_rows), use_container_width=True, hide_index=True)
    else:
        st.success("No major loaded words from the project lexicon were detected.")

    if report["category_summary"]:
        st.markdown("### Framing fingerprint")
        summary_df = pd.DataFrame(
            [{"Category": key, "Points": value} for key, value in report["category_summary"].items()]
        ).set_index("Category")
        st.bar_chart(summary_df)

    if report["punctuation_notes"]:
        st.markdown("### Punctuation / style signals")
        for note in report["punctuation_notes"]:
            st.write(f"- {note}")

    st.markdown("### Neutral rewrite suggestion")
    st.info(report["neutral_rewrite"] or "No rewrite available yet.")

    with st.expander("Method note"):
        st.write(report["method_note"])
        st.write(
            "This project is intentionally transparent: the score comes from a visible list of loaded terms, "
            "punctuation patterns, and category weights. It should be used as a critical-reading aid, not as a truth detector."
        )


st.title("FrameCheck: News Bias and Sensationalism Detector")
st.caption("A lightweight INFOSCI 102 project for transparent media-literacy analysis.")

st.markdown(
    """
FrameCheck helps readers inspect how a headline or short article is framed.  
It does **not** decide whether something is true or false. Instead, it flags words and style patterns that may make a text feel emotional, partisan, exaggerated, or weakly sourced.
"""
)

single_tab, compare_tab, method_tab = st.tabs(["Analyze one text", "Compare two texts", "About the method"])

with single_tab:
    st.markdown("## Analyze one headline or paragraph")
    example_choice = st.selectbox("Try a sample input or write your own:", list(EXAMPLES.keys()))
    default_text = EXAMPLES[example_choice]
    user_text = st.text_area(
        "Enter a news headline or short paragraph:",
        value=default_text,
        height=140,
        placeholder="Example: Shocking policy disaster sparks outrage across the country!!!",
    )

    if st.button("Analyze text", type="primary"):
        report = analyze_text(user_text)
        if not user_text.strip():
            st.warning("Please enter text first.")
        else:
            render_report(report)

with compare_tab:
    st.markdown("## Compare framing across two versions")
    st.write("Use this when two headlines discuss the same event but use different wording.")

    col_a, col_b = st.columns(2)
    with col_a:
        text_a = st.text_area(
            "Text A",
            value="SHOCKING: Radical policy destroys local economy!!!",
            height=150,
        )
    with col_b:
        text_b = st.text_area(
            "Text B",
            value="New policy faces criticism over possible economic effects",
            height=150,
        )

    if st.button("Compare texts"):
        comparison = compare_texts(text_a, text_b)
        st.success(comparison["summary"])
        col1, col2 = st.columns(2)
        with col1:
            render_report(comparison["text_a"], "Text A")
        with col2:
            render_report(comparison["text_b"], "Text B")

with method_tab:
    st.markdown("## What makes this project original")
    st.write(
        "Most simple sentiment projects only say whether text is positive or negative. "
        "FrameCheck instead creates an explainable framing report: it shows the exact words, categories, score contribution, and a neutral rewrite."
    )

    st.markdown("## What the score means")
    st.write(
        "The score is based on a transparent rule system: loaded terms, punctuation/capitalization, and short-text adjustment. "
        "Because news truth is complex, the app avoids claiming that text is definitely biased or false."
    )

    st.markdown("## INFOSCI 102 concepts used")
    st.write(
        "The project uses strings, lists, dictionaries, loops, functions, conditionals, modules, data tables, and user interaction through a simple Python web app."
    )

    st.markdown("## Limitations")
    st.write(
        "FrameCheck can miss subtle bias and can flag words that are appropriate in some contexts. "
        "It should be treated as a media-literacy assistant, not an automated judge of truth."
    )
