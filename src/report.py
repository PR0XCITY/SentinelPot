import os
import csv
from enrichment.geoip import get_country


def generate_report(sessions, scores, insights):

    os.makedirs("output", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    with open("output/report.txt", "w") as f:

        f.write("=" * 60 + "\n")
        f.write("SentinelPot Honeypot Security Analysis Report\n")
        f.write("=" * 60 + "\n\n")

        for sid, data in sessions.items():

            score, level, reasons = scores[sid]

            f.write(f"Session ID : {sid}\n")
            country = get_country(data['ip'])
            f.write(f"Attacker IP : {data['ip']}\n")
            f.write(f"Country     : {country}\n")

            f.write("Commands Executed:\n")

            if data["commands"]:
                for cmd in data["commands"]:
                    f.write(f"  - {cmd}\n")
            else:
                f.write("  - None\n")

            f.write(f"\nFailed Logins : {data['failed_logins']}\n")
            f.write(f"Threat Level : {level}\n")
            f.write(f"Threat Score : {score}\n")

            f.write("\nIndicators:\n")

            for r in reasons:
                f.write(f" * {r}\n")

            f.write("\n" + "-" * 60 + "\n\n")

        f.write("=" * 60 + "\n")
        f.write("Attack Summary\n")
        f.write("=" * 60 + "\n")

        f.write(f"Total Sessions: {len(sessions)}\n")


    with open("reports/report.csv", "w", newline="") as csvfile:

        writer = csv.writer(csvfile)
        writer.writerow(["session", "ip", "threat_level", "score"])

        for sid, data in sessions.items():
            score, level, _ = scores[sid]
            writer.writerow([sid, data["ip"], level, score])
