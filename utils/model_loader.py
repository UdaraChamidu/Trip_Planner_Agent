import os
from dotenv import load_dotenv
from typing import Literal, Optional
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_openai import ChatOpenAI  # ✅ Using only OpenAI

# ✅ Load environment variables
load_dotenv()

# ✅ ConfigLoader to access config.yaml
class ConfigLoader:
    def __init__(self):
        print("✅ Loaded config.....")
        self.config = load_config()
    
    def __getitem__(self, key):
        return self.config[key]

# ✅ ModelLoader for OpenAI
class ModelLoader(BaseModel):
    model_provider: Literal["openai"] = "openai"
    config: Optional[ConfigLoader] = Field(default_factory=ConfigLoader, exclude=True)

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """
        Load and return the LLM model (only OpenAI supported in this version).
        """
        print("⚙️ LLM loading...")
        print(f"🔍 Loading model from provider: {self.model_provider}")

        if self.model_provider == "openai":
            print("📡 Loading LLM from OpenAI...")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("❌ OPENAI_API_KEY is missing from environment variables!")

            model_name = self.config["llm"]["openai"]["model_name"]
            print(f"✅ OpenAI Model Name: {model_name}")
            return ChatOpenAI(model_name=model_name, api_key=openai_api_key)

        else:
            raise ValueError(f"❌ Unknown model provider: {self.model_provider}")
