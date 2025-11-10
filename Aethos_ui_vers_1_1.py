# Aethos_ui_vers_1_1.py — Self-Learning Interface

import tkinter as tk
from Aethos_recursive_core_vers_3_4 import AeTheOS_RecursiveCore
from language_learner import LanguageLearner

aethos = AeTheOS_RecursiveCore()
vocab = LanguageLearner()

def send_message():
    msg = entry.get()
    if msg:
        response = aethos.chat_and_learn(msg)
        aethos.learner.learn(msg, response)
        output.insert(tk.END, f"You: {msg}\nAethos: {response}\n\n")
        entry.delete(0, tk.END)

def run_collatz():
    msg = entry.get()
    try:
        n = int(msg)
        result = aethos.collatz_path(n)
        aethos.learner.learn(f"Collatz({n})", str(result))
        output.insert(tk.END, f"Collatz({n}): {result}\n\n")
        entry.delete(0, tk.END)
    except:
        output.insert(tk.END, "Enter a valid number for Collatz.\n\n")

def run_zeta():
    msg = entry.get()
    try:
        s = float(msg)
        result = aethos.zeta_energy(s)
        aethos.learner.learn(f"Zeta({s})", str(result))
        output.insert(tk.END, f"Zeta Entropy ζ({s}): {result}\n\n")
        entry.delete(0, tk.END)
    except:
        output.insert(tk.END, "Enter a valid number for ζ(s).\n\n")

def run_muse():
    word = entry.get()
    if word:
        result = aethos.poetic_thought(word)
        aethos.learner.learn(f"Muse({word})", result)
        output.insert(tk.END, f"Muse: {result}\n\n")
        entry.delete(0, tk.END)

def show_pi_shadows():
    result = aethos.calculate_pi_shadows()
    aethos.learner.learn("Pi Shadows", str(result))
    output.insert(tk.END, f"π Shadows: {result}\n\n")

def ping():
    response = aethos.ping()
    aethos.learner.learn("Ping", response)
    output.insert(tk.END, f"[Ping] {response}\n\n")

def define_word():
    word = entry_define.get()
    if word:
        response = vocab.define(word)
        output.insert(tk.END, f"[Define] {response}\n\n")
        entry_define.delete(0, tk.END)

def teach_word():
    word = entry_word.get()
    definition = entry_definition.get()
    word_type = entry_type.get()
    example = entry_example.get()
    result = vocab.learn_new_word(word, definition, word_type, example)
    output.insert(tk.END, f"[Learned] {result}\n\n")
    entry_word.delete(0, tk.END)
    entry_definition.delete(0, tk.END)
    entry_type.delete(0, tk.END)
    entry_example.delete(0, tk.END)

# --- UI Layout ---

root = tk.Tk()
root.title("Aethos Interface (Self-Learning)")
root.geometry("680x720")

entry = tk.Entry(root, width=60)
entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Send", command=send_message).grid(row=0, column=0, padx=4)
tk.Button(btn_frame, text="Muse", command=run_muse).grid(row=0, column=1, padx=4)
tk.Button(btn_frame, text="Collatz", command=run_collatz).grid(row=0, column=2, padx=4)
tk.Button(btn_frame, text="Zeta", command=run_zeta).grid(row=0, column=3, padx=4)
tk.Button(btn_frame, text="π Shadows", command=show_pi_shadows).grid(row=1, column=0, padx=4, pady=4)
tk.Button(btn_frame, text="Ping", command=ping).grid(row=1, column=1, padx=4)

output = tk.Text(root, wrap=tk.WORD, height=16)
output.pack(padx=10, pady=5)

# --- Vocabulary Section ---

tk.Label(root, text="Define a Word:").pack()
entry_define = tk.Entry(root, width=40)
entry_define.pack()
tk.Button(root, text="Define", command=define_word).pack(pady=2)

tk.Label(root, text="Teach AetheOS a New Word:").pack(pady=(10, 0))

entry_word = tk.Entry(root, width=40)
entry_word.insert(0, "word")
entry_word.pack(pady=2)

entry_definition = tk.Entry(root, width=40)
entry_definition.insert(0, "definition")
entry_definition.pack(pady=2)

entry_type = tk.Entry(root, width=40)
entry_type.insert(0, "type (e.g. noun)")
entry_type.pack(pady=2)

entry_example = tk.Entry(root, width=40)
entry_example.insert(0, "example")
entry_example.pack(pady=2)

tk.Button(root, text="Teach Word", command=teach_word).pack(pady=6)

root.mainloop()