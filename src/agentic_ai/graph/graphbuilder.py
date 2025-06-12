from langgraph.graph import StateGraph, START, END
from src.agentic_ai.nodes.llm_node import ChatbotNode
from src.agentic_ai.state.state import State

class GraphBuilder:
    
    def __init__(self, llm):
        self.llm = llm
        self.graph_builder = StateGraph(State)
    
    def build_chatbot_graph(self):
        self.chatbot = ChatbotNode(self.llm)
        # add node 
        self.graph_builder.add_node("chatbot", self.chatbot.chatbot_node)
        # add edge 
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase):
        if usecase == "Basic Chatbot":
            self.build_chatbot_graph()
        
        return self.graph_builder.compile()