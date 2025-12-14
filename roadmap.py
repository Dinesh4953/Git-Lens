def generate_roadmap(data):
    roadmap = []

    if not data["has_readme"]:
        roadmap.append("Create a README with setup and usage instructions.")

    if not data["has_tests"]:
        roadmap.append("Add unit tests using pytest or unittest.")

    if not data["has_ci"]:
        roadmap.append("Configure GitHub Actions for CI/CD.")

    roadmap.append("Improve commit message clarity and frequency.")
    roadmap.append("Refactor code for modularity and readability.")

    return roadmap


def fix_first(data):
    fixes = []

    if not data["has_readme"]:
        fixes.append("Add README.md")

    if not data["has_tests"]:
        fixes.append("Introduce automated tests")

    return fixes[:2]
