from sqlalchemy import create_engine, text

db_url = "postgresql://rafik:1sPmKldQwj8mx@83.149.198.142/rafik_db"

engine = create_engine(db_url)

with  engine.connect() as conn:
	res = conn.execute(text("SELECT VERSION()"))
	print(f"{res=}")
