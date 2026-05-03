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
- organizing the project into GitHub-ready files
- drafting the README
- drafting this replication and AI usage document
- drafting a demo video script
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

The following prompts summarize the non-trivial AI prompts used during development:

1. **Project simplification prompt**

```text
I have a final project proposal about building an AI-assisted Python tool that helps users evaluate reliability, framing, sensationalism, bias, and misinformation in news content. I only have a few hours. What simpler project from this idea would work best for INFOSCI 102 while still scoring well on originality and the rubric?
```

2. **Implementation prompt**

```text
Based on the final project rubric and my proposal, create a simple but strong Python project that can be uploaded to GitHub. It should analyze news headlines or short paragraphs for loaded wording, sensationalism, political framing, and weak sourcing. Make it simple enough to finish quickly, but polished enough for a high grade. Include a Streamlit app, scoring logic, neutral rewrite feature, README, replication document, AI disclosure, and demo script.
```

3. **Documentation prompt**

```text
Write a replication and AI usage document for this INFOSCI 102 project. Include operating system, Python version, dependencies, installation steps, how to run the project, expected outputs, AI tools used, prompts used, what AI contributed, what I contributed, and external resources.
```

4. **Demo script prompt**

```text
Create a 4-7 minute demo video script for a Streamlit project called FrameCheck. The project analyzes news headlines for sensationalism and framing, shows flagged terms, gives a score, compares two headlines, and suggests a neutral rewrite. The script should explain the purpose, design decisions, code logic, limitations, and how to run it.
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
