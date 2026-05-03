# FrameCheck: News Bias and Sensationalism Detector

**Author:** Asilbek Amonov  
**Course:** INFOSCI 102 Final Project

FrameCheck is a lightweight Python web app that helps users inspect the framing of news headlines or short article text. The app does not decide whether a claim is true or false. Instead, it flags emotionally loaded, exaggerated, partisan, urgent, or weakly sourced language and explains why those words may affect how readers interpret a story.

## What I built

I built an interactive Streamlit application with two main modes:

1. **Analyze one text**: users paste a headline or short paragraph and receive a framing/sensationalism score, flagged words, category explanations, and a neutral rewrite suggestion.
2. **Compare two texts**: users paste two headlines about a similar topic and compare how differently they frame the same issue.

The original contribution is the **explainable framing fingerprint**: instead of only giving a vague score, FrameCheck shows the exact terms that influenced the score, what category each term belongs to, and why the term matters.

## Inputs and outputs

### Input examples

```text
SHOCKING: Radical leaders destroy the economy in devastating policy disaster!!!
```

```text
City council approves new transportation budget after public hearing
```

### Output examples

The app produces:

- framing / sensationalism score out of 100
- risk label
- flagged words and categories
- category bar chart
- punctuation/capitalization notes
- neutral rewrite suggestion

## How to run the project

### 1. Install Python

Tested target: Python 3.11 or newer.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit app

```bash
streamlit run app.py
```

The app should open in your browser at a local address such as:

```text
http://localhost:8501
```

## Files in this repository

```text
framecheck_project/
├── app.py                         # Streamlit web app
├── analysis_engine.py             # Core scoring and rewrite logic
├── requirements.txt               # Python dependencies
├── README.md                      # Short project overview and usage instructions
├── replication_ai_usage.md        # Full replication and AI disclosure document
├── demo_script.md                 # Suggested 4-7 minute demo video script
├── submission_checklist.md        # Final Canvas and Discussions checklist
├── sample_inputs.csv              # Example texts for testing/demo
└── tests/
    └── test_engine.py             # Basic unit tests for core logic
```

## Replication document

See [`replication_ai_usage.md`](replication_ai_usage.md) for full setup instructions, AI-use disclosure, prompt documentation, and limitations.
