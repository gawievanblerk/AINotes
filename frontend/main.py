import tkinter as tk
from tkinter import messagebox, simpledialog
import requests

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Taking App")
        self.notes = []

        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Text(self.root)
        self.text.pack()

        self.save_button = tk.Button(self.root, text="Save Note", command=self.save_note)
        self.save_button.pack()

        self.load_button = tk.Button(self.root, text="Load Notes", command=self.load_notes)
        self.load_button.pack()

    def save_note(self):
        note_content = self.text.get("1.0", tk.END).strip()
        if not note_content:
            messagebox.showwarning("Empty Note", "Note content cannot be empty")
            return

        note_title = simpledialog.askstring("Note Title", "Enter note title:")
        if not note_title:
            messagebox.showwarning("Empty Title", "Note title cannot be empty")
            return

        # Assuming user is authenticated and token is stored
        token = "YOUR_ACCESS_TOKEN_HERE"
        headers = {"Authorization": f"Bearer {token}"}
        data = {"id": len(self.notes) + 1, "title": note_title, "content": note_content, "tags": []}
        response = requests.post("http://localhost:8000/notes/", json=data, headers=headers)

        if response.status_code == 200:
            messagebox.showinfo("Success", "Note saved successfully")
            self.notes.append(data)
        else:
            messagebox.showerror("Error", "Failed to save note")

    def load_notes(self):
        # Assuming user is authenticated and token is stored
        token = "YOUR_ACCESS_TOKEN_HERE"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get("http://localhost:8000/notes/", headers=headers)

        if response.status_code == 200):
            self.notes = response.json()
            messagebox.showinfo("Notes", f"Loaded {len(self.notes)} notes")
        else:
            messagebox.showerror("Error", "Failed to load notes")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
