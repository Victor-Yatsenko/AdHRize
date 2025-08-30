import os, dotenv

dotenv.load_dotenv()

# CLIENT
CLIENT_LOGIN      = os.getenv("CLIENT_LOGIN")
CLIENT_PASSWORD   = os.getenv("CLIENT_PASSWORD")

ADMIN_LOGIN       = os.getenv("ADMIN_LOGIN")
ADMIN_PASSWORD    = os.getenv("ADMIN_PASSWORD")

# SERVER
OPEN_PORT         = os.getenv("OPEN_PORT")
TEAMS_WEBHOOK_URL = os.getenv("TEAMS_WEBHOOK_URL")

REMOTE_SERVER     = os.getenv("REMOTE_SERVER")
USER_NAME         = os.getenv("USER_NAME")
USER_PASSWORD     = os.getenv("USER_PASSWORD")
PATCH_TO_SCRIPT   = os.getenv("PATCH_TO_SCRIPT")