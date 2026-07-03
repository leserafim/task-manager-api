# Task Management API

A RESTful Task Management API built with Python, FastAPI, and Pydantic, featuring full CRUD functionality and automatic Swagger documentation.

---

## 🚀 Features

* **Full CRUD Operations**: Create, Read, Update, and Delete tasks seamlessly.
* **Strict Data Validation**: Powered by Pydantic to enforce data integrity and catch malformed payloads early.
* **Auto-Generated Documentation**: Instant access to interactive API testing via Swagger UI.
* **Asynchronous Architecture**: Built using Python's async/await paradigms for high-performance handling.

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Pydantic**
* **Uvicorn** (ASGI Server)

## 📦 Installation and Setup

### 1. Clone the repository
'''bash
git clone [https://github.com/leserafim/task-manager-api.git](https://github.com/leserafim/task-manager-api.git)
cd task-manager-api
2. Set up the Virtual Environment
Bash
python -m venv venv
3. Activate the Environment
Windows (PowerShell):

PowerShell
.\venv\Scripts\Activate.ps1
Linux/macOS:

Bash
source venv/bin/activate
4. Run the Development Server
Bash
uvicorn main:app --reload
The server will start locally at http://127.0.0.1:8000.

🔍 API Testing
Once the server is running, you can access the interactive API documentation to test all endpoints:
👉 Swagger UI: http://127.0.0.1:8000/docs

🧠 Development Process & AI Collaboration
This project was developed using modern, accelerated engineering methodologies. It features active collaboration with generative AI operating as an advanced Code Reviewer and architectural partner. This synergy was leveraged to validate industry best practices, optimize async route performance, and ensure strict repository hygiene through precise Git versioning control.

👤 Author
Leandro Serafim - Backend & Infrastructure Explorer
