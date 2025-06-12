import streamlit as st 
from src.agentic_ai.uicomponent.uiconfig import Config

class StreamlitApp:
    def __init__(self):
        self.config=Config()
        self.user_setup={}

    def load_streamlit(self):
        st.set_page_config(page_title="🤖 "+ self.config.get_pagetitle(), layout="wide")
        st.header("🤖 " + self.config.get_pagetitle())

        with st.sidebar:
            # Get Platform
            platform_options = self.config.get_platform_options()
            self.user_setup["platform"] = st.selectbox("Select Platform: ", platform_options)

            # Get Model, API_KEY
            if self.user_setup["platform"] == "Groq":
                # Model
                model_options = self.config.get_groq_model_options()
                self.user_setup["model"]=st.selectbox("Select Model:", model_options)
                # API_KEY
                self.user_setup["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input("API Key",type="password")
                if not self.user_setup["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
            elif self.user_setup["platform"] == "Gemini":
                # Model
                model_options = self.config.get_gemini_model_options()
                self.user_setup["model"]=st.selectbox("Select Model:", model_options)
                # API_KEY
                self.user_setup["GEMINI_API_KEY"] = st.session_state["GEMINI_API_KEY"]=st.text_input("API Key",type="password")
            # Get usecase 
            usecase_options = self.config.get_usecase_options()
            self.user_setup["usecase"]=st.selectbox("Select Use Case:", usecase_options)   

    def get_user_setup(self):
        return self.user_setup