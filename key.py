from dotenv import load_dotenv
import os

# Explicitly load the .env file
load_dotenv()

# Check if the API key is being loaded
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API Key successfully loaded!")
    print(f"API Key: {api_key[:4]}...")  # Partial key for debugging
else:
    print("API Key not found. Ensure the .env file is set up correctly.")
