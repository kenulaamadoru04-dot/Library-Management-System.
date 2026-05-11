from datetime import datetime, timedelta

TODAY = datetime.today().date()
VALID_DAYS = 14
FINE_PER_DAY = 100

member_ids = [
    {"Name": "John", "Age": 25, "Joined_Date": "2024-07-01", "Member_ID": "MID0001", "Borrowed_Books": ["BID0001"]},
    {"Name": "Diana", "Age": 21, "Joined_Date": "2024-09-03", "Member_ID": "MID0002", "Borrowed_Books": ["BID0002"]},
    {"Name": "Peter", "Age": 22, "Joined_Date": "2024-08-11", "Member_ID": "MID0003", "Borrowed_Books": []},
    {"Name": "Tony", "Age": 50, "Joined_Date": "2024-06-06", "Member_ID": "MID0004", "Borrowed_Books": []},
    {"Name": "Emily", "Age": 24, "Joined_Date": "2024-10-15", "Member_ID": "MID0005", " Borrowed_Books": []},
    {"Name": "Michael", "Age": 30, "Joined_Date": "2024-11-20", "Member_ID": "MID0006", "Borrowed_Books": []},
    {"Name": "Sophia", "Age": 19, "Joined_Date": "2024-12-01", "Member_ID": "MID0007",  "Borrowed_Books": []},
    {"Name": "Daniel", "Age": 27, "Joined_Date": "2024-07-18", "Member_ID": "MID0008", "borrowed_Books": []},
    {"Name": "Olivia", "Age": 23, "Joined_Date": "2024-08-25", "Member_ID": "MID0009", "Borrowed_Books": []},
    {"Name": "Chris", "Age": 35, "Joined_Date": "2024-09-14", "Member_ID": "MID0010", "Borrowed_Books": []},
    {"Name": "Natalie", "Age": 28, "Joined_Date": "2024-10-30", "Member_ID": "MID0011", "Borrowed_Books": []},
    {"Name": "Kevin", "Age": 26, "Joined_Date": "2024-11-08", "Member_ID": "MID0012", "Borrowed_Books": []},
    {"Name": "Grace", "Age": 20, "Joined_Date": "2024-12-12", "Member_ID": "MID0013", "Borrowed_Books": []},
    {"Name": "Ethan", "Age": 31, "Joined_Date": "2025-01-05", "Member_ID": "MID0014", "Borrowed_Books": []},
]

books_details = [
    {
        "Name": "Game of Thrones",
        "BookID": "BID0001",
        "Author": "R R Martin",
        "Availability": True,

    },
    {
        "Name": "Harry Potter",
        "BookID": "BID0002",
        "Author": "J K Rowling",
        "Availability": False
    },
    {
        "Name": "The Hobbit",
        "BookID": "BID0003",
        "Author": "J R R Tolkien",
        "Availability": True
    },
    {
        "Name": "The Alchemist",
        "BookID": "BID0004",
        "Author": "Paulo Coelho",
        "Availability": False
    },
    {
        "Name": "Atomic Habits",
        "BookID": "BID0005",
        "Author": "James Clear",
        "Availability": False
    },
    {
        "Name": "Rich Dad Poor Dad",
        "BookID": "BID0006",
        "Author": "Robert Kiyosaki",
        "Availability": True
    },
    {
        "Name": "Sherlock Holmes",
        "BookID": "BID0007",
        "Author": "Arthur Conan Doyle",
        "Availability": False
    },
    {
        "Name": "Think and Grow Rich",
        "BookID": "BID0008",
        "Author": "Napoleon Hill",
        "Availability": True
    },
    {
        "Name": "The Great Gatsby",
        "BookID": "BID0009",
        "Author": "F Scott Fitzgerald",
        "Availability": True
    },
    {
        "Name": "1984",
        "BookID": "BID0010",
        "Author": "George Orwell",
        "Availability": False
    },
    {
        "Name": "The Catcher in the Rye",
        "BookID": "BID0011",
        "Author": "J D Salinger",
        "Availability": True
    },
    {
        "Name": "To Kill a Mockingbird",
        "BookID": "BID0012",
        "Author": "Harper Lee",
        "Availability": False
    }
]

borrowed_list = [{'BookID': 'BID0001', 'MemberID': 'MID0001', 'BorrowedDate': '2026-05-07', 'DueDate': '2026-04-03'},
                 {'BookID': 'BID0002', 'MemberID': 'MID003', 'BorrowedDate': '2026-05-01', 'DueDate': '2026-05-15'}]

# ------------- Checking the Member ID -------------

def name_validation():

    member_id = input("Enter your Member ID: ")

    if member_details(member_id):
        return member_id

    print("⚠️ Member ID not found ⚠️")
    return False

# ------------------- Print Member Details -----------

def member_details(member_id):
    for member in member_ids:

        if member["Member_ID"] == member_id:
            print(f"""
    A valid member
    -------------------------------------
    Name: {member['Name']}
    Age: {member['Age']}
    Joined Date: {member['Joined_Date']}
    Member ID: {member['Member_ID']}
    -------------------------------------
    """)
            return True
    return False
