import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API key from .env
load_dotenv()

def generate():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    # Prompt user for input
    user_input = input("Ask about a food recipe: ").strip().lower()

    # Basic keyword filter to allow only food-related prompts
    food_keywords = [
        "recipe", "ingredients", "cook", "bake", "grill", "fry",
        "dish", "cuisine", "meal", "dessert", "food", "snack", "starter","make"
    ]

    if not any(keyword in user_input for keyword in food_keywords):
        print("❌ I don't know anything about this. Please ask questions related to food recipes only.")
        return

    # Set up Gemini client
    client = genai.Client(
        api_key=api_key,
    )

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_input),
            ],
        ),
    ]
    tools = [
        types.Tool(
            googleSearch=types.GoogleSearch()
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        tools=tools,
    )

    # Generate response stream
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
