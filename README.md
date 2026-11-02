# python_to_gdrive_sync

A Python tool to sync local files and folders with Google Drive.

> 🚧 **Work in progress** — the project is just getting started.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/BerlynDev/python_to_gdrive_sync.git
   cd python_to_gdrive_sync
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```
3. Put your Google API credentials (e.g. `client_secret.json`) in the `credentials/` folder.

## Credentials

Everything inside `credentials/` is ignored by Git (only the `.gitkeep` placeholder is tracked),
so your secrets and tokens never get committed. **Never** commit credential files.
