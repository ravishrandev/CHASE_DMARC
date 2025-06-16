# 📊 DMARC Analyzer

Author: Rav Kulathanthilage
Last modified: 16/06/2025


This Python-based tool automates the process of collecting and analyzing DMARC reports from your Gmail inbox. It securely connects via the Gmail API, downloads zipped XML reports, parses the data, and displays a clean, tabulated summary — optionally inside a Docker container.

Run once or twice a week to monitor mails passing through the CHASE domain to protect against malicious attacks

---

## 🚀 Features

- Securely connects to Gmail using OAuth 2.0
- Parses zipped DMARC XML reports
- Summarizes data into a readable table (using `tabulate`)
- Supports both local and Dockerized usage

---

## 🛠️ Getting Started

### 🔑 1. Google Cloud Setup
- Create a project in [Google Cloud Console](https://console.cloud.google.com/)
- Enable the Gmail API
- Download the `credentials.json` file and place it in your project root

---

### 💻 2. Run Locally (Python)

Make sure dependencies in `requirements.txt` are installed:

```bash
pip install -r requirements.txt

```

then run the script:

```bash
python main.py
```

## 🐳 Run with Docker (Recommended)

```bash
docker run \
  -v $(pwd):/app \
  -v $(pwd)/credentials.json:/app/credentials.json \
  -v $(pwd)/token.json:/app/token.json \
  dmarc-analyzer
  ```


## 📂 File Structure
.
├── extracted/                # Unzipped XML DMARC files
├── main.py                  # Entry point
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker config
├── README.md                # This file
├── credentials.json         # OAuth credentials (not committed)
└── token.json               # Generated access token (not committed)

