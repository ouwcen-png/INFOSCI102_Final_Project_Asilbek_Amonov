"""
FrameCheck analysis engine.

This file contains the rule-based text analysis used by the Streamlit app.
It is intentionally lightweight so classmates can inspect, run, and modify it.
No external API keys, datasets, or paid services are required.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class LexiconTerm:
    """A loaded word/phrase and the category it belongs to."""

    term: str
    category: str
    weight: int
    explanation: str


# A small, transparent lexicon. This is not meant to be a complete truth detector.
# It is a media-literacy aid that flags wording choices readers may want to inspect.
LEXICON: List[LexiconTerm] = [
    # Emotional / dramatic wording
    LexiconTerm("shocking", "Emotional language", 8, "Strong emotional wording can push the reader toward a reaction before evidence is shown."),
    LexiconTerm("outrage", "Emotional language", 8, "This word signals anger and can intensify the reader's emotional response."),
    LexiconTerm("furious", "Emotional language", 7, "This word emphasizes anger rather than a neutral description of events."),
    LexiconTerm("terrifying", "Emotional language", 8, "Fear-based language may increase sensationalism."),
    LexiconTerm("disaster", "Emotional language", 7, "This word frames the issue as severe before explaining the evidence."),
    LexiconTerm("collapse", "Emotional language", 7, "This word can imply extreme failure and may need evidence or context."),
    LexiconTerm("destroy", "Emotional language", 8, "This word strongly frames an action as harmful or catastrophic."),
    LexiconTerm("destroys", "Emotional language", 8, "This word strongly frames an action as harmful or catastrophic."),
    LexiconTerm("devastating", "Emotional language", 8, "This word emphasizes emotional impact and severity."),
    LexiconTerm("explosive", "Emotional language", 7, "This word often signals drama rather than neutral reporting."),
    LexiconTerm("bombshell", "Emotional language", 8, "This word is common in sensational framing."),
    LexiconTerm("nightmare", "Emotional language", 7, "This word frames the situation as frightening or chaotic."),

    # Exaggeration / certainty
    LexiconTerm("always", "Overgeneralization", 5, "Absolute wording can oversimplify complicated issues."),
    LexiconTerm("never", "Overgeneralization", 5, "Absolute wording can oversimplify complicated issues."),
    LexiconTerm("everyone", "Overgeneralization", 5, "Broad claims about all people usually require strong evidence."),
    LexiconTerm("nobody", "Overgeneralization", 5, "Broad claims about all people usually require strong evidence."),
    LexiconTerm("all", "Overgeneralization", 4, "Very broad language can hide important exceptions."),
    LexiconTerm("completely", "Overgeneralization", 5, "Totalizing language can make a claim sound more certain than it is."),
    LexiconTerm("totally", "Overgeneralization", 5, "Totalizing language can make a claim sound more certain than it is."),
    LexiconTerm("guaranteed", "Overgeneralization", 6, "Certainty language may be misleading when outcomes are uncertain."),
    LexiconTerm("proves", "Overgeneralization", 6, "A single event or study rarely proves a broad claim by itself."),

    # Urgency / clickbait
    LexiconTerm("breaking", "Urgency / clickbait", 4, "Urgency framing can be legitimate, but it can also push quick reactions."),
    LexiconTerm("urgent", "Urgency / clickbait", 6, "Urgency language can pressure the reader before they assess evidence."),
    LexiconTerm("must see", "Urgency / clickbait", 7, "This phrase is often used to attract attention rather than add information."),
    LexiconTerm("you won't believe", "Urgency / clickbait", 9, "This phrase is a common clickbait pattern."),
    LexiconTerm("what happens next", "Urgency / clickbait", 8, "This phrase is a common clickbait pattern."),
    LexiconTerm("secret", "Urgency / clickbait", 6, "This word can imply hidden knowledge without proving it."),
    LexiconTerm("exposed", "Urgency / clickbait", 7, "This word frames the story as a revelation or scandal."),

    # Political / identity labels
    LexiconTerm("radical", "Political framing", 7, "This label can frame a person or group negatively before evidence is discussed."),
    LexiconTerm("extremist", "Political framing", 8, "This label can be accurate in some contexts, but it strongly frames the subject."),
    LexiconTerm("leftist", "Political framing", 6, "Political identity labels can signal partisan framing."),
    LexiconTerm("right-wing", "Political framing", 6, "Political identity labels can signal partisan framing."),
    LexiconTerm("liberal elite", "Political framing", 8, "This phrase frames a political group in a negative way."),
    LexiconTerm("deep state", "Political framing", 8, "This phrase often signals conspiratorial or highly partisan framing."),
    LexiconTerm("corrupt", "Political framing", 7, "This accusation is strong and should be supported with evidence."),
    LexiconTerm("traitor", "Political framing", 9, "This is a highly charged label that frames the subject as morally illegitimate."),
    LexiconTerm("woke", "Political framing", 6, "This term is often used as a political label rather than a precise description."),
    LexiconTerm("anti-american", "Political framing", 8, "This phrase strongly frames a person or group as disloyal."),

    # Weak sourcing / rumor patterns
    LexiconTerm("some say", "Weak sourcing", 5, "Vague sourcing makes it hard to verify who is making the claim."),
    LexiconTerm("people are saying", "Weak sourcing", 6, "Vague sourcing can make a claim sound common without evidence."),
    LexiconTerm("sources say", "Weak sourcing", 4, "Anonymous sourcing can be valid, but readers should look for supporting details."),
    LexiconTerm("reportedly", "Weak sourcing", 3, "Reported claims may need verification from direct evidence."),
    LexiconTerm("rumor", "Weak sourcing", 6, "Rumor language suggests the claim may not be confirmed."),
    LexiconTerm("unconfirmed", "Weak sourcing", 5, "Unconfirmed claims should be treated cautiously."),

    # Misinformation risk cues
    LexiconTerm("hoax", "Misinformation cue", 7, "This word makes a strong claim that something is fake or deceptive."),
    LexiconTerm("cover-up", "Misinformation cue", 8, "This phrase implies hidden wrongdoing and needs strong evidence."),
    LexiconTerm("conspiracy", "Misinformation cue", 7, "This word may signal speculation or contested claims."),
    LexiconTerm("fake news", "Misinformation cue", 8, "This phrase is often used as a delegitimizing label."),
]

REPLACEMENTS: Dict[str, str] = {
    "shocking": "notable",
    "outrage": "criticism",
    "furious": "concerned",
    "terrifying": "serious",
    "disaster": "problem",
    "collapse": "decline",
    "destroy": "affect",
    "destroys": "affects",
    "devastating": "significant",
    "explosive": "important",
    "bombshell": "major development",
    "nightmare": "difficult situation",
    "always": "often",
    "never": "rarely",
    "everyone": "many people",
    "nobody": "few people",
    "completely": "substantially",
    "totally": "substantially",
    "guaranteed": "possible",
    "proves": "suggests",
    "breaking": "new report",
    "urgent": "time-sensitive",
    "must see": "worth noting",
    "you won't believe": "notable",
    "what happens next": "the next development",
    "secret": "previously undisclosed",
    "exposed": "reported",
    "radical": "controversial",
    "extremist": "strongly ideological",
    "leftist": "left-leaning",
    "right-wing": "conservative",
    "liberal elite": "liberal leaders",
    "deep state": "government officials",
    "corrupt": "accused of misconduct",
    "traitor": "critic",
    "woke": "progressive",
    "anti-american": "critical of U.S. policy",
    "some say": "some commentators claim",
    "people are saying": "some people claim",
    "sources say": "anonymous sources say",
    "rumor": "unverified claim",
    "unconfirmed": "not yet verified",
    "hoax": "alleged false claim",
    "cover-up": "alleged concealment",
    "conspiracy": "unverified explanation",
    "fake news": "disputed information",
}


def clean_text(text: str) -> str:
    """Normalize whitespace while preserving the original text for display."""
    return re.sub(r"\s+", " ", text.strip())


def count_all_caps_words(text: str) -> int:
    """Count words with 3+ uppercase letters, excluding common acronyms like USA."""
    words = re.findall(r"\b[A-Z]{3,}\b", text)
    common_acronyms = {"USA", "U.S", "U.S.A", "EU", "UN", "NATO", "AI", "COVID", "NASA", "FBI", "CIA"}
    return sum(1 for word in words if word not in common_acronyms)


def find_loaded_terms(text: str) -> List[Dict[str, object]]:
    """Find lexicon terms in the text using word-boundary matching."""
    lowered = text.lower()
    results: List[Dict[str, object]] = []

    for item in LEXICON:
        # Match phrases and words in a way that avoids matching inside unrelated words.
        pattern = r"(?<!\w)" + re.escape(item.term.lower()) + r"(?!\w)"
        matches = list(re.finditer(pattern, lowered))
        for match in matches:
            original = text[match.start():match.end()]
            results.append(
                {
                    "term": original,
                    "normalized": item.term,
                    "category": item.category,
                    "weight": item.weight,
                    "explanation": item.explanation,
                    "start": match.start(),
                    "end": match.end(),
                }
            )

    results.sort(key=lambda x: (int(x["start"]), -len(str(x["term"]))))
    return results


def category_summary(flags: List[Dict[str, object]]) -> Dict[str, int]:
    """Return total weight by category."""
    summary: Dict[str, int] = {}
    for flag in flags:
        category = str(flag["category"])
        summary[category] = summary.get(category, 0) + int(flag["weight"])
    return dict(sorted(summary.items(), key=lambda item: item[1], reverse=True))


def punctuation_score(text: str) -> Tuple[int, List[str]]:
    """Score punctuation/capitalization patterns often used in sensational text."""
    score = 0
    notes: List[str] = []

    exclamation_count = text.count("!")
    question_count = text.count("?")
    caps_count = count_all_caps_words(text)

    if exclamation_count >= 1:
        added = min(10, exclamation_count * 3)
        score += added
        notes.append(f"{exclamation_count} exclamation mark(s) add urgency or emotional intensity (+{added}).")

    if question_count >= 2:
        added = min(6, question_count * 2)
        score += added
        notes.append(f"{question_count} question marks may signal uncertainty or curiosity framing (+{added}).")

    if caps_count >= 1:
        added = min(10, caps_count * 4)
        score += added
        notes.append(f"{caps_count} all-caps word(s) can make a headline feel more aggressive (+{added}).")

    return score, notes


def length_adjustment(text: str) -> int:
    """Small adjustment for very short text where each loaded word has more influence."""
    words = re.findall(r"\b\w+\b", text)
    if 1 <= len(words) <= 8:
        return 5
    return 0


def risk_label(score: int) -> str:
    if score >= 70:
        return "High framing risk"
    if score >= 40:
        return "Medium framing risk"
    if score >= 15:
        return "Low-to-medium framing risk"
    return "Low framing risk"


def neutral_rewrite(text: str) -> str:
    """Create a simple neutralized version by replacing loaded terms and cleaning punctuation."""
    rewritten = clean_text(text)

    # Replace longer phrases first so phrase-level replacements happen before word replacements.
    for loaded, neutral in sorted(REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True):
        pattern = r"(?<!\w)" + re.escape(loaded) + r"(?!\w)"
        rewritten = re.sub(pattern, neutral, rewritten, flags=re.IGNORECASE)

    # Reduce repeated exclamation/question marks to a period when they appear at the end.
    rewritten = re.sub(r"!+", ".", rewritten)
    rewritten = re.sub(r"\?{2,}", "?", rewritten)
    rewritten = re.sub(r"\s+", " ", rewritten).strip()

    # Avoid awkward double periods.
    rewritten = re.sub(r"\.\.+", ".", rewritten)

    if rewritten and rewritten[-1] not in ".?!":
        rewritten += "."

    return rewritten


def analyze_text(text: str) -> Dict[str, object]:
    """Analyze text and return a transparent scoring report."""
    cleaned = clean_text(text)
    if not cleaned:
        return {
            "input": "",
            "score": 0,
            "risk_label": "No input",
            "flags": [],
            "category_summary": {},
            "punctuation_notes": [],
            "neutral_rewrite": "",
            "word_count": 0,
            "method_note": "Enter a headline or paragraph to analyze it.",
        }

    flags = find_loaded_terms(cleaned)
    lexical_score = sum(int(flag["weight"]) for flag in flags)
    punct_score, punct_notes = punctuation_score(cleaned)
    short_text_bonus = length_adjustment(cleaned) if flags else 0
    raw_score = lexical_score + punct_score + short_text_bonus
    score = max(0, min(100, raw_score))
    words = re.findall(r"\b\w+\b", cleaned)

    method_note = (
        "FrameCheck uses a transparent rule-based method. It does not verify truth. "
        "It flags wording patterns that may affect how readers interpret a story."
    )

    return {
        "input": cleaned,
        "score": score,
        "risk_label": risk_label(score),
        "flags": flags,
        "category_summary": category_summary(flags),
        "punctuation_notes": punct_notes,
        "neutral_rewrite": neutral_rewrite(cleaned),
        "word_count": len(words),
        "method_note": method_note,
    }


def compare_texts(text_a: str, text_b: str) -> Dict[str, object]:
    """Compare two headlines/articles and summarize which uses more loaded framing."""
    a = analyze_text(text_a)
    b = analyze_text(text_b)
    difference = int(a["score"]) - int(b["score"])

    if difference > 10:
        summary = "Text A appears more sensational or loaded than Text B based on this rule-based score."
    elif difference < -10:
        summary = "Text B appears more sensational or loaded than Text A based on this rule-based score."
    else:
        summary = "The two texts have similar framing scores based on this rule-based method."

    return {"text_a": a, "text_b": b, "difference": difference, "summary": summary}


def _cli() -> None:
    parser = argparse.ArgumentParser(description="Analyze a headline or paragraph with FrameCheck.")
    parser.add_argument("--text", required=True, help="Headline or paragraph to analyze")
    args = parser.parse_args()
    report = analyze_text(args.text)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    _cli()
