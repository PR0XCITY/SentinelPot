def build_sessions(events):
    s = {}

    for e in events:
        sid = e.get("session")
        if not sid:
            continue

        if sid not in s:
            s[sid] = {
                "ip": e.get("src_ip"),
                "commands": [],
                "failed_logins": 0
            }

        if e.get("eventid") == "cowrie.login.failed":
            s[sid]["failed_logins"] += 1

        if e.get("eventid") == "cowrie.command.input":
            s[sid]["commands"].append(e.get("input"))

    return s

