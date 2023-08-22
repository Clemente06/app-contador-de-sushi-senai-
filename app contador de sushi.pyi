import tkinter as tk
from tkinter import ttk

# Função para atualizar um contador específico
def update_counter(value, counter_label):
    current_value = int(counter_label['text'])
    new_value = current_value + value
    counter_label['text'] = str(new_value)
    update_general_counter(value)

# atualizar o cg
def update_general_counter(value):
    general_counter['text'] = str(int(general_counter['text']) + value)

# reset
def reset_counters():
    for label in section_counters.values():
        label['text'] = "0"
    general_counter['text'] = "0"

# janela princ
root = tk.Tk()
root.title("Contador de Sushi")
root.configure(bg="white")  # Define a cor de fundo da janela para branco

# cg
general_counter = tk.Label(root, text="0", font=("Helvetica", 18), bg="white")
general_counter.pack(anchor=tk.NE, padx=10, pady=10)

# notebook
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10)

section_counters = {}

sushi_types = [
    "Niguiri", "Uramaki", "Hossomaki", "Hot Roll", "Sashimi", "Temaki"
]

# notebook abas
for sushi_type in sushi_types:
    section_frame = ttk.Frame(notebook)
    notebook.add(section_frame, text=sushi_type)

    section_label = tk.Label(section_frame, text=sushi_type, font=("Helvetica", 12), bg="white")
    section_label.pack(padx=10, pady=5)

    section_counter = tk.Label(section_frame, text="0", font=("Helvetica", 24), bg="white")
    section_counter.pack(padx=10, pady=5)
    section_counters[sushi_type] = section_counter

    section_increment_button = tk.Button(section_frame, text="+", command=lambda t=sushi_type: update_counter(3 if t == "Temaki" else 1, section_counters[t]), bg="green", fg="white")
    section_increment_button.pack(padx=10, pady=5)

    section_decrement_button = tk.Button(section_frame, text="-", command=lambda t=sushi_type: update_counter(-3 if t == "Temaki" else -1, section_counters[t]), bg="red", fg="white")
    section_decrement_button.pack(padx=10, pady=5)

# reset
reset_button = tk.Button(root, text="Reset", command=reset_counters, bg="blue", fg="white")
reset_button.pack(padx=10, pady=10)

# loop
root.mainloop()
