from models.database import Database
import os
from dotenv import load_dotenv

load_dotenv()

db_engine = os.getenv("DB_ENGINE")
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_database = os.getenv("DB_DATABASE")

connection = Database(db_engine, db_user, db_password, db_database, db_host)


def get_connection():
    return connection
