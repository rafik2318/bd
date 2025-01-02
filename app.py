from sqlalchemy import create_engine, text

db_url = "postgresql://rafik:1sPmKldQwj8mx@83.149.198.142/rafik_db"

engine = create_engine(db_url)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
