from pydantic import BaseModel
from datetime import date
from typing import Optional

class BookBase(BaseModel):
  id: Optional[int] = None
  author: str
  name: str
  publisher: str
  topic: str

  class Config:
    from_attributes = True


class BookCreate(BookBase):
  pass

class BookUpdate(BookBase):
  author: Optional[str] = None
  name: Optional[str] = None
  publisher: Optional[str] = None
  topic: Optional[str] = None
  
class LoanBase(BaseModel):
  id: Optional[int] = None
  take_date: date
  return_date: date
  where_returned: date

  class Config:
    orm_mode = True

class LoanCreate(LoanBase):
  book_id: int
  reader_id: int

class LoanUpdate(LoanBase):
  take_date: Optional[date] = None
  return_date: Optional[date] = None
  where_returned: Optional[date] = None

  

class ReaderBase(BaseModel):
  id: Optional[int] = None
  full_name: str
  address: str
  phone_number: str
  passport_number: str
  departure_mark: str

  class Config:
        orm_mode = True

class ReaderCreate(ReaderBase):
  pass

class ReaderUpdate(ReaderBase):
  full_name: Optional[str] = None
  address: Optional[str] = None
  phone_number: Optional[str] = None
  passport_number: Optional[str] = None
  departure_mark: Optional[str] = None

  
