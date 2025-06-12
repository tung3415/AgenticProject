import streamlit as st 

from src.agentic_ai.ui_component.frontend_streamlit.loadui import LoadStreamlitUI

# UI and user_input
def langgraph_agentic_app():
    """
    Frontend and Backend
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """
    ui = LoadStreamlitUI()
    ui.load_streamlit_ui()
    
    user_message = st.text_input("Enter your message: ")


