# 🌍 AI-Powered Travel Planner Assistant

An intelligent, chat-based travel planning application that combines the power of **GPT-4o**, **real-time data tools**, and **user-friendly UI** to help you plan your trips effortlessly.

---

## 🧠 Features

- 💬 **Chat with AI Agent**: Plan your travel through interactive conversation powered by OpenAI's GPT-4o.
- 🌤️ **Weather Integration**: Get real-time weather forecasts using OpenWeatherMap.
- 💱 **Currency Converter**: View live currency exchange rates with Exchangerate-API.
- 📍 **Place Information Search**: Discover locations and travel destinations via TavilySearch.
- 🗂️ **Chat History**: View previous chat sessions and continue from where you left off.
- 🗑️ **Delete Chats**: Clean up or remove outdated sessions easily.
- 📄 **Download PDF**: Export your final travel plan as a downloadable PDF.

---

## 📸 Screenshots
<p align="center"> <img width="800" alt="Travel Planner Screenshot" src="https://github.com/user-attachments/assets/e2b81f74-3568-4ef7-a603-b86d76838459" /> </p>

---

## 🏗️ Tech Stack

| Layer | Technologies Used |
|-------|-------------------|
| 🧠 AI | [OpenAI GPT-4o](https://platform.openai.com/docs/models/gpt-4o), LangChain, LangGraph |
| 🌐 Frontend | [Streamlit](https://streamlit.io/) |
| 🔧 Backend | [FastAPI](https://fastapi.tiangolo.com/) |
| 🔌 Tools Integration | OpenWeatherMap, Exchangerate-API, TavilySearch |
| ⚙️ DevOps | LLMOps (ongoing development) |

---


## 📁 Project Structure

```
ai-travel-planner/
│                                                                                 
├── backend/                     # FastAPI backend
│   ├── app.py                   # FastAPI main app
│   ├── tools/                   # External API integration tools
│   └── ...
│
├── frontend/                    # Streamlit frontend
│   ├── streamlit_app.py         # Main UI logic
│   ├── utils/                   # Session, formatting, and helper functions
│   └── ...
│
├── .env.example                 # Sample environment file
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
└── setup.py                     # Setup configuration (for package installation)
```
---

## 📌 Roadmap

 Chat interface with GPT-4o
 Weather and currency integrations
 Session history & deletion
 PDF generation
 LLMOps monitoring, logging, and model versioning

---


## ⚙️ Setup Instructions

- Clone the Repository
```bash
git clone https://github.com/yourusername/ai-travel-planner.git
cd ai-travel-planner
```

- Set Up Environment
Create a .env file and add the following keys:
```bash
OPENAI_API_KEY=your_openai_key
OPENWEATHER_API_KEY=your_open_weather_key
EXCHANGE_RATE_API_KEY=your_exchange_rate_key
TAVILY_API_KEY=your_tavily_api_key
```
- install uv in cmd
```pip install uv```

- create the project folder
```uv init AI_Travel_Planner```
- it generate automatically some useful files...

- check python available virsions in uv
```uv python list```

- python specific virsion installation ... 
```uv python install cpython-3.11.0-windows-x86_64-none```  
- this not worked. so i tried this..
```uv venv --python=3.11```

- activate 
```.venv\Scripts\activate```

- install  a packege using uv
```uv pip install langchain```

- to see the current installed packeges
```uv pip list```

- to check the all commands that i have entered
```Get-History```

- install requirements
```uv pip install -r requirements.txt```

- change the setup.py file according to chatgpt.(because of an errer when installing requirements)

- to run
```streamlit run streamlit_app.py```
```uvicorn main:app --reload--port 8000 ```

---

## 🙌 Deployment part will be done with LLMops



