# AINotes

AINotes is a simple note-taking application built with Python. It uses Tkinter for the UI and FastAPI for the backend. The application supports Google Auth for authentication.

## Features

- User Authentication with Google Auth
- Create, Read, Update, Delete (CRUD) operations for notes
- Basic note management with tags and search functionality
- Responsive design for different devices
- Secure note storage with encryption

## Installation

1. Clone the repository:

```bash
git clone https://github.com/gawievanblerk/AINotes.git
cd AINotes
```

2. Install the dependencies:

```bash
pip3 install -r requirements.txt
```

3. Run the backend server:

```bash
cd backend
uvicorn main:app --reload
```

4. Run the frontend application:

```bash
cd frontend
python3 main.py
```

## Configuration

To configure Google Auth, you need to create a project in the Google Cloud Console and obtain the `client_id`, `client_secret`, and `redirect_uri`. Replace the placeholders in `frontend/auth.py` with your values.

## Usage

1. Run the backend server and frontend application as described in the installation steps.
2. Use the UI to create, read, update, and delete notes.
3. Authenticate with Google to secure your notes.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to contribute.

## License

This project is licensed under the MIT License.
