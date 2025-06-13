from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
import os 
from dotenv import load_dotenv
load_dotenv()
def get_tools():
    """
    Return a list of tools 
    """
    tools = [TavilySearchResults(max_results=2)]
    return tools 

def create_tool_node(tools):
    """
    Create and return toolnode 
    """
    return ToolNode(tools=tools)