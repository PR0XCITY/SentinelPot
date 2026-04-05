# **SentinelPot**

> **A lightweight honeypot-based attacker behavior and threat analysis framework built on top of Cowrie SSH honeypot logs.**

---

## **📌 Overview**

**SentinelPot** is a cybersecurity project designed to capture, process, and analyze attacker activity from an **SSH honeypot environment**.

Built on top of the open-source **Cowrie SSH honeypot**, it helps transform raw attack logs into meaningful threat intelligence using custom Python modules for:

- **Session reconstruction**
- **Threat scoring**
- **Suspicious command detection**
- **GeoIP enrichment**
- **Readable report generation**
- **CSV export**
- **Terminal dashboard output**

---

## **🚀 Features**

- **SSH honeypot integration** using **Cowrie**
- **Session reconstruction** from honeypot logs
- **Threat scoring** and severity classification
- **Suspicious command detection**
- **GeoIP-based attacker country enrichment**
- **Human-readable report generation**
- **CSV report generation**
- **Terminal-based dashboard output**

---

## **📂 Project Structure**

```bash
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
```

---

## **🛠️ Requirements**

Before running **SentinelPot**, make sure you have:

- **Kali Linux** or **Ubuntu**
- **Python 3**
- **Cowrie SSH honeypot** installed separately
- A **Python virtual environment**

---

## **⚙️ Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/PR0XCITY/SentinelPot.git
cd SentinelPot
```

### **2. Create a Virtual Environment**

```bash
python3 -m venv venv
```

### **3. Activate the Virtual Environment**

```bash
source venv/bin/activate
```

### **4. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## **🐄 Cowrie Setup**

**SentinelPot** depends on **Cowrie** for collecting attacker interaction logs.

Make sure **Cowrie** is installed and running separately before using this framework.

### **Example Cowrie Startup**

```bash
cd ~/cowrie
source cowrie-env/bin/activate
bin/cowrie start
```

---

## **▶️ Running SentinelPot**

Move into the project directory and activate the environment:

```bash
cd ~/sentinelpot
source venv/bin/activate
```

Then run your main analysis script:

```bash
python3 src/main.py
```

> **Note:** Replace `src/main.py` with your actual entry-point file if it is different.

---

## **📊 Output**

SentinelPot can generate outputs such as:

- **Reconstructed attacker sessions**
- **Threat-scored attack summaries**
- **Suspicious command logs**
- **GeoIP-enriched attacker metadata**
- **CSV-based reports**
- **Readable security analysis reports**

Generated files are typically stored in:

```bash
output/
reports/
```

---

## **🎯 Use Cases**

SentinelPot is useful for:

- **Cybersecurity learning and experimentation**
- **Attacker behavior analysis**
- **SSH brute-force and post-login activity observation**
- **Basic threat intelligence enrichment**
- **Honeypot log analysis and reporting**

---

## **⚠️ Disclaimer**

This project is intended for **educational and research purposes only**.

Do **not** deploy or expose a honeypot carelessly on production infrastructure without understanding the associated risks.

---

## **👨‍💻 Author**

**Abhyudai Srivastava**