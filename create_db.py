from models import engine, db_session, Base
Base.metadata.create_all(bind=engine)