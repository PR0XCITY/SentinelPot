import os

print("\n===================================")
print(" SentinelPot Security Dashboard")
print("===================================\n")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_PATH = os.path.join(BASE, "output", "report.txt")

if not os.path.exists(REPORT_PATH):
    print("Report not found. Run analysis first.")
else:
    with open(REPORT_PATH) as f:
        print(f.read())

print("===================================")
print(" End of Report")
print("===================================\n")