# ------------------ Add a New Member ----------------

def add_member():
    last_member_id = member_ids[-1]["Member_ID"]
    id_number = int(last_member_id[-3:])
    new_id = f"MID{(id_number + 1):04}"
    new_member = {
        "Name": input("Enter your Name: "),
        "Age": input("Enter your Age: "),
        "Joined_Date": TODAY.strftime("%Y-%m-%d"),
        "Member_ID": new_id,
        "Borrowed_Books": []
    }
    member_ids.append(new_member)
    print(new_member)
    return new_id


# ------------------ Borrowing a Book ----------------

def borrowing_book(book_id, mem_id):
    for book in books_details:

        if book["BookID"] == book_id:

            if not book["Availability"]:
                print("Book is already borrowed")
                break

            details = {
                "BookID": book["BookID"],
                "MemberID": mem_id,
                "BorrowedDate": TODAY.strftime("%Y-%m-%d"),
                "DueDate": (TODAY + timedelta(days=VALID_DAYS)).strftime("%Y-%m-%d"),
            }

            borrowed_list.append(details)
            book["Availability"] = False
            book["Last Borrowed Date"] = TODAY.strftime("%Y-%m-%d")
            book["Last Borrowed Member"] = mem_id

            print("Book Borrowed ✅")
            return True

    print("Book ID not found")
    return False

# ------------------- Receiving Borrowed Book ------------------

def receive_book(book_id):

    for book in borrowed_list:

        if book["BookID"] == book_id:

            print_book_details(book_id)
            for borrowings in borrowed_list:
                if borrowings["BookID"] == book_id:
                    print(f"Due Date: {borrowings['DueDate']}")
                    print(f"Returned Date: {datetime.today().strftime('%Y-%m-%d')}")

            due_date = datetime.strptime(book['DueDate'], '%Y-%m-%d').date()
            today = datetime.today().date()
            over_days = (today - due_date).days

            if over_days > 0:
                fine = over_days * FINE_PER_DAY

                print(f"""
You are late by {over_days} days!
Your fine is Rs.{fine}/=
""")
            else:

                print("Book returned successfully ✅")

            borrowed_list.remove(book)

            for book_detail in books_details:

                if book_detail["BookID"] == book_id:
                    book_detail["Availability"] = True

            return

    print("Borrow record not found")

# ------------------Display Book Details ------------------------------

def print_book_details(book_id):

    for book in books_details:

        if book["BookID"] == book_id:
            print(f"""-------------------------------
Book Details

Book ID: {book["BookID"]}
Name: {book["Name"]}
Author: {book["Author"]}
Availability: {book["Availability"]}

---------------------------------------------------- 
""")

# -------------- Borrowed Details ------------------------
def show_borrowings(borrowed_details):

    print("\n")
    print(f"{'Book ID':<12} {'Member ID':<14} {'Due Date':<10}")

    for borrow in borrowed_details:
        print(f"{borrow['BookID']:<12} {borrow['MemberID']:<14} {borrow['DueDate']:<10}")

    print("\n")


# ---------------------Menu -------------------------------

def menu():

    print("""
======================================
         UCSC Library System
======================================
            1.View All Books
            2.Borrow a Book
            3.Return a Book
            4.Add Member
            5.Show All the members
            6.Show All Borrowed Details
            0.Exit
======================================
""")

# ---------- View All Books ------------------

def show_books(book_list):

    print("\n")
    print(f"{'ID':<8}  {'Name':<30}  {'Author':<29}{'Availability':<10}")

    for book in book_list:
        status = "✅Available" if book["Availability"] else "❌Borrowed"
        print(f"{book['BookID']:<8} {book['Name']:<30} {book['Author']:<30} {status:<10}")

    print("\n")

# -------------Show Members -----------------
def show_members(members_list):

    print("\n")
    print(f"{'ID':<8} {'Name':<15} {'Age':<6} {'Joined Date':<20}")

    for member in members_list:

        print(f"{member['Member_ID']:<8} {member['Name']:<15} {member['Age']:<6} {member['Joined_Date']:<20}")

    print("\n")

# -------------Main Programme ----------------

library_process = True

while library_process:

    menu()
    user_option = input("Select an option: ")

    if user_option == "1":
        show_books(books_details)

    elif user_option == "2":
        user_id = name_validation()
        if user_id:
            book_id = input("Enter Book ID: ")
            borrowing_book(book_id, user_id)
        else:
            continue

    elif user_option == "3":
        user_id = name_validation()
        book_id = input("Enter Book ID: ")
        receive_book(book_id)
    elif user_option == "4":
        new_m_id = add_member()
    elif user_option == "5":
        show_members(member_ids)
    elif user_option == "6":
        show_borrowings(borrowed_list)
    elif user_option == "0":
        break
    else:
        print("⚠️Invalid option")
        continue








