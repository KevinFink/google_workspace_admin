#!/usr/bin/env python3
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build

if len(sys.argv) != 2:
    print("Usage: python read_gmail_delegation.py <mailbox_owner_email>")
    sys.exit(1)

SCOPES = [
    "https://www.googleapis.com/auth/gmail.settings.sharing",
    "https://www.googleapis.com/auth/gmail.settings.basic",  # read scope for list
]
SUBJECT = sys.argv[1]  # the mailbox owner you're trying to manage

creds = service_account.Credentials.from_service_account_file(
    "oauth2service.json",
    scopes=SCOPES,
    subject=SUBJECT,
)

svc = build("gmail", "v1", credentials=creds, cache_discovery=False)
print(svc.users().settings().delegates().list(userId="me").execute())
