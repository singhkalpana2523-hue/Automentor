from agents.code_analysis_agent import analyze_code
from agents.explanation_agent import explain_issues
from agents.suggestion_agent import suggest_improvements

def run_agents(code):
    issues = analyze_code(code)

    explanations = explain_issues(issues)
    suggestions = suggest_improvements(issues)

    return {
        "issues": issues,
        "explanations": explanations,
        "suggestions": suggestions,
        "agent_mode": "AI-Reasoning Enabled"
    }
