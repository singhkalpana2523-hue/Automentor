from flask import Flask, render_template, request
from agents.code_analysis_agent import analyze_code
from agents.explanation_agent import explain_issues
from agents.suggestion_agent import suggest_improvements
from agents.coordinator_agent import run_agents

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    feedback = None
    if request.method == "POST":
        code = request.form["code"]
        feedback = run_agents(code)

        # feedback = {
        #     "issues": issues,
        #     "explanations": explanations,
        #     "suggestions": suggestions
        # }

    return render_template("index.html", feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
