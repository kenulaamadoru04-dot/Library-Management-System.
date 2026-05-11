import json
from datetime import datetime, timedelta

TODAY = datetime.today().date()
VALID_DAYS = 14
FINE_PER_DAY = 100


with open("members.json", "r") as file:
    json_data = json.load(file)

member_ids = json_data

with open("books.json", "r") as file:
    json_data = json.load(file)

books_details = json_data


with open("borrowings.json", "r") as file:
    json_data = json.load(file)

borrowed_list = json_data

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
    with open("members.json", "w") as file:
        json.dump(member_ids, file, indent=4)
    return new_id

# ------------------ Borrowing a Book ----------------

def borrowing_book(book_id, mem_id):
    for book in books_details:

        if book["BookID"] == book_id:

            if not book["Availability"]:
                print("Book is not available now")
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
            7.Remove a Member
            8.Remove a Book
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
    print(f"{'ID':<8} {'Name':<15} {'Age':<6} {'Joined Date':<20} {'Number of Books Borrowed':<20}")

    for member in members_list:

        print(f"{member['Member_ID']:<8} {member['Name']:<15} {member['Age']:<6} {member['Joined_Date']:<20} {f'{len(member['Borrowed_Books'])}/2':>10}")

    print("\n")

# ---------------Remove members ---------------
def remove_a_member(member_id):
    for member in member_ids:
        if member["Member_ID"] == member_id:
            member_ids.remove(member)
            with open("members.json", "w") as file:
                json.dump(member_ids, file, indent=4)
            break

    print("Member ID not found")

# ------------- Remove a Book ---------------

def remove_a_book(book_id):
    for book in books_details:
        if book["BookID"] == book_id:
            books_details.remove(book)
            break

    print("Book ID not found")

# ------------- Limit to Two Books ----------
def limit(member_id):
    for member in member_ids:
        if member["Member_ID"] == member_id:
            if len(member["Borrowed_Books"]) == 2:
                print("You already borrowed two books.")
                return False
    return True

# -------------Main Programme ----------------

library_process = True

while library_process:

    menu()
    user_option = input("Select an option: ")

    if user_option == "1":
        show_books(books_details)

    elif user_option == "2":
        user_id = name_validation()
        if user_id and limit(user_id):
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
    elif user_option == "7":
        user_id = name_validation()
        remove_a_member(user_id)
    elif user_option == "8":
        book_id = input("Enter Book ID: ")
        remove_a_book(book_id)
    elif user_option == "0":
        break
    else:
        print("⚠️Invalid option")
        continue








