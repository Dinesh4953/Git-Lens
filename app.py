from flask import Flask, render_template, request, send_file
from dotenv import load_dotenv
from github_analyzer import fetch_repo_data
from scorer import calculate_score, weakest_area
from summary_ai import generate_summary
from roadmap import generate_roadmap, fix_first
import os

load_dotenv()

app = Flask(__name__)

# 1️⃣ FIRST PAGE → ROOT index.html (GUIDE PAGE)
@app.route("/")
def guide():
    return send_file("index.html")


# 2️⃣ ANALYZER PAGE
@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    if request.method == "POST":
        repo_url = request.form.get("repo_url")

        try:
            data = fetch_repo_data(repo_url)
            score, breakdown = calculate_score(data)
            summary = generate_summary(data, score)
            roadmap = generate_roadmap(data)

            # ----- LEVEL -----
            if score < 40:
                level = "Beginner"
            elif score < 70:
                level = "Intermediate"
            else:
                level = "Advanced"

            # ----- VERDICT -----
            verdict = "Production Ready" if score >= 75 else "Needs Improvement"

            # ----- CONFIDENCE (FIXED) -----
            commits = len(data["commits"])

            if commits >= 20:
                confidence_label = "High"
                confidence_percent = 92
            elif commits >= 8:
                confidence_label = "Medium"
                confidence_percent = 70
            else:
                confidence_label = "Low"
                confidence_percent = 45

            return render_template(
                "result.html",
                repo=data["repo"]["full_name"],
                score=score,
                level=level,
                verdict=verdict,
                confidence=confidence_percent,        # NUMBER
                confidence_label=confidence_label,    # TEXT
                breakdown=breakdown,
                weakest=weakest_area(breakdown),
                summary=summary,
                roadmap=roadmap,
                fix_first=fix_first(data),
                skills=data["skills"]
            )

        except Exception as e:
            return render_template("analyze.html", error=str(e))

    return render_template("analyze.html")



if __name__ == "__main__":
    app.run(debug=True)
