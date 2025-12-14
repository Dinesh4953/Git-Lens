def generate_summary(data, score):
    issues = []

    if not data["has_readme"]:
        issues.append("Documentation is insufficient.")
    if not data["has_tests"]:
        issues.append("Automated tests are missing.")
    if len(data["commits"]) < 10:
        issues.append("Commit activity is inconsistent.")

    if not issues:
        return "Repository shows strong structure, documentation, and development practices."

    return " ".join(issues)
