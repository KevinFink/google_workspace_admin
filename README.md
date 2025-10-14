# Google Workspace Administration

There is a tool called GAM (Google Apps Manager) that allows administrators to manage Google Workspace
from the command line. However, I couldn't get it to work properly for certain tasks (e.g. gmail delegation).

This repository contains Python scripts that talk directly to the Google Workspace Admin API.

## Setup

1. **Create a Google Cloud Project**: Go to the [Google Cloud Console](https://console.cloud.google.com/), create a new project, and enable the "Admin SDK" API for that project.
2. **Create a Service Account**: In the Cloud Console, navigate to "IAM & Admin" > "Service Accounts", and create a new service account. Assign it the "Domain-wide Delegation" role.
3. **Delegate Domain-wide Authority**: In the service account settings, enable "G Suite Domain-wide Delegation" and note the "Client ID".
4. **Authorize API Scopes**: In the Google Workspace Admin Console, go to "Security" > "API Controls" > "Domain-wide Delegation", and add a new API client with the Client ID from the previous step. Authorize the following scopes:
   - `https://www.googleapis.com/auth/admin.directory.user`
   - `https://www.googleapis.com/auth/admin.directory.group`
   - `https://www.googleapis.com/auth/gmail.settings.basic`
   - `https://www.googleapis.com/auth/gmail.settings.sharing`
5. **Download Service Account Credentials**: Download the JSON key file for the service account and save it as `oauth2service.json` in this repository.
6. **Install Dependencies**: Make sure you have Python installed, then install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Scripts

### Gmail Delegation Management

- **`set_gmail_delegation.py`** - Creates a Gmail delegation between two users
  - Usage: `./set_gmail_delegation.py <mailbox_owner_email> <delegate_email>`
  - Grants delegation permissions allowing the delegate to read, send, and manage emails for the mailbox owner

- **`read_gmail_delegation.py`** - Lists all existing Gmail delegations for a user
  - Usage: `./read_gmail_delegation.py <mailbox_owner_email>`
  - Shows who has delegation access to the specified mailbox

### Diagnostic Tools

- **`check_scopes.py`** - Verifies OAuth scopes granted to the service account
  - Shows what API permissions are available for troubleshooting access issues

- **`check_service_account_credentials.py`** - Tests service account authentication
  - Verifies the service account can authenticate and access Google Workspace APIs

