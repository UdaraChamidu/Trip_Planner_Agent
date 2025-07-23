# 🤖 Travel Assistant Agent with LangGraph + FastAPI + OpenAI and LLMOps (Ongoing)

This project implements an AI agent using **LangGraph**, **FastAPI**, and **OpenAI**, designed to handle complex user queries through an agentic workflow. The backend processes questions using a graph based reasoning flow and returns a natural language response.

---

## 🚀 Features

- ✅ Agentic reasoning via LangGraph
- ✅ OpenAI LLM integration (`gpt-4o`)
- ✅ FastAPI-powered backend with RESTful API
- ✅ Cross-Origin Resource Sharing (CORS) support.
- ✅ Automatically saves a visual representation of the agent's decision graph
- ✅ Easily extensible to other providers like Groq (currently disabled)

---

## ⚙️ Setup Instructions

### install uv in cmd
```pip install uv```

### create the project folder
```uv init AI_Travel_Planner```
- it generate automatically some useful files...

### check python available virsions in uv
```uv python list```

### python specific virsion installation ... 
```uv python install cpython-3.11.0-windows-x86_64-none```  
- this not worked. so i tried this..
```uv venv --python=3.11```

### activate 
```.venv\Scripts\activate```

### install  a packege using uv
```uv pip install langchain```

### to see the current installed packeges
```uv pip list```

### to check the all commands that i have entered
```Get-History```

## install requirements
```uv pip install -r requirements.txt```

- change the setup.py file according to chatgpt.(because of an errer when installing requirements)

## to run
```streamlit run streamlit_app.py```
```uvicorn main:app --reload--port 8000 ```


## Deployment part will be done with LLMops
