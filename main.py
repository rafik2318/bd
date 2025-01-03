from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Book, Reader, Loan
from pydantic_schemas import BookCreate, BookUpdate, ReaderCreate, ReaderUpdate, LoanCreate, LoanUpdate
from app import get_db, create_tables

app = FastAPI()

@app.on_event("startup")
def startup():
    create_tables()

@app.post("/books/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    if book.author:
        db_book.author = book.author
    if book.name:
        db_book.name = book.name
    if book.publisher:
        db_book.publisher = book.publisher
    if book.topic:
        db_book.topic = book.topic

    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(db_book)
    db.commit()
    return db_book

@app.post("/readers/", response_model=Reader)
def create_reader(reader: ReaderCreate, db: Session = Depends(get_db)):
    db_reader = Reader(**reader.dict())
    db.add(db_reader)
    db.commit()
    db.refresh(db_reader)
    return db_reader

@app.get("/readers/{reader_id}", response_model=Reader)
def read_reader(reader_id: int, db: Session = Depends(get_db)):
    db_reader = db.query(Reader).filter(Reader.id == reader_id).first()
    if db_reader is None:
        raise HTTPException(status_code=404, detail="Reader not found")
    return db_reader

@app.put("/readers/{reader_id}", response_model=Reader)
def update_reader(reader_id: int, reader: ReaderUpdate, db: Session = Depends(get_db)):
    db_reader = db.query(Reader).filter(Reader.id == reader_id).first()
    if db_reader is None:
        raise HTTPException(status_code=404, detail="Reader not found")    
    if reader.full_name:
        db_reader.full_name = reader.full_name
    if reader.address:
        db_reader.address = reader.address
    if reader.phone_number:
        db_reader.phone_number = reader.phone_number
    if reader.passport_number:
        db_reader.passport_number = reader.passport_number
    if reader.departure_mark:
        db_reader.departure_mark = reader.departure_mark
    db.commit()
    db.refresh(db_reader)
    return db_reader

@app.delete("/readers/{reader_id}", response_model=Reader)
def delete_reader(reader_id: int, db: Session = Depends(get_db)):
    db_reader = db.query(Reader).filter(Reader.id == reader_id).first()
    if db_reader is None:
        raise HTTPException(status_code=404, detail="Reader not found")
    
    db.delete(db_reader)
    db.commit()
    return db_reader

@app.post("/loans/", response_model=Loan)
def create_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    db_loan = Loan(**loan.dict())
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan

@app.get("/loans/{loan_id}", response_model=Loan)
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan

@app.put("/loans/{loan_id}", response_model=Loan)
def update_loan(loan_id: int, loan: LoanUpdate, db: Session = Depends(get_db)):
    db_loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    
    if loan.take_date:
        db_loan.take_date = loan.take_date
    if loan.return_date:
        db_loan.return_date = loan.return_date
    if loan.where_returned:
        db_loan.where_returned = loan.where_returned

    db.commit
