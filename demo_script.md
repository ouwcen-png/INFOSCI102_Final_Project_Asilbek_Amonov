# Demo Video Script, 4-7 Minutes

## 0:00-0:40 — Introduction

Hi, my name is Asilbek Amonov, and my final project is called **FrameCheck: News Bias and Sensationalism Detector**.

The purpose of this project is to help everyday readers notice how news headlines or short article text may be framed. The app does not decide whether something is absolutely true or false. Instead, it highlights emotionally loaded language, exaggeration, political framing, weak sourcing, and clickbait-style wording.

I built this because people often react to news based on wording before they evaluate evidence. My goal was to create a simple media-literacy tool that makes those wording choices visible.

## 0:40-1:30 — Show the app

Here is the Streamlit app. It has three main sections:

1. Analyze one text
2. Compare two texts
3. About the method

I chose Streamlit because it lets me turn Python code into a simple browser-based app without needing a complex web development setup.

## 1:30-2:40 — Demo: analyze one headline

Now I will enter a loaded headline:

```text
SHOCKING: Radical leaders destroy the economy in devastating policy disaster!!!
```

When I click **Analyze text**, the app gives a framing and sensationalism score out of 100. It also gives a risk label.

Below that, the app shows the specific flagged words. For example, it flags words like `SHOCKING`, `Radical`, `destroy`, `devastating`, and `disaster`. Each term is assigned a category, such as emotional language or political framing, and the app explains why that word may affect the reader.

This is important because the app is not just giving a mysterious score. It shows exactly what caused the score.

## 2:40-3:30 — Explain the framing fingerprint and rewrite

The app also creates a framing fingerprint. This chart shows which categories contributed most to the score.

Then the app gives a neutral rewrite suggestion. The rewrite does not claim to be perfect, but it shows how the same idea could be written in less emotionally charged language.

This is one of the original parts of my project. Instead of only saying “this is biased,” the app helps the user learn how wording changes framing.

## 3:30-4:30 — Demo: compare two headlines

Next, I will use the comparison tab.

Text A:

```text
SHOCKING: Radical policy destroys local economy!!!
```

Text B:

```text
New policy faces criticism over possible economic effects
```

Both headlines could refer to a similar issue, but they frame it differently. The app compares the scores and explains which text appears more loaded based on the rule-based method.

This feature is useful because bias often becomes easier to see when two versions are placed side by side.

## 4:30-5:30 — Explain the code and INFOSCI 102 concepts

The project is organized into two main code files.

`analysis_engine.py` contains the core logic. It uses lists and dictionaries to store loaded terms, categories, weights, and explanations. It uses functions to clean text, find flagged terms, calculate scores, summarize categories, and generate the neutral rewrite.

`app.py` contains the Streamlit interface. It takes user input, calls the analysis functions, and displays the results using metrics, tables, charts, and text boxes.

This project uses INFOSCI 102 concepts such as strings, lists, dictionaries, loops, conditionals, functions, modules, and basic data display.

## 5:30-6:20 — Limitations and design decision

The biggest design decision was to use a transparent rule-based system instead of a complicated machine learning model. This makes the project easier to reproduce and easier to understand.

The limitation is that FrameCheck cannot truly verify facts, and it can miss subtle bias. It can also flag words that may be appropriate in some contexts. That is why I describe it as a critical-reading assistant, not a truth detector.

## 6:20-7:00 — Replication and closing

To run the project, a user installs the dependencies with:

```bash
pip install -r requirements.txt
```

Then they launch the app with:

```bash
streamlit run app.py
```

The repository also includes a README, a replication and AI usage document, sample inputs, and a demo script. All AI assistance and prompts are disclosed in the replication document.

Thank you for watching my demo.
