# 🔍 RepoLens AI

**RepoLens AI** is a recruiter-style GitHub repository analyzer that evaluates projects beyond raw metrics.  
It gives a clear verdict, highlights critical weaknesses, and tells developers exactly what to fix first.

---

## 🚀 Live Demo

👉 **Deployed Application:**  
https://git-lens.onrender.com

(Open the link to analyze any public GitHub repository of thi project)

---
# 📽 Project Presentation (Rendered Slides)

The project presentation is available as a rendered slide deck:

🔗 **View Slides Online:**  
https://docs.google.com/presentation/d/XXXXXXXX/view

📥 **Download PPT:**  
[RepoLens-AI.pptx](docs/RepoLens-AI.pptx)
---

## 🧠 Why RepoLens AI?

Most tools only show metrics like stars, commits, or languages.  
**RepoLens AI acts like a recruiter.**

> “Most tools show metrics. RepoLens acts like a recruiter — it gives a verdict, highlights weaknesses, and tells exactly what to fix first.”

> “RepoLens AI doesn’t just evaluate repositories, it teaches students how to build recruiter-ready GitHub projects before evaluation.”

---

## 🔍 What Repositories Can Be Analyzed?

- ✅ Public GitHub repositories
- ✅ Academic / personal projects
- ✅ Internship & portfolio repositories
- ❌ Private repositories (GitHub API restriction)
- ❌ Empty or ZIP-only uploads

#
## 🧪 Testing
Tests are included using pytest and are automatically run using GitHub Actions.

## 🔄 CI/CD
This project uses GitHub Actions to run automated tests on every push.

## 🏗 Architecture & Code Depth

The project is designed with scalability in mind. Core responsibilities are logically separated:
- Routing and orchestration in `app.py`
- Analysis and scoring logic in dedicated helper modules
- CI/CD and testing handled independently

Future refactoring will further modularize services and utilities.
