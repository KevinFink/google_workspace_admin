#!/usr/bin/env python3
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build

if len(sys.argv) != 3:
    print(
        "Usage: python remove_gmail_delegation.py <mailbox_owner_email> <delegate_email>"
    )
    sys.exit(1)

SCOPES = ["https://www.googleapis.com/auth/gmail.settings.sharing"]
SUBJECT = sys.argv[1]  # mailbox owner
DELEGATE = sys.argv[2]  # delegate to remove

creds = service_account.Credentials.from_service_account_file(
    "oauth2service.json", scopes=SCOPES, subject=SUBJECT
)
svc = build("gmail", "v1", credentials=creds, cache_discovery=False)

print(
    svc.users()
    .settings()
    .delegates()
    .delete(userId="me", delegateEmail=DELEGATE)
    .execute()
)
