# 🔐 AES Encrypt/Decrypt Tool with GUI

A secure, user-friendly AES encryption and decryption tool built using Python and Tkinter. This application allows you to encrypt/decrypt text using a 256-bit key, generate new keys, and import existing key files — all through very simple graphical interface. 
This project is just for fun as i'd like to occassionally add improvements to it over time. The end goal would be a simple deployable application that a non-development based person could use with ease. Stay tuned!! 

---

## 🚀 Features

- 🧠 **Class-Based Architecture**  
  Modular design with clear separation of concerns (`AESUtils`, `KeyManager`, GUI runner)

- 🔐 **AES-256 CBC Encryption**  
  Secure message encryption/decryption using the PyCryptodome library

- 🗝️ **Key Management**  
  - Generate new 256-bit `.key` files  
  - Import existing key files via GUI

- 🖥️ **Graphical Interface**  
  - Text input/output fields for messages  
  - Dropdown for choosing operations: Encrypt, Decrypt, Generate Key, Import Key  
  - Drag-and-drop-like import experience (via file dialog)

---

## 📁 File Structure

```text
Encryption-project/
├── aes_utils.py        # Handles AES encryption and decryption
├── key_manager.py      # Key generation and validation logic
├── main.py             # GUI application using Tkinter
└── shared.key          # (Optional) Pre-generated 256-bit key file
