import streamlit as st 

from src.agentic_ai.uicomponent.streamlitapp.streamlit_app import StreamlitApp
from src.agentic_ai.llms.llmmodel import LLMChatModel
from src.agentic_ai.graph.graphbuilder import GraphBuilder
from langchain_core.messages import HumanMessage
from src.agentic_ai.uicomponent.streamlitapp.display_result import DisplayResultStreamlit
# UI and user_input
def langgraph_agentic_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """
    ui = StreamlitApp()
    ui.load_streamlit()
    user_setup = ui.get_user_setup()
    usecase = user_setup["usecase"]
    
    user_message = st.text_input("Enter your message: ")
    if user_message:
         # LLM
        llm_config = LLMChatModel(user_setup)
        llm = llm_config.get_llm()
        # Graph
        graphbuilder = GraphBuilder(llm)
        graph = graphbuilder.setup_graph(usecase)
        DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()




