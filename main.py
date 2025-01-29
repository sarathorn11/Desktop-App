import tkinter as tk
from tkinter import ttk, messagebox

def on_button_click():
    messagebox.showinfo("Message", "Hello, Tkinter!")

# Create the main window
root = tk.Tk()
root.title("MULTI Tools KH V2.0")
root.geometry("800x500")

# Top Navigation Bar
nav_frame = tk.Frame(root, bg="blue", height=30)
nav_frame.pack(fill=tk.X)

# Manage LDPlayer9 Section
manage_frame = tk.Frame(root, padx=10, pady=5)
manage_frame.pack(fill=tk.X)

path_label = tk.Label(manage_frame, text="LDPlayer Path")
path_label.grid(row=0, column=0, padx=5, pady=5)

path_entry = tk.Entry(manage_frame, width=50)
path_entry.grid(row=0, column=1, padx=5, pady=5)

save_button = tk.Button(manage_frame, text="+ Save Path", bg="green", fg="white")
save_button.grid(row=0, column=2, padx=5, pady=5)

# Table
columns = ("No", "Device Name", "Status")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Action Buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, padx=10, pady=5)

refresh_button = tk.Button(button_frame, text="Refresh Table", bg="green", fg="white")
refresh_button.pack(side=tk.LEFT, padx=5)

deselect_button = tk.Button(button_frame, text="Deselect ALL", bg="blue", fg="white")
deselect_button.pack(side=tk.LEFT, padx=5)

start_button = tk.Button(button_frame, text="Start", bg="blue", fg="white")
start_button.pack(side=tk.LEFT, padx=5)

close_button = tk.Button(button_frame, text="Close", bg="red", fg="white")
close_button.pack(side=tk.LEFT, padx=5)

arrange_button = tk.Button(button_frame, text="Arrange", bg="orange", fg="white")
arrange_button.pack(side=tk.LEFT, padx=5)

ldmulti_button = tk.Button(button_frame, text="LDMultiPlayer", bg="yellow", fg="black")
ldmulti_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()