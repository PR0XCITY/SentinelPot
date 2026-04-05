def generate_stats(sessions):

    attacker_count = {}
    command_count = {}

    for s in sessions.values():

        ip = s["ip"]
        attacker_count[ip] = attacker_count.get(ip, 0) + 1

        for cmd in s["commands"]:
            base = cmd.split()[0]
            command_count[base] = command_count.get(base, 0) + 1

    return attacker_count, command_count
