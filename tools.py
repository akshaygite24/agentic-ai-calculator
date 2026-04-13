from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """
    Use this tool for solving math expression like:
    2+3, 10*5, 100/2
    """
    try:
        return str(eval(expression))
    except:
        return "Error in calculation"