from sqlalchemy import  Column, Date, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

bd = declarative_base()

class Loan(bd):
	__tablename__ = "loans"	

	id = Column(Integer, primary_key = True, index = True)
	take_date = Column(Date, nullable=False)
	return_date = Column(Date, nullable=False)
	where_returned = Column(Date, nullable=False)

	reader_id = Column(Integer, ForeignKey("readers.id"),nullable=False)
	book_id = Column(Integer, ForeignKey("books.id"),nullable=False)

	book = relationship("Book", back_populates = "loan")
	reader = relationship("Reader", back_populates = "loan")

class Book(bd):
	__tablename__ = "books"

	id = Column(Integer, primary_key = True, index = True)
	author = Column(String)
	name = Column(String)
	publisher = Column(String)
	topic = Column(String)
	
	loan = relationship("Loan", back_populates = "book")
	
class Reader(bd):
	__tablename__ = "readers"
	
	id = Column(Integer, primary_key = True, index = True)
	full_name = Column(String)
	address = Column(String)
	phone_number = Column(String)
	passport_number = Column(String)
	departure_mark = Column(String)

	loan = relationship("Loan", back_populates="reader")
