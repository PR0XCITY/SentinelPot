def explain(data):
    reasons = []

    if data["failed_logins"] > 0:
        reasons.append("Multiple failed login attempts")

    for c in data["commands"]:
        if "uname" in c or "id" in c:
            reasons.append("System reconnaissance detected")
        if "wget" in c or "curl" in c:
            reasons.append("Malware download attempt detected")
        if "sudo" in c or "su" in c:
            reasons.append("Privilege escalation attempt detected")

    if not reasons:
        reasons.append("Low-risk probing activity")

    return list(set(reasons))

