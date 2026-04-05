def calculate_score(data):

    score = 0
    reasons = []

    score += data["failed_logins"] * 2

    for cmd in data["commands"]:

        if "uname" in cmd or "id" in cmd:
            score += 1
            reasons.append("Reconnaissance command detected")

        if "sudo" in cmd or "su" in cmd:
            score += 3
            reasons.append("Privilege escalation attempt")

        if "wget" in cmd or "curl" in cmd:
            score += 5
            reasons.append("Possible malware download")

    if score >= 8:
        level = "HIGH"
    elif score >= 4:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level, list(set(reasons))
