# 🤖 Pronto ERP Agentic Chatbot using Groq LLM & FastAPI

This project is an intelligent agent interface designed to interact with **Pronto ERP** systems using natural language queries. It combines the power of **Groq’s ultra-fast LLM inference**, **LangGraph's tool-based agent architecture**, and the simplicity of **FastAPI** to deliver real-time, accurate ERP data through an AI chatbot interface.

---

## 🧠 Project Overview

At its core, this system enables users to **query ERP data conversationally**. Instead of navigating through complex ERP dashboards or writing manual reports, users can simply type requests like:

> “What’s the wholesale price for item ABC in region 400?”
> “How many units are in stock at warehouse WH01?”
> “List all recent sales orders for product XYZ.”

The system processes the input, intelligently determines which tools (APIs) to call using a **LangGraph agent**, and streams back the result in real-time via **FastAPI's server-sent events (SSE)**.

---

## 🔧 Architecture & Flow

1. **User Input**
   A message is sent to the `/chat` endpoint containing a natural language prompt.

2. **LLM Reasoning via LangGraph Agent**
   The prompt is handled by a **LangGraph React Agent** powered by **Groq's Qwen-32B model**, which decides:

   * What the user is asking
   * Which tool (ERP API wrapper) to invoke
   * What parameters to extract and pass

3. **Tool Execution**
   The selected tool (like `get_item_prices`, `get_item_warehouses`, etc.) is invoked using structured inputs.

4. **Response Streaming**
   The results are streamed back to the user line by line using FastAPI’s async generator.

---

## 🚀 Key Features

### 🔄 Real-time Streaming API

* Supports SSE for progressive token-level streaming response.
* Instant feedback and fluid interaction.

### 🧰 LangGraph + LangChain Tool Agent

* Structured tool execution using `create_react_agent`.
* Tools defined with LangChain’s `@tool` decorator.

### ⚡ Groq API Integration

* Utilizes Groq’s blazing-fast inference for the Qwen-32B LLM.
* Fast responses even with large models.

### 🔗 ERP Toolset

* Interfaces with **Pronto Cloud’s ERP REST APIs**.
* Automatically handles login, access tokens, headers, and payload formatting.

---

## 📂 Project Structure

```plaintext
.
├── app.py                     # FastAPI app and /chat endpoint
├── main.py                    # Launch script for running the API server
├── graph.py                   # LangGraph agent logic and definition
├── tools.py                   # ERP API tool wrappers (get_item_prices, get_sales_orders, etc.)
├── pronto_agentic_groq_qwen.ipynb  # Jupyter notebook demo (optional)
└── requirements.txt           # Project dependencies
```

---

## 🧰 ERP Tools Implemented

| Tool Name             | Purpose                                           |
| --------------------- | ------------------------------------------------- |
| `get_access_token`    | Logs in and retrieves session token               |
| `get_item_prices`     | Fetches wholesale prices for items with filtering |
| `get_item_attributes` | Retrieves item attributes like color, size, type  |
| `get_all_item_prices` | Gets comprehensive pricing details                |
| `get_item_warehouses` | Fetches stock quantity across warehouses          |
| `get_sales_orders`    | Lists sales order details for a given item        |

Each tool calls a specific Pronto ERP REST endpoint and formats the response before returning it to the user.

---

## 🖥️ Usage Instructions

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/your-org/pronto-agent-groq.git
cd pronto-agent-groq
pip install -r requirements.txt
```

### 2. Run the API Server

```bash
python main.py
```

The server starts at: `http://localhost:8001`

---

## 🔌 Example API Call

### Endpoint:

```http
POST /chat
```

### Request:

```json
{
  "message": "Check price for item ABC in region 100"
}
```

### Response (Streamed):

```
data: {"content": "Calling get_item_prices..."}
data: {"content": "Item ABC costs $25.30 in region 100"}
data: [DONE]
```

Test it using curl:

```bash
curl -X POST http://localhost:8001/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Check warehouse stock for item 1234"}'
```

---

## 🧠 Behind the Scenes

* **Token Streaming**: Utilizes `async def` and `yield` in FastAPI to support server-sent events.
* **Tool Reasoning**: LangGraph allows the agent to reason over a toolset and dynamically pick which function to call.
* **Model Choice**: The Qwen-32B model provides long context and strong multilingual capability with high inference speed using Groq.

---

## 🛡️ Security Notes

* The current setup assumes testing or internal use. In production:

  * Secure the `/chat` endpoint.
  * Store and manage credentials (e.g. API tokens) securely.
  * Handle sensitive data responsibly.

---

## 🧪 Future Improvements

* ✅ Add memory/context window for conversation continuity
* ✅ Dockerize for easy deployment
* 🔄 Add logging, monitoring, and retry logic for API tools
* 🌐 Web UI for real-time testing
* 🔐 OAuth/token refresh handling for Pronto APIs
* 💬 Multilingual support and translation
