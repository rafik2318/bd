from sqlalchemy.orm import Session
from datetime import date

def create_book(db: Session, author: str, name: str, publisher: str, topic: str):
  book = Book(author=author, name=name, publisher=publisher, topic=topic)
  db.add(book)
  db.commit()
  db.refresh(book)
  print(f"Book created: {db_book.name}")
  return book

def read_book(db: Session, book_id: int):
  book = db.query(Book).filter(Book.id == book_id).fisrt()
  if book:
    print(f"Book is found: author:{book.author}, name:{book.name}, publisher:{book.publisher}, topic:{book.topic}")
  else:
    print(f"Book with if {book.id} not found")
  return book

def update_book(db: Session, book_id: int, author: str = None, name: str = None, publisher: str = None, topic: str = None):
  book = db.query(Book).filter(Book.id == book_id).fisrt()
  if book:
    if author:
      book.author = author
    if name:
      book.name = name
    if publisher: 
      book.publisher = publisher
    if topic:
      book.topic = topic
    db.commit()
    db.refresh(book)
    print(f"Book with id {book.id} updated")
    return book
  else:
    print(f"Book with id {book.id} not found")
  return None

def delete_book(db: Session, book_id: int):
  book = db.query(Book).filter(Book.id == book_id).fisrt()
  if book:
    db.delete(book)
    db.commit()
    print(f"Book with id {book.id} deleted")
    return True
  else:
    print(f"Bookwith id {book.id} not found")
  return False

def create_loan(db: Session, take_date: date, return_date: date, where_returned: date)
  loan = Loan(take_date=take_date, return_date=return_date, where_returned=where_returned)
  db.add(loan)
  db.commit()
  db.refresh(loan)
  print("loan created")
  return loan

def read_loan(db: Session, loan_id: int):
  loan = db.query(Loan).filter(Loan.id == loan_id).first()
  if loan:
    print(f"loan is found: take_date:{loan.take_date}, return_date:{loan.return_date}, where_returned:{loan.where_returned}")
  else:
    print(f"loan with  id {loan.id} not found")
  return loan

def update_loan(db: Session, take_date: date = None, return_date: date = None, where_returned: date = None):
  loan = db.query(Loan).filter(Loan.id == loan_id).first()
  if loan:
    if take_date:
      loan.take_date = take_date
    if return_date:
      loan.return_date = return_date
    if where_returned:
      loan.where_returned = where_returned
    db.commit()
    db.refresh(loan)
    print(f"loan with id {loan.id} updated")
    return loan
  else:
    print(f"loan with id {book.id} not found")
  return None

def delete_loan(db: Session, loan_id: int):
  loan = db.query(Loan).filter(Loan.id == loan_id).first()
  if loan:
    db.delete(loan)
    db.commit()
    print(f"loan with id {loan.id} deleted")
    return True
  else:
    print(f"loan with id {loan.id} not found")
  return False

def create_reader(db: Session, full_name: str, address: str, phone_number: str, passport_number: str, departure_mark: str):
  reader = Reader(full_name=full_name, address=address, phone_number=phone_number, passport_number=passport_number, departure_mark=departure_mark)
  db.add(reader)
  db.commit()
  db.refresh(reader)
  print("reader created")
  return reader

def read_loan(db: Session, reader_id: int):
  reader = db.query(Reader).filter(Reader.id == reader_id).first()
  if reader:
    print(f"reader is found: full_name:{reader.full_name}, address:{reader.address}, phone_number:{reader.phone_number}, passport_number:{reader.passport_number}, departure_mark:{reader.departure_mark}")
  else:
    print(f"reader with  id {reader.id} not found")
  return reader
  
def update_reader(db: Session, reader_id: int, full_name: str = None, address: str = None, phone_number: str = None, passport_number: str = None, departure_mark: str = None):
  reader = db.query(Reader).filter(Reader.id == reader_id).first()
  if reader:
    if full_name:
            reader.full_name = full_name
        if address:
            reader.address = address
        if phone_number:
            reader.phone_number = phone_number
        if passport_number:
            reader.passport_number = passport_number
        if departure_mark:
            reader.departure_mark = departure_mark
        db.commit()
        db.refresh(reader)
        print(f"reader with id {reader.id} updated")
        return reader
  else:
    print(f"reader with id {reader.id} not found")
  return None

def delete_reader(db: Session, reader_id: int):
    reader = db.query(Reader).filter(Reader.id == reader_id).first()
    if reader:
        db.delete(reader)
        db.commit()
        print(f"reader with id {reader.id} deleted")
        return True
    else:
      print(f"reader with id {reader.id} not found")
    return False
    
