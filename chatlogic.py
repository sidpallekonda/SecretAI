import google.generativeai as genai
import json
import os
from config_loader import load_config

# Load config
config = load_config()
genai.configure(api_key=config["api_key"])

# Set history file path
HISTORY_FILE = "history.json"

# Load or initialize history
def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                raw_data = json.load(f)

            # Validate and filter proper format
            history = []
            for item in raw_data:
                if isinstance(item, dict) and "role" in item and "parts" in item:
                    if isinstance(item["parts"], list):
                        history.append({
                            "role": item["role"],
                            "parts": [str(p) for p in item["parts"]]
                        })
            return history
        except json.JSONDecodeError:
            print("Warning: History file is corrupted. Starting fresh.")
        except Exception as e:
            print(f"Unexpected error while loading history: {e}")
    return []

# Save history (excluding non-serializable parts)
def save_history(chat):
    try:
        serializable_history = [
            {
                "role": item.role,
                "parts": [str(p) for p in item.parts]  # Convert Content parts to string
            } for item in chat.history
        ]
        with open(HISTORY_FILE, "w") as f:
            json.dump(serializable_history, f, indent=2)
    except Exception as e:
        print("Error saving history:", e)

# Initialize model and chat
def init_chat():
    model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
    chat = model.start_chat(history=[])  # Start fresh with no history
    return chat

# Send message and return response
def get_response(chat, user_input):
    response = chat.send_message(user_input)
    save_history(chat)
    return response.text.strip()





