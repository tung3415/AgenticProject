from src.agentic_ai.state.state import State

class ChatbotNode:
    
    def __init__(self, llm):
        self.llm=llm

    def chatbot_node(self, state: State) -> State:
        return {"messages": [self.llm.invoke(state["messages"])]}