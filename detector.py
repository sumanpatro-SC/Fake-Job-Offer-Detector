from rules import SUSPICIOUS_KEYWORDS, SUSPICIOUS_DOMAINS

def analyze_text(text):
    text_lower = text.lower()
    risk_score = 0
    reasons = []

    for keyword, score in SUSPICIOUS_KEYWORDS.items():
        if keyword in text_lower:
            risk_score += score
            reasons.append(f"Suspicious keyword detected: '{keyword}'")

    for domain in SUSPICIOUS_DOMAINS:
        if domain in text_lower:
            risk_score += 25
            reasons.append("Unofficial email domain used")

    if risk_score > 100:
        risk_score = 100

    if risk_score <= 30:
        level = "Low Risk"
    elif risk_score <= 60:
        level = "Medium Risk"
    else:
        level = "High Risk"

    return {
        "risk_score": risk_score,
        "risk_level": level,
        "reasons": reasons
    }
