\# SentinelPot

\## Honeypot-Based Attacker Behavior \& Threat Analysis Framework



SentinelPot is a cybersecurity project built on top of the open-source Cowrie SSH honeypot.  

It captures attacker activity and analyzes it using custom Python modules for session reconstruction, threat scoring, geolocation enrichment, and report generation.



\---



\## Project Structure



sentinelpot/

│

├── analysis/

├── dashboard/

├── data/

├── enrichment/

├── output/

├── reports/

├── samples/

├── src/

├── README.md

└── requirements.txt



\---



\## Features



\- SSH honeypot integration using Cowrie

\- Session reconstruction from honeypot logs

\- Threat scoring and severity classification

\- Suspicious command detection

\- GeoIP-based attacker country enrichment

\- Human-readable report generation

\- CSV report generation

\- Terminal-based dashboard output



\---



\## Requirements



\- Kali Linux / Ubuntu

\- Python 3

\- Cowrie installed separately

\- Python virtual environment



\---



\## Dependency Installation



Inside SentinelPot:



```bash

cd \~/sentinelpot

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

