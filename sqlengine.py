from sqlalchemy import create_engine

def connect():
    return create_engine('sqlite:///main.db')