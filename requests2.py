from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from models import Book, Loan, Reader
from app import get_db
from pydantic_schemas import BookBase, LoanBase, ReaderBase, BookCreate, BookUpdate, ReaderCreate, ReaderUpdate, LoanCreate, LoanUpdate 

app = FastAPI()

@app.get("/loans/taken-1-day-or-older", response_model=List[LoanBase])
def get_loans_taken_3_months_or_older(db: Session = Depends(get_db)):
    three_months_ago = datetime.today() - timedelta(days=1) 
    loans = db.query(Loan).filter(Loan.take_date <= three_months_ago.date()).all()
    if not loans:
        raise HTTPException(status_code=404, detail="No loans found 1 day ago or older")
    return loans

@app.get("/books/by-author/{author_name}", response_model=List[BookBase])
def get_books_by_author(author_name: str, db: Session = Depends(get_db)):
    books = db.query(Book).filter(Book.author == author_name).all()
    if not books:
        raise HTTPException(status_code=404, detail=f"No books found for author '{author_name}'")
    return books

@app.get("/loans/reader/{reader_id}", response_model=List[LoanBase])
def get_loans_by_reader(reader_id: int, db: Session = Depends(get_db)):
    loans = (
        db.query(Loan)
        .join(Book, Loan.book_id == Book.id)
        .filter(Loan.reader_id == reader_id)
        .all()
    )
    if not loans:
        raise HTTPException(status_code=404, detail="No loans found for the given reader")
    return loans

@app.put("/books/update-publisher")
def update_books_publisher_by_topic(topic: str, new_publisher: str, db: Session = Depends(get_db)):
    books = db.query(Book).filter(Book.topic == topic).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found with the given topic")
    
    for book in books:
        book.publisher = new_publisher
    
    db.commit()
    return {"message": f"Updated {len(books)} books with the new publisher"}

from sqlalchemy.sql import func

@app.get("/books/group-by-author", response_model=List[dict])
def get_books_grouped_by_author(db: Session = Depends(get_db)):
    grouped_books = (
        db.query(Book.author, func.count(Book.id).label("book_count"))
        .group_by(Book.author)
        .all()
    )

    if not grouped_books:
        raise HTTPException(status_code=404, detail="No books found to group by author")

    return [{"author": author, "book_count": book_count} for author, book_count in grouped_books]


@app.get("/readers/", response_model=List[ReaderBase])
def get_readers(sort_by: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Reader)
    if sort_by == "name":
        query = query.order_by(Reader.full_name)
    elif sort_by == "address":
        query = query.order_by(Reader.address)
    
    readers = query.all()
    if not readers:
        raise HTTPException(status_code=404, detail="No readers found")
    return readers

@app.get("/books/order-by-name-asc", response_model=List[BookBase])
def get_books_ordered_by_name_asc(db: Session = Depends(get_db)):
    books = db.query(Book).order_by(Book.name.asc()).all()

    if not books:
        raise HTTPException(status_code=404, detail="No books found")

    return books
