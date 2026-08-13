import os
from dotenv import load_dotenv
from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel, tool, LiteLLMModel
from helpers.getActiveModel import get_active_model
import datetime

# Load environment variables from .env into os.environ
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")



# Tool to suggest a menu based on the occasion and dietary preferences

@tool
def suggest_menu(occasion: str) -> str:
    """
        Suggests a menu based on the occasion and dietary preferences.
        Args:
            occasion (str): The occasion for which the menu is being planned. Allowed values are:
                - "Casual Dinner" : Menu for Casual Party
                - "Formal Dinner" : Menu for Formal Party
                - "Birthday Party" : Menu for Birthday Party
                - "SuperHero Party" : Menu for Superhero Party
                - "Custom" : "Custom menu based on user input"
            """

    if occasion == "Casual Dinner":
        return "Menu for Casual Dinner: Grilled Chicken, Caesar Salad, Garlic Bread, Lemonade."
    elif occasion == "Formal Dinner":
        return "Menu for Formal Dinner: Beef Wellington, Roasted Vegetables, Truffle Mashed Potatoes, Red Wine."
    elif occasion == "Birthday Party":
        return "Menu for Birthday Party: Pizza, Chicken Wings, Veggie Platter, Birthday Cake."
    elif occasion == "SuperHero Party":
        return "Menu for Superhero Party: Hero Sandwiches, Power Smoothies, Superfruit Salad, Themed Cupcakes."
    elif occasion == "Custom":
        return "Custom menu based on user input."
    else:
        return "Invalid occasion. Please choose from 'Casual Dinner', 'Formal Dinner', 'Birthday Party', 'SuperHero Party', or 'Custom'."

#DuckDuckGoSearchTool()




agent = CodeAgent(tools=[suggest_menu, DuckDuckGoSearchTool()], model=get_active_model())

agent.run("""
    Alfred needs to prepare for the party. Here are the tasks:
    1. Prepare the drinks - 30 minutes
    2. Decorate the mansion - 60 minutes
    3. Set up the menu - 45 minutes
    4. Prepare the music and playlist - 45 minutes

    If we start right now, at what time will the party be ready?
    """)

agent.push_to_hub('Sushrut0703/AlfredAgent', token=HF_TOKEN)

