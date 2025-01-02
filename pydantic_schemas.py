from pedantic import BaseModel
from datetime import Date
from typing import Optional

class BookBase(BaseModel):
  author: str
  name: str
  publisher: str
  topic: str

  class Config:
    orm_mode = True


class BookCreate(BookBase):
  pass

class BookUpdate(BookBase):
  author: Optional[str] = None
  name: Optional[str] = None
  publisher: Optional[str] = None
  topic: Optional[str] = None

  
class LoanBase(BaseModel):
  take_date: date
  return_date: date
  where_returned: date

  class Config:
    orm_mode = True

class LoanCreate(LoanBase):
  pass

class LoanUpdate(LoanBase):
  take_date: Optional[date] = None
  return_date: Optional[date] = None
  where_returned: Optional[date] = None

  

class ReaderBase(BaseModel):
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

  
