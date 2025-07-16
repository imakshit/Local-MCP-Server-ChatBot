# Local-MCP-Server-ChatBot (with MCP Server + HTML UI)

A lightweight local AI chat app powered by [LLaMA3](https://ollama.com/library/llama3), [Ollama](https://ollama.com/), and a custom **Model Control Plane (MCP)** API server. Includes a simple HTML+JS frontend to interact with the model.

---

## 🔧 Features

- 🚀 Run LLaMA3 locally via [Ollama](https://ollama.com)
- 🛠️ Custom MCP server built with FastAPI
- 🌐 HTML/CSS UI (no React/Node required)
- ⚡ Blazingly fast, private, and local
- 💬 Ask questions and get instant answers

---

## 🖼️ Architecture

```text
[Frontend: HTML UI]
        │
        ▼
HTTP POST /query
        │
        ▼
[MCP Server: FastAPI]
        │
        ▼
[Ollama (LLaMA3)]
```

---

## Setup Instructions

1. Clone the Repo
2. Install the pre-requisited defined in requirements.txt file using the command "pip install -r requirements.txt"
3. Pull the model with ollama using the command: "ollama pull llama3"
4. Make sure ollama is running using the command: "ollama run llama3"
5. Run the MCP server using the command: "uvicorn mcp_server:app --reload --port 8000"
6. Run the HTML UI by opening the file "index.html"

---
## POST /query

Send a prompt to the local model and receive a response.

Request Body:
```
{
  "prompt": "What is the Newton's Third Law?"
}
```
Response:
```
Newton's Third Law of Motion, also known as the Law of Action and Reaction, states:......
```
---

## HTML UI

![screenshot1](https://github.com/imakshit/Local-MCP-Server-ChatBot/blob/main/screenshots/screenshot1.png)

---

## Further Ideas to improve the project

- Add support for more models
- Create a better UI
- Innovate and modify the code as per the specific use case

---

## 👋 Acknowledgments
- Ollama — for local model runtime
- Meta — for LLaMA3
- FastAPI — for easy backend
- Tailwind CSS — for clean styling

---
