import tkinter as tk
from tkinter import scrolledtext
from chatlogic import get_response, init_chat, load_history

def launch_gui():
    root = tk.Tk()
    root.title("SecretAI")
    root.geometry("600x600")
    root.configure(bg="#1e1e1e")

    chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#1d1d1d", fg="white", font=("Arial", 10))
    chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    chat_area.insert(tk.END, "                                I'm a GEMINIIIUH *insert blond whitegirl noises*\n\n")

    entry = tk.Entry(root, bg="#0E0E0D", fg="white", insertbackground="white", font=("Arial", 10))
    entry.pack(padx=10, pady=5, fill=tk.X)

    chat = init_chat()

    # Load previous history into chat_area
    try:
        history = load_history()
        for msg in history:
            role = msg.get("role", "")
            parts = msg.get("parts", [])
            text = " ".join(str(p) for p in parts)
            if role == "user":
                chat_area.insert(tk.END, f"You: {text}\n")
            else:
                chat_area.insert(tk.END, f"Gemini: {text}\n\n")
    except Exception as e:
        chat_area.insert(tk.END, f"[Error loading history: {e}]\n\n")

    def on_send():
        user_input = entry.get()
        if not user_input.strip():
            return
        chat_area.insert(tk.END, f"You: {user_input}\n")
        entry.delete(0, tk.END)
        try:
            reply = get_response(chat, user_input)
            chat_area.insert(tk.END, f"Gemini: {reply}\n\n")
        except Exception as e:
            chat_area.insert(tk.END, f"Error: {str(e)}\n\n")

    entry.bind("<Return>", lambda event: on_send())

    send_btn = tk.Button(root, text="Send", command=on_send)
    send_btn.pack(pady=5)

    root.mainloop()




