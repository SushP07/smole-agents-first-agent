
from smolagents import InferenceClientModel, LiteLLMModel
import os
from dotenv import load_dotenv

# Load environment variables from .env into os.environ
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def get_active_model():
    """
    Attempts to initialize and test the Hugging Face model first.
    Falls back to Google Gemini via LiteLLMModel if HF fails.
    """
    print("Attempting to connect with Hugging Face (Primary)...")
    try:
        hf_model = InferenceClientModel()
        
        # Test probe call: Verify quota and endpoint status before running agent
        hf_model([{"role": "user", "content": "ping"}])
        print("✓ Successfully connected to Hugging Face model.\n")
        return hf_model

    except Exception as e:
        print(f"⚠️ Hugging Face failed (Reason: {e}). Switching to Gemini fallback...")
        gemini_model = LiteLLMModel(
            model_id="gemini/gemini-2.5-flash",
            api_key=GEMINI_API_KEY
        )
        print("✓ Connected to Gemini API fallback.\n")
        return gemini_model