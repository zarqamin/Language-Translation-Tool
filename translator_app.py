import tkinter as tk
from tkinter import ttk, messagebox
import google.generativeai as genai

# Paste your Gemini API key here
API_KEY = "YOUR_API_KEY_HERE "

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash-lite")

languages = [
    "English",
    "Urdu",
    "Arabic",
    "French",
    "Spanish",
    "German",
    "Chinese",
    "Hindi",
    "Turkish"
]

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    source_lang = source_combo.get()
    target_lang = target_combo.get()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    try:
        prompt = f"Translate this text from {source_lang} to {target_lang}. Only give translated text:\n\n{text}"
        response = model.generate_content(prompt)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, response.text)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed:\n{e}")

def copy_text():
    translated = output_text.get("1.0", tk.END).strip()

    if translated == "":
        messagebox.showwarning("Warning", "No translated text to copy.")
        return

    root.clipboard_clear()
    root.clipboard_append(translated)
    messagebox.showinfo("Copied", "Translated text copied!")

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("650x550")
root.configure(bg="#f0f4f8")

title = tk.Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 20, "bold"),
    bg="#f0f4f8",
    fg="#1c3053"
)
title.pack(pady=15)

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack(pady=5)

tk.Label(frame, text="Source Language:", bg="#f0f4f8", font=("Arial", 11)).grid(row=0, column=0, padx=10)
source_combo = ttk.Combobox(frame, values=languages, state="readonly", width=20)
source_combo.set("English")
source_combo.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Target Language:", bg="#f0f4f8", font=("Arial", 11)).grid(row=0, column=2, padx=10)
target_combo = ttk.Combobox(frame, values=languages, state="readonly", width=20)
target_combo.set("Urdu")
target_combo.grid(row=0, column=3, padx=10)

tk.Label(root, text="Enter Text:", bg="#f0f4f8", font=("Arial", 12, "bold")).pack(anchor="w", padx=40, pady=5)

input_text = tk.Text(root, height=8, width=70, font=("Arial", 11))
input_text.pack(padx=40)

translate_btn = tk.Button(
    root,
    text="Translate",
    command=translate_text,
    bg="#1c3053",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15
)
translate_btn.pack(pady=15)

tk.Label(root, text="Translated Text:", bg="#f0f4f8", font=("Arial", 12, "bold")).pack(anchor="w", padx=40)

output_text = tk.Text(root, height=8, width=70, font=("Arial", 11))
output_text.pack(padx=40)

copy_btn = tk.Button(
    root,
    text="Copy Translation",
    command=copy_text,
    bg="#00897b",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18
)
copy_btn.pack(pady=15)

root.mainloop()