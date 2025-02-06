from sqlmodel import SQLModel, Session, create_engine, select
from dotenv import load_dotenv
import os

db_url = os.getenv("DB_HOST")
db_conn_args = {"check_same_thread": False}
db_engine = create_engine(db_url, connect_args=db_conn_args)

def get_db_session ():
    with Session(db_engine) as session:
        yield session
        
def create_db_and_tables():
    SQLModel.metadata.create_all(db_engine)