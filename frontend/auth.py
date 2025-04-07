import requests
import webbrowser
import tkinter as tk
from urllib.parse import urlencode
from tkinter import messagebox, simpledialog

class GoogleAuth:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token = None

    def authenticate(self):
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": "openid email profile",
            "access_type": "offline",
            "prompt": "consent"
        }
        auth_url = "https://accounts.google.com/o/oauth2/auth?" + urlencode(params)
        webbrowser.open(auth_url)

        # Wait for user to input the auth code
        auth_code = simpledialog.askstring("Authorization Code", "Enter the authorization code:")
        if not auth_code:
            messagebox.showerror("Error", "Authorization code is required")
            return

        # Exchange auth code for tokens
        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "code": auth_code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "grant_type": "authorization_code"
        }
        response = requests.post(token_url, data=data)
        if response.status_code == 200):
            self.token = response.json().get("access_token")
            messagebox.showinfo("Success", "Authentication successful")
        else:
            messagebox.showerror("Error", "Failed to authenticate")

if __name__ == "__main__":
    root = tk.Tk()
    auth = GoogleAuth(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", redirect_uri="YOUR_REDIRECT_URI")
    auth.authenticate()
    root.mainloop()
