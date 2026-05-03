# Replication and AI Usage Document

## Project title

FrameCheck: News Bias and Sensationalism Detector

## Author

Asilbek Amonov

## 1. Project overview

FrameCheck is a Python-based media-literacy tool that analyzes news headlines or short article text for potentially loaded framing. The app gives a framing/sensationalism score, identifies specific flagged words, explains why those words matter, summarizes the categories of framing, and suggests a more neutral rewrite.

The project does not claim to determine absolute truth or detect misinformation with certainty. Instead, it functions as a critical-reading assistant that helps users notice wording choices that may shape interpretation.

## 2. Tested environment

The project was designed to run in a standard Python environment.

Tested configuration:

- Operating system: macOS / Windows / Linux should all work
- Python: 3.11 or newer recommended
- Browser: Chrome, Safari, Edge, or Firefox
- Hardware: no special hardware required
- Internet: only needed to install dependencies or upload the project to GitHub/Canvas

## 3. Required software

Required:

- Python 3.11 or newer
- pip
- Streamlit
- pandas

Dependencies are listed in `requirements.txt`:

```text
streamlit==1.57.0
pandas==3.0.2
```

## 4. Installation instructions

### Step 1: Download the project

Download the repository from GitHub or unzip the submitted project folder.

### Step 2: Open a terminal in the project folder

The folder should contain:

```text
app.py
analysis_engine.py
requirements.txt
README.md
replication_ai_usage.md
```

### Step 3: Install dependencies

Run:

```bash
pip install -r requirements.txt
```

### Step 4: Launch the app

Run:

```bash
streamlit run app.py
```

After this command, Streamlit should open the app in the browser. If it does not open automatically, copy the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## 5. How to use the project

### Analyze one text

1. Open the app.
2. Go to the **Analyze one text** tab.
3. Paste a headline or short paragraph.
4. Click **Analyze text**.
5. Read the score, flagged words, explanations, category chart, punctuation notes, and neutral rewrite.

Example input:

```text
SHOCKING: Radical leaders destroy the economy in devastating policy disaster!!!
```

Expected behavior:

- The app gives a high framing/sensationalism score.
- It flags terms such as `SHOCKING`, `Radical`, `destroy`, `devastating`, and `disaster`.
- It explains that these words create emotional or political framing.
- It suggests a more neutral rewrite.

### Compare two texts

1. Go to the **Compare two texts** tab.
2. Paste two versions of a headline.
3. Click **Compare texts**.
4. Compare the two scores and explanations.

Example:

Text A:

```text
SHOCKING: Radical policy destroys local economy!!!
```

Text B:

```text
New policy faces criticism over possible economic effects
```

Expected behavior:

- Text A should receive a higher score than Text B.
- The app should explain that Text A contains more loaded emotional/political wording.

## 6. Optional command-line test

The core engine can also be run without Streamlit:

```bash
python analysis_engine.py --text "SHOCKING: Radical leaders destroy the economy!!!"
```

Expected output:

A JSON-style report with the score, risk label, flagged words, category summary, and neutral rewrite.

## 7. Optional unit tests

To run the basic tests:

```bash
python -m unittest discover tests
```

Expected output:

The tests should pass and confirm that high-sensationalism text scores higher than neutral text.

## 8. Data and model requirements

No external dataset, API key, paid service, or model weight is required. The project uses a small transparent lexicon built directly into `analysis_engine.py`.

This choice was intentional because the final project needed to be reproducible. A rule-based system is easier for classmates and instructors to inspect, run, and understand.

## 9. AI Use and External Resources Disclosure

### AI tools used

- ChatGPT, GPT-5.5 Thinking, used as a programming and documentation assistant.
- Codex or similar AI coding tool may be used to help paste, edit, or debug the files locally.

### What AI helped with

AI assistance was used for:

- narrowing the original broad project proposal into a realistic final project
- designing the app structure
- writing the first version of the Python code
- drafting this replication and AI usage document
- debugging and simplifying implementation choices

### What was student-authored / student-directed

The project idea came from my original proposal about building an AI-assisted Python tool for evaluating reliability, bias, sensationalism, and misleading framing in news content. I directed the scope toward a simpler, more reproducible version focused on headline and short-text analysis.

Student design decisions included:

- focusing on media literacy rather than claiming absolute truth detection
- choosing a transparent rule-based method instead of a complex ML model
- including a neutral rewrite feature
- including a two-headline comparison feature
- presenting results in a way that non-technical users can understand

### Prompt documentation


1. **Implementation prompt**

```text
Help me turn the simplified idea into a small Streamlit project. The project should analyze a headline or short paragraph, flag loaded language, give a score, explain the result, and include one original feature that makes it more than a basic sentiment checker.
```

2. **Documentation prompt**

```text
Help me organize the project into clean Python files for GitHub. I want one file for the Streamlit app, one file for the analysis logic, a requirements file, a README, and a replication document. Review the project structure and explain how other students can run it. Make sure the instructions are simple enough for someone using Python and Streamlit for the first time.
```



### External resources used

- Streamlit documentation was used to confirm how to install and run a Streamlit app.
- GitHub documentation was used to confirm how to create a repository and upload files.
- No external datasets, code repositories, pretrained models, or paid APIs were used.

## 10. Limitations

FrameCheck has important limitations:

1. It does not verify whether a factual claim is true.
2. It can miss subtle bias that does not use obvious loaded words.
3. It can flag words that are reasonable in some contexts.
4. The score depends on a small rule-based lexicon, not a trained model.
5. The neutral rewrite is simple and may not always produce perfect wording.

These limitations are part of the design transparency. The goal is not to replace human judgment, but to support critical reading.

## 11. Originality statement

The original contribution is the combination of:

- a transparent loaded-language scoring system
- category-level explanation
- a visual framing fingerprint
- side-by-side headline comparison
- neutral rewrite suggestion
- a clear media-literacy framing that avoids overclaiming truth detection

This makes the project more original than a basic sentiment analysis demo because it focuses on explainability and user interpretation.
