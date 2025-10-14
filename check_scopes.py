#! /usr/bin/env python3

from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests

SCOPES = ["https://www.googleapis.com/auth/gmail.settings.sharing"]
SUBJECT = ""  # User to check

creds = service_account.Credentials.from_service_account_file(
    "oauth2service.json", scopes=SCOPES, subject=SUBJECT
)
creds.refresh(Request())
print(
    requests.get(
        "https://oauth2.googleapis.com/tokeninfo", params={"access_token": creds.token}
    ).json()["scope"]
)
