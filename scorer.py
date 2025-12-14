def calculate_score(data):
    score = 0
    breakdown = {}

    # Documentation
    if data["has_readme"]:
        breakdown["Documentation"] = 15
        score += 15
    else:
        breakdown["Documentation"] = 5
        score += 5

    # Project Structure
    if len(data["contents"]) >= 6:
        breakdown["Structure"] = 15
        score += 15
    else:
        breakdown["Structure"] = 8
        score += 8

    # Commit Consistency
    commits = len(data["commits"])
    if commits >= 20:
        breakdown["Commits"] = 15
        score += 15
    elif commits >= 10:
        breakdown["Commits"] = 10
        score += 10
    else:
        breakdown["Commits"] = 5
        score += 5

    # Testing
    if data["has_tests"]:
        breakdown["Testing"] = 15
        score += 15
    else:
        breakdown["Testing"] = 5
        score += 5

    # CI/CD
    if data["has_ci"]:
        breakdown["CI/CD"] = 10
        score += 10
    else:
        breakdown["CI/CD"] = 3
        score += 3

    # Code Depth
    if data["repo"].get("size", 0) > 300:
        breakdown["Depth"] = 10
        score += 10
    else:
        breakdown["Depth"] = 5
        score += 5

    return score, breakdown


def weakest_area(breakdown):
    """
    Returns the weakest scoring area
    Used for 'Primary Weakness' feature
    """
    return min(breakdown, key=breakdown.get)
