# Multi-Agent Research Assistant

**Built by [Amit Kumar](https://www.linkedin.com/in/amitkumar1454/) — MSc Data Science, University of Westminster, London**

An autonomous multi-agent research pipeline built with **LangGraph** and **LangChain**. Four specialised AI agents collaborate — supervised by a central orchestrator — to research any topic, draft a structured report, and iteratively refine it until quality is approved.

![LangGraph Architecture](assets/research_graph.png)
*Multi-agent workflow visualised as a LangGraph state machine*

---

## What it does

You enter a research topic. The system automatically:

1. **Supervisor** analyses the current state and routes to the right agent
2. **Researcher** pulls live web intelligence via Tavily Search
3. **Writer** synthesises findings into a structured 900–1400 word report
4. **Critiquer** reviews across 5 dimensions (coverage, evidence, structure, clarity, actionability)
5. Loop continues until the Critiquer approves or 3 revisions are completed
6. Final report available to read and download in the Streamlit UI

---

## Tech Stack

| Layer | Tools |
|---|---|
| Agent orchestration | LangGraph, LangChain |
| LLM | Together AI (Mixtral-8x7B) |
| Web search | Tavily Search API |
| UI | Streamlit |
| Language | Python 3.9+ |

---

## Project Structure

```
Multi-Agent-Research-Assistant-Langgraph/
├── agents.py          # Agent node implementations (Supervisor, Researcher, Writer, Critiquer)
├── graph.py           # LangGraph state machine and workflow builder
├── prompts.py         # All agent prompt templates
├── app.py             # Streamlit web application
├── main.py            # CLI entry point
├── visualize_graph.py # Generate workflow graph image
├── assets/
│   └── research_graph.png
├── tests/
│   └── test_tools.py
├── requirements.txt
├── .env               # API keys (not committed)
└── README.md
```

---

## Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/Phoenix1454/Multi-Agent-Research-Assistant-Langgraph.git
cd Multi-Agent-Research-Assistant-Langgraph
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up API keys

Create a `.env` file in the root:

```env
TOGETHER_API_KEY=your_together_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get your keys:
- **Together AI** → [together.ai](https://www.together.ai/) (free tier available)
- **Tavily** → [tavily.com](https://tavily.com/) (free tier available)

### 4. Run the app

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

### Optional — visualise the graph

```bash
python visualize_graph.py
```

---

## Testing

Unit tests cover the supervisor's routing logic and the critique safety checks (no API keys required):

```bash
uv run pytest tests/ -v
```

Tests run automatically on every push via [GitHub Actions](.github/workflows/tests.yml).

---

## Agent Architecture

```
START
  │
  ▼
Supervisor ──► Researcher ──┐
  ▲                         │
  └──── Critiquer ◄── Writer┘
  │
  ▼ (APPROVED or max revisions)
END
```

Each agent runs as a node in a LangGraph `StateGraph`. The Supervisor uses conditional edges to route between nodes based on workflow state — no hardcoded sequencing.

---

## Example Topics

- *"The impact of large language models on software engineering jobs"*
- *"Latest advances in retrieval-augmented generation (RAG)"*
- *"How agentic AI systems are changing enterprise workflows in 2025"*
- *"Quantum computing applications in cybersecurity"*

---

## Testing

Unit tests cover the Supervisor's routing logic and the Critiquer's safety checks — no API keys required:

```bash
uv run pytest tests/ -v
```

Tests run automatically on every push via GitHub Actions.

---

## Troubleshooting

**API key errors** — check your `.env` is in the project root with no extra spaces

**Import errors** — run `pip install -r requirements.txt --upgrade`

**Together AI quota** — the free tier has rate limits; wait a minute and retry

---

## Licence

MIT © 2026 Amit Kumar — see [LICENSE](LICENSE)

---

## Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amit_Kumar-blue?logo=linkedin)](https://www.linkedin.com/in/amitkumar1454/)
[![GitHub](https://img.shields.io/badge/GitHub-Phoenix1454-black?logo=github)](https://github.com/Phoenix1454)
