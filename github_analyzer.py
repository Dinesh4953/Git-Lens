import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def fetch_repo_data(repo_url):
    owner, repo = repo_url.replace("https://github.com/", "").strip("/").split("/")
    base = f"https://api.github.com/repos/{owner}/{repo}"

    repo_resp = requests.get(base, headers=HEADERS, timeout=10).json()
    if "message" in repo_resp:
        raise Exception(repo_resp["message"])

    commits = requests.get(
        base + "/commits?per_page=30",
        headers=HEADERS,
        timeout=10
    ).json()

    contents = requests.get(
        base + "/contents",
        headers=HEADERS,
        timeout=10
    ).json()

    if isinstance(contents, dict):
        contents = []

    files = [f["name"].lower() for f in contents if "name" in f]

    return {
        "repo": repo_resp,
        "commits": commits if isinstance(commits, list) else [],
        "contents": contents,
        "has_readme": any("readme" in f for f in files),
        "has_tests": any("test" in f for f in files),
        "has_ci": ".github" in files
    }
    
    
    
    
    
import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def fetch_repo_data(repo_url):
    owner, repo = repo_url.replace("https://github.com/", "").strip("/").split("/")
    base = f"https://api.github.com/repos/{owner}/{repo}"

    # Repo metadata
    repo_resp = requests.get(base, headers=HEADERS, timeout=10).json()
    if "message" in repo_resp:
        raise Exception(repo_resp["message"])

    # Commits (limited)
    commits = requests.get(
        base + "/commits?per_page=30",
        headers=HEADERS,
        timeout=10
    ).json()

    # Contents
    contents = requests.get(
        base + "/contents",
        headers=HEADERS,
        timeout=10
    ).json()
    if isinstance(contents, dict):
        contents = []

    files = [f["name"].lower() for f in contents if "name" in f]

    # Languages API (IMPORTANT)
    languages_resp = requests.get(
        base + "/languages",
        headers=HEADERS,
        timeout=10
    ).json()

    # -------- SKILL EXTRACTION --------
    skills = set()

    # Languages
    for lang in languages_resp.keys():
        skills.add(lang)

    # Framework & tools detection
    if "requirements.txt" in files or "pipfile" in files:
        skills.add("Python Backend")

    if "app.py" in files:
        skills.add("Flask")

    if "manage.py" in files:
        skills.add("Django")

    if "package.json" in files:
        skills.add("JavaScript / Node.js")

    if ".github" in files:
        skills.add("CI/CD (GitHub Actions)")

    if any("test" in f for f in files):
        skills.add("Automated Testing")

    if not skills:
        skills.add("General Programming")

    return {
        "repo": repo_resp,
        "commits": commits if isinstance(commits, list) else [],
        "contents": contents,
        "has_readme": any("readme" in f for f in files),
        "has_tests": any("test" in f for f in files),
        "has_ci": ".github" in files,
        "skills": sorted(skills)
    }

