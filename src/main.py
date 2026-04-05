import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parser import load_events
from analyzer import build_sessions
from threat_score import calculate_score
from insights import explain
from report import generate_report
from analysis.stats import generate_stats


LOG_PATH = os.path.expanduser("~/cowrie/var/log/cowrie/cowrie.json")

if not os.path.exists(LOG_PATH):
    LOG_PATH = "samples/cowrie.json"

events = load_events(LOG_PATH)

sessions = build_sessions(events)

scores = {}
insights = {}

for sid, data in sessions.items():

    score, level, reasons = calculate_score(data)

    scores[sid] = (score, level, reasons)

    insights[sid] = explain(data)


generate_report(sessions, scores, insights)


attackers, commands = generate_stats(sessions)

print("\nTop Attacker IPs:")
for ip, count in attackers.items():
    print(ip, "→", count)

print("\nMost Used Commands:")
for cmd, count in commands.items():
    print(cmd, "→", count)

print("\nAnalysis complete")
print("Report saved in output/report.txt")
