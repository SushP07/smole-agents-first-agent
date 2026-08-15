import os
from dotenv import load_dotenv
from smolagents import CodeAgent, DuckDuckGoSearchTool, tool, GradioUI
from helpers.getActiveModel import get_active_model
from tools.tool_decorator import suggest_menu, catering_service_tool
import datetime

from langfuse import get_client
from openinference.instrumentation.smolagents import SmolagentsInstrumentor

# Load environment variables from .env into os.environ
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Authenticate Langfuse client
langfuse = get_client()

if langfuse.auth_check():
    print("✓ Langfuse client authenticated successfully!")
else:
    print("❌ Langfuse authentication failed. Check keys in .env.")

# 3. Instrument smolagents with OpenInference (Traces auto-export to Langfuse)
SmolagentsInstrumentor().instrument()




#DuckDuckGoSearchTool()




agent = CodeAgent(tools=[suggest_menu, catering_service_tool, DuckDuckGoSearchTool()], model=get_active_model())

# agent.run("""
#     Alfred needs to prepare for the party. Here are the tasks:
#     1. Prepare the drinks - 30 minutes
#     2. Decorate the mansion - 60 minutes
#     3. Set up the menu - 45 minutes
#     4. Prepare the music and playlist - 45 minutes

#     If we start right now, at what time will the party be ready?
#     """)


# Run the agent to find the best catering service
result = agent.run(
    "Can you give me the name of the highest-rated catering service in Gotham City?"
)

print(result)

# agent.push_to_hub('Sushrut0703/AlfredAgent', token=HF_TOKEN)
# GradioUI(agent).launch()
