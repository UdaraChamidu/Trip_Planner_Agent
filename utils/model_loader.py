import os
from dotenv import load_dotenv
from typing import Literal, Optional
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()

class ConfigLoader:
    def __init__(self):
        print(f"Loaded config.....")
        self.config = load_config()
    
    def __getitem__(self, key):
        return self.config[key]

class ModelLoader(BaseModel):
    model_provider: Literal["groq", "openai"] = "groq"
    config: Optional[ConfigLoader] = Field(default_factory=ConfigLoader, exclude=True)

    class Config:
        arbitrary_types_allowed = True
    
    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")
        
        if self.model_provider == "groq":
            print("Loading LLM from Groq..............")
            groq_api_key = os.getenv("GROQ_API_KEY")
            if not groq_api_key:
                raise ValueError("❌ GROQ_API_KEY is missing from environment!")
            model_name = self.config["llm"]["groq"]["model_name"]
            print("✅ Groq Model Name:", model_name)
            return ChatGroq(model=model_name, api_key=groq_api_key)

        elif self.model_provider == "openai":
            print("Loading LLM from OpenAI..............")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("❌ OPENAI_API_KEY is missing from environment!")
            model_name = self.config["llm"]["openai"]["model_name"]
            print("✅ OpenAI Model Name:", model_name)
            return ChatOpenAI(model_name=model_name, api_key=openai_api_key)

        else:
            raise ValueError(f"Unknown model provider: {self.model_provider}")
