from langgraph.graph import StateGraph, START, END
from src.agentic_ai.nodes.llm_node import ChatbotNode
from src.agentic_ai.state.state import State
# from langgraph.checkpoint.memory import InMemorySaver
from src.agentic_ai.tool.search_tool import get_tools
from src.agentic_ai.tool.search_tool import create_tool_node
from langgraph.prebuilt import tools_condition
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

    def graph_tool(self):
        """
        Create graph tool 
        """
        # Define tool_node 
        tools = get_tools()
        tool_node = create_tool_node(tools)
        # Define llm_node 
        self.llm_with_tools = self.llm.bind_tools(tools)
        def chatbot(state: State):
            return {"messages": [self.llm_with_tools.invoke(state["messages"])]}
        # Graph add 
        self.graph_builder.add_node("chatbot", chatbot)
        self.graph_builder.add_node("tools", tool_node)
        # add edge 
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")

    def setup_graph(self, usecase):
        if usecase == "Chatbot":
            self.build_chatbot_graph()
        if usecase == "Agentic Tool":
            self.graph_tool()
        return self.graph_builder.compile()