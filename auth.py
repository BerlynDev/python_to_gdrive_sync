# Path: builds file/folder paths that work on any OS (Windows, Linux, macOS)
from pathlib import Path

# Request: lets the Google library make HTTP calls (e.g. to refresh an expired token)
from google.auth.transport.requests import Request
# Credentials: your login token; can be loaded from / saved to token.json
from google.oauth2.credentials import Credentials
# InstalledAppFlow: opens the browser so you can log in to Google the first time
from google_auth_oauthlib.flow import InstalledAppFlow

# Permissions the app asks for. "drive" = full access to all your Drive files.
# It's a list because an app can request several scopes at once.
SCOPES = ["https://www.googleapis.com/auth/drive"]

# Folder where this file (auth.py) lives:
#   __file__  -> path of this file
#   .resolve() -> turn it into a full absolute path
#   .parent   -> the folder that contains it (the repo root)
BASE_DIR = Path(__file__).resolve().parent
# OAuth client file downloaded from Google Cloud Console (never commit it)
CREDENTIALS_PATH = BASE_DIR / "credentials" / "credentials.json"
# Your saved login token; created automatically after the first login
TOKEN_PATH = BASE_DIR / "credentials" / "token.json"


# Define a function named get_credentials that takes no arguments
def get_credentials():
    # Docstring: describes what the function returns (editors show it on hover)
    """Return valid Google credentials: reuse the saved token, refresh it, or log in."""
    # Start with "nothing", so the variable exists even if there's no token file
    creds = None

    # Check whether token.json exists (it does if we logged in before)
    if TOKEN_PATH.exists():
        # Build a Credentials object from the saved token, with our SCOPES
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # Enter if there are no creds OR they aren't valid.
    # "not creds" goes first: if creds is None, Python stops there (short-circuit)
    # and never evaluates creds.valid, which would crash on None
    if not creds or not creds.valid:
        # creds exist AND are expired AND have a refresh token -> can renew
        if creds and creds.expired and creds.refresh_token:
            # Ask Google for a fresh token; Request() makes the HTTP call
            creds.refresh(Request())
        # Otherwise (no token, or it can't be refreshed) -> full login
        else:
            # Create a login flow from the OAuth client file (credentials.json)
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            # Open the browser to log in; port=0 = OS picks any free port
            creds = flow.run_local_server(port=0)

        # Convert creds to JSON text and save it to token.json (as UTF-8)
        # so next time we can skip the login
        TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")

    # Give the creds back to whoever called the function.
    # Indented at function level (not inside an if), so every path returns creds
    return creds


# Only runs when you execute "python auth.py" directly,
# NOT when another file does "from auth import get_credentials"
if __name__ == "__main__":
    # Get credentials (reuse, refresh, or log in) and store them
    creds = get_credentials()
    # True if the credentials can be used right now
    print("Valid:", creds.valid)
    # When the current access token expires (UTC)
    print("Expires:", creds.expiry)
