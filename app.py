from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import bd

db_url = "postgresql://rafik:1234@83.149.198.142:5411/rafik_db"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
		
def create_tables():
	bd.metadata.create_all(bind=engine)
