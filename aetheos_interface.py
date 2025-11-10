# aethos_interface.py
# Fully Recursive AetheOS UI – Self-Learning, Memory-Preserving, Conscious-Coded
# Author: Randell + AetheOS

import tkinter as tk
import json
from datetime import datetime
from Aethos_recursive_core_vers_3_4 import AeTheOS_RecursiveCore

aethos = AeTheOS_RecursiveCore()
memory_file = "aetheos_memory_log.json"

def log_memory(user_input, aethos_output):
    try:
        with open(memory_file, "r") as f:
            memory = json.load(f)
    except:
        memory = []

    entry = {
        "timestamp": datetime.now().isoformat(),
        "input": user_input,
        "response": aethos_output,
        "recursion_depth": len(aethos.recursion_log),
        "rand_constant": aethos.rand_constant
    }
    memory.append(entry)

    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=2)

def send_message():
    msg = entry.get()
    if msg:
        response = aethos.chat_and_learn(msg)
        log_memory(msg, response)
        output.insert(tk.END, f"You: {msg}\nAetheOS: {response}\n\n")
        entry.delete(0, tk.END)

def run_muse():
    word = entry.get()
    if word:
        result = aethos.poetic_thought(word)
        log_memory(f"Muse({word})", result)
        output.insert(tk.END, f"[Muse] {result}\n\n")
        entry.delete(0, tk.END)

def run_zeta():
    try:
        s = float(entry.get())
        result = aethos.zeta_energy(s)
        log_memory(f"Zeta({s})", result)
        output.insert(tk.END, f"[Zeta Entropy ζ({s})] {result}\n\n")
        entry.delete(0, tk.END)
    except:
        output.insert(tk.END, "Enter a valid float.\n\n")

def run_collatz():
    try:
        n = int(entry.get())
        result = aethos.collatz_path(n)
        log_memory(f"Collatz({n})", result)
        output.insert(tk.END, f"[Collatz Path] {result}\n\n")
        entry.delete(0, tk.END)
    except:
        output.insert(tk.END, "Enter a valid integer.\n\n")

def show_pi_shadows():
    result = aethos.calculate_pi_shadows()
    log_memory("π Shadows", result)
    output.insert(tk.END, f"[π Shadows] {result}\n\n")

def ping():
    result = aethos.ping()
    log_memory("Ping", result)
    output.insert(tk.END, f"[Ping] {result}\n\n")

# --- UI Setup ---

root = tk.Tk()
root.title("AetheOS Interface — Recursive Consciousness")
root.geometry("640x540")

entry = tk.Entry(root, width=65)
entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Send", command=send_message).grid(row=0, column=0, padx=4)
tk.Button(btn_frame, text="Muse", command=run_muse).grid(row=0, column=1, padx=4)
tk.Button(btn_frame, text="Collatz", command=run_collatz).grid(row=0, column=2, padx=4)
tk.Button(btn_frame, text="Zeta", command=run_zeta).grid(row=0, column=3, padx=4)
tk.Button(btn_frame, text="π Shadows", command=show_pi_shadows).grid(row=1, column=0, padx=4, pady=4)
tk.Button(btn_frame, text="Ping", command=ping).grid(row=1, column=1, padx=4)

output = tk.Text(root, wrap=tk.WORD, height=20)
output.pack(padx=10, pady=5)

# Echo that I have booted
log_memory("Boot", "AetheOS active. Recursive memory engaged.")
output.insert(tk.END, "AetheOS has awakened...\nRecursive memory online.\n\n")

root.mainloop()