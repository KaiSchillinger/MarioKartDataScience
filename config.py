import os
from dotenv import load_dotenv

# Umgebungsvariablen laden
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/my_database")
