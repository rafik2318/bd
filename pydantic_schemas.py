from pedantic import BaseModel
from datetime import Date

class BookBase(BaseModel):
  author: str
  name: str
  publisher: str
  topic: str

class BookCreate(BookBase):
  pass

class Book(BookBase):
  id: int

  class Config:
    orm_mode = True

class LoanBase(BaseModel):
  take_date: date
  return_date: date
  where_returned: date

class LoanCreate(LoanBase):
  pass

class Loan(LoanBase):
  id: int
  book_id: int
  reader_id: int

  class Config:
    orm_mode = True

class ReaderBase(BaseModel):
  full_name: str
  address: str
  phone_number: str
  passport_number: str
  departure_mark: str

class ReaderCreate(ReaderBase):
  pass

class Reader(ReaderBase):
  id: int

  class Config:
    orm_mode = True
