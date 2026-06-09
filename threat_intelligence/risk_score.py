def calculate_risk_score(abuse_score, malicious):

    if abuse_score > 70 or malicious:
        return "High"

    return "Low"
