## We will define tools with decorator which has simple functionality

from smolagents import CodeAgent, InferenceClientModel, tool
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Let's pretend we have a function that fetches the highest-rated catering services.
@tool
def catering_service_tool(query: str) -> str:
    """
    This tool returns the highest-rated catering service in Gotham City.

    Args:
        query: A search term for finding catering services.
    """
    # Example list of catering services and their ratings
    services = {
        "Gotham Catering Co.": 4.9,
        "Wayne Manor Catering": 4.8,
        "Gotham City Events": 4.7,
    }

    # Find the highest rated catering service (simulating search query filtering)
    best_service = max(services, key=services.get)

    return best_service

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


