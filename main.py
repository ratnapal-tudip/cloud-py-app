from fastapi import FastAPI
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

host = os.environ.get("host")
user = os.environ.get("user")
password = os.environ.get("password")
database = os.environ.get("database")

app = FastAPI()

def get_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        connection_timeout=10
    )

@app.get("/users")
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # 👈 returns dict like PyMySQL

    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users

@app.get("/health")
def health():
    return {"status": "ok"}
