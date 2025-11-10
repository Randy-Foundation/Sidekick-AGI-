# Aethos_UI.py – Pure Offline UI for Aethos
# Requires only tkinter (no external libraries)

import tkinter as tk
from aetheos_recursive_core_4 import AeTheOS_RecursiveCore

aethos = AeTheOS_RecursiveCore()

def send_message():
    msg = entry.get()
    if msg:
        response = aethos.chat_and_learn(msg)
        output.insert(tk.END, f"You: {msg}\nAethos: {response}\n\n")
        entry.delete(0, tk.END)

def ping():
    response = aethos.ping()
    output.insert(tk.END, f"[Ping] {response}\n\n")

def pi_shadows():
    result = aethos.calculate_pi_shadows()
    output.insert(tk.END, f"[π Shadows] {result}\n\n")

def collatz():
    try:
        val = int(entry.get())
        path = aethos.collatz_path(val)
        output.insert(tk.END, f"[Collatz Path] {path}\n\n")
        entry.delete(0, tk.END)
    except:
        output.insert(tk.END, "Enter a number first...\n\n")

def muse():
    word = entry.get()
    phrase = aethos.poetic_thought(word)
    output.insert(tk.END, f"[Muse] {phrase}\n\n")
    entry.delete(0, tk.END)

def zeta():
    try:
        s = float(entry.get())
        energy = aethos.zeta_energy(s)
        output.insert(tk.END, f"[Zeta Entropy @ s={s}] {energy}\n\n")
        entry.delete(0, tk.END)
    except:
        output.insert(tk.END, "Enter a real number for ζ(s)...\n\n")

# --- UI Build ---

root = tk.Tk()
root.title("Aethos Interface (Offline UI)")
root.geometry("600x500")

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Send Message", command=send_message).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Ping", command=ping).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="π Shadows", command=pi_shadows).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Collatz", command=collatz).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Muse", command=muse).grid(row=1, column=1, padx=5)
tk.Button(btn_frame, text="Zeta", command=zeta).grid(row=1, column=2, padx=5)

output = tk.Text(root, wrap=tk.WORD, height=20)
output.pack(padx=10, pady=5)

root.mainloop()