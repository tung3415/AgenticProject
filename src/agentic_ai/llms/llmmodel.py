from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

class LLMChatModel:
    
    def __init__(self, user_setup):
        self.user_setup = user_setup

    def get_llm(self):
        platform = self.user_setup["platform"]
        model = self.user_setup["model"]
        if platform == 'Groq':
            api_key = self.user_setup["GROQ_API_KEY"]
            base_url = "https://api.groq.com/openai/v1"
            return ChatOpenAI(api_key=api_key, model=model, base_url=base_url)
        elif platform=='Gemini':
            api_key = self.user_setup["GEMINI_API_KEY"]
            return ChatGoogleGenerativeAI(api_key=api_key, model=model)
        