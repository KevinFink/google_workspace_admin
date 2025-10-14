#! /usr/bin/env python3

from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/admin.directory.user.readonly"]
SUBJECT = ""  # any user in your domain

creds = service_account.Credentials.from_service_account_file(
    "oauth2service.json",
    scopes=SCOPES,
    subject=SUBJECT,
)

svc = build("admin", "directory_v1", credentials=creds, cache_discovery=False)
print(svc.users().get(userKey=SUBJECT).execute()["primaryEmail"])
