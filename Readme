# 🤖 Agentic AI Code Review & Refactoring System

An **agentic AI system** that automatically reviews GitHub repositories, detects code quality and security issues, and proposes **safe, verified refactors** using local LLMs.
Built with **FastAPI, Docker, Streamlit, and Ollama**, this project combines deterministic analysis with LLM reasoning and verifier-gated safety checks.

---

## 🚀 Features

* **Agentic Architecture** with task-specific agents
* **Deterministic-first analysis** (AST, Bandit, Semgrep)
* **LLM-powered refactoring** (unified diffs only)
* **Verifier-gated safety** (tests run before acceptance)
* **Offline LLM inference** via Ollama
* **Dockerized backend**
* **Streamlit UI** for easy repo submission
* **GitHub-ready** webhook integration (optional)

---

## 🧠 System Overview

```
User / Streamlit UI
        ↓
   POST /review
        ↓
   FastAPI Backend
        ↓
   Review Service
        ↓
 Planner → Analyzer → Security → Refactor → Verifier
        ↓
   Verified Results
```

---

## 🧩 Agents

* **Planner Agent**
  Identifies important files and prioritizes analysis.

* **Code Analyzer Agent**
  AST-based static analysis for bugs and code smells.

* **Security Agent**
  Integrates Bandit and Semgrep for vulnerability detection.

* **Refactor Agent**
  Uses LLMs to generate safe, unified diffs only.

* **Verifier Agent**
  Applies patches and runs tests to accept or reject changes.

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Python
* **AI/LLM:** Ollama (local), LangChain
* **Security:** Bandit, Semgrep
* **Containerization:** Docker, Docker Compose
* **Frontend:** Streamlit
* **VCS Integration:** GitHub API (optional)

---

## ⚙️ Setup & Run

### Prerequisites

* Python 3.10+
* Docker & Docker Compose
* Ollama (installed locally)

### 1. Start Ollama

```bash
ollama serve
ollama pull qwen2.5:7b
```

### 2. Run Backend (Docker)

```bash
docker compose -f docker/docker-compose.prod.yml up -d --build
```

Backend will be available at:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

## 🖥️ Streamlit UI

### Install

```bash
pip install streamlit requests
```

### Run

```bash
streamlit run streamlit_app.py
```

Open:

```
http://localhost:8501
```

Paste a GitHub repo URL and start the review.

---

## 🔌 API Usage

### Review a Repository

**Endpoint**

```
POST /review
```

**Body**

```json
{
  "repo_url": "https://github.com/psf/requests"
}
```

**Response (example)**

```json
{
  "status": "completed",
  "results": [
    {
      "file": "app/main.py",
      "status": "accepted",
      "rationale": "Improved error handling without behavior change"
    }
  ]
}
```

---

## 🔐 GitHub Webhook (Optional)

* Designed for GitHub App integration
* Triggered on PR events
* Posts review feedback as PR comments

> Note: Webhook endpoints are not meant for manual testing.

---

## 🧪 Safety & Reliability

* No direct code modification without verification
* Unified diffs ensure Git safety
* Tests gate every refactor
* Deterministic tools reduce hallucinations
* Local LLM ensures privacy and cost control

---

## 📌 Use Cases

* Automated code reviews
* Secure CI pipelines
* Internal developer tooling
* AI-assisted refactoring platforms

---

## 🔮 Future Enhancements

* Async job queue (Celery/Redis)
* GitHub PR comments & auto-fix branches
* User auth and review history
* Multi-language support
* Production deployment (AWS/GCP)

---

## 📜 License

MIT License

---

**Author:** Priyansh
**Status:** Production-ready (MVP)
