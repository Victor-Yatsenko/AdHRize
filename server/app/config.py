import os, dotenv

dotenv.load_dotenv()
TEAMS_WEBHOOK_URL = os.getenv("TEAMS_WEBHOOK_URL")

