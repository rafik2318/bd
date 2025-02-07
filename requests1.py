import requests
import random
from datetime import date, timedelta

BASE_URL = "http://127.0.0.1:8000" 

authors = ["author 1","author 2","author 3","author 4","author 5"]
publishers = ["publisher 1","publishers2","publisher 3","publisher 4","publisher 5"]
topics = ["topic 1","topic 2","topic 3","topic 4","topic 5"]
names = ["name 1","name 2","name 3","name 4","name 5"]

reader_names = ["reader_name 6","reader_name 2","reader_name 3","reader_name 4","reader_name 5"]
addresses = ["address 1","address 2","address 3","address 4","address 5"]
phone_numbers = ["phone_number 1","phone_number 2","phone_number 3","phone_number 4","phone_number 5"]
passport_numbers = ["passport_number 1","passport_number 2","passport_number 3","passport_number 4","passport_number 5"]
departure_marks = ["departure_mark 1","departure_mark 2","departure_mark 3","departure_mark 4","departure_mark 5"]

def create_book():
    book_data = {
        "author": random.choice(authors),
        "name": random.choice(names),
        "publisher": random.choice(publishers),
        "topic": random.choice(topics)
    }

    try:
        response = requests.post(f"{BASE_URL}/books/", json=book_data)
        
        print(response.json())
        if response.status_code in [200, 201]:
            if 'id' in response.json():
                print(f"Book created: {response.json()['name']}")
                return response.json()['id']
            else:
                print(f"id not founed: {response.json()}")
                return None
        else:
            print(f"Failed to create book: {response.status_code}, {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"error {e}")
        return None

def create_reader():
    reader_data = {
        "full_name": random.choice(reader_names),
        "address": random.choice(addresses),
        "phone_number": random.choice(phone_numbers),
        "passport_number": random.choice(passport_numbers),
        "departure_mark": random.choice(departure_marks)
    }

    try:
        response = requests.post(f"{BASE_URL}/readers/", json=reader_data)
        print(response.json())

        if response.status_code in [200, 201]:
            if 'id' in response.json():
                print(f"Reader created: {response.json()['full_name']}")
                return response.json()['id']
            else:
                print("if not founed", response.json())
                return None
        else:
            print(f"Failed to create reader: {response.status_code}, {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"error : {e}")
        return None
def create_loan(book_id, reader_id):

    if not book_id or not reader_id:
        print("no ID")
        return

    take_date = date.today() - timedelta(days=random.randint(1, 30))
    return_date = take_date + timedelta(days=random.randint(1, 14))
    where_returned = return_date + timedelta(days=random.randint(1, 5))
    loan_data = {
        "take_date": str(take_date),
        "return_date": str(return_date),
        "where_returned": str(where_returned),
        "book_id": book_id,
        "reader_id": reader_id
    }
    print(book_id, reader_id)
    
    try:
        print(f"Loan data: {loan_data}")
        response = requests.post(f"{BASE_URL}/loans/", json=loan_data)

        print("Response status code:", response.status_code)
        print("Response content:", response.text)

        if response.status_code in [200, 201]:
            print(f"Loan created for book ID {book_id} and reader ID {reader_id}")
        else:
            print(f"Failed to create loan: {response.status_code}, {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"error: {e}")

def populate_db():
    for _ in range(5): 
        book_id = create_book()
        if not book_id:
            print("loan not created")
            continue
        reader_id = create_reader()
        if not reader_id:
            print("loan not created")
            continue
        create_loan(book_id, reader_id)

if __name__ == "__main__":
    populate_db()
