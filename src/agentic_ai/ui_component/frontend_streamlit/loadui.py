import streamlit as st 
from src.agentic_ai.ui_component.uiconfig import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}
    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 "+ self.config.get_pagetitle(), layout="wide")
        st.header("🤖 " + self.config.get_pagetitle())

        with st.sidebar:
            # Get option from config 
            platform_options = self.config.get_platform_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls["selected_platform"] = st.selectbox("Select Platform", platform_options)

            # Get Model 
            if self.user_controls["selected_platform"]=="Groq":
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_model"]=st.selectbox("Select Model:", model_options)

                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input("API Key",type="password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
            
            # Get usecase 
            self.user_controls["selected_usecase"]=st.selectbox("Select Use Case:", self.config.get_usecase_options())            