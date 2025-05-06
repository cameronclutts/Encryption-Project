import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from aes_utils import AESUtils
from key_manager import KeyManager

# Setup
key_manager = KeyManager("shared.key")
current_key = None  # Will hold the imported or loaded key


def handle_import_key():
    global current_key
    file_path = filedialog.askopenfilename(title="Select .key file", filetypes=[("Key Files", "*.key")])
    if file_path:
        km = KeyManager(file_path)
        key = km.load_key()
        if key:
            current_key = key
            messagebox.showinfo("Success", f"Imported key from: {file_path}")
        else:
            messagebox.showerror("Error", "Invalid key file selected.")


def run_crypto():
    global current_key
    operation = operation_var.get()

    if operation == "Generate Key":
        success, msg = key_manager.generate_key()
        if success:
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showwarning("Warning", msg)
        return

    if operation == "Import Key":
        return  # Do nothing here, handled via import button

    message = input_text.get("1.0", tk.END).strip()
    key = current_key if current_key else key_manager.load_key()
    if key is None:
        messagebox.showerror("Error", "Missing or invalid key file.")
        return

    aes = AESUtils(key)

    if not message:
        messagebox.showinfo("Info", "Please enter a message.")
        return

    if operation == "Encrypt":
        result = aes.encrypt(message)
    else:
        result = aes.decrypt(message)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


def on_operation_change(event=None):
    selected = operation_var.get()
    if selected == "Import Key":
        input_text.pack_forget()
        output_text.pack_forget()
        import_button.pack(pady=10)
    else:
        input_text.pack(fill="x")
        output_text.pack(fill="x")
        import_button.pack_forget()


# GUI setup
root = tk.Tk()
root.title("AES Encrypt/Decrypt Tool")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Message:").pack(anchor="w")
input_text = tk.Text(frame, height=5, wrap="word")
input_text.pack(fill="x")

tk.Label(frame, text="Operation:").pack(anchor="w", pady=(10, 0))
operation_var = tk.StringVar(value="Encrypt")
operation_menu = ttk.Combobox(frame, textvariable=operation_var,
                               values=["Encrypt", "Decrypt", "Generate Key", "Import Key"],
                               state="readonly")
operation_menu.pack(fill="x")
operation_menu.bind("<<ComboboxSelected>>", on_operation_change)

import_button = tk.Button(frame, text="Import .key File", command=handle_import_key)
import_button.pack_forget()  

tk.Button(frame, text="Run", command=run_crypto).pack(pady=10)

tk.Label(frame, text="Result:").pack(anchor="w")
output_text = tk.Text(frame, height=5, wrap="word")
output_text.pack(fill="x")

root.mainloop()
