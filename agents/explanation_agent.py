import requests

def explain_issues(issues):
    if not issues:
        return ["No major issues detected. Code quality looks good."]

    explanations = []

    for issue in issues:
        prompt = f"""
You are an experienced programming mentor.
Explain the following code issue to a beginner in simple language:

Issue: {issue}

Give a short and clear explanation.
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        explanation = response.json()["response"]
        explanations.append(explanation.strip())

    return explanations
