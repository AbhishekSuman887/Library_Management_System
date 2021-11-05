class Library:
    totalBooks = ["Mahabharat", "Play with C", "Data Science Book", "Physics Book", "Maths book", "AI Book"]

    @staticmethod
    def addNewBooksToLibrary(books):
        Library.totalBooks = Library.totalBooks + books
        
    @staticmethod
    def dispalyListOfBooks():
        for i, item in enumerate(Library.totalBooks):
            print(f"\t{i+1}. {item}")
        

class Student:
    objects = {}
    def __init__(self, rollno, book):
        self.rollno = rollno
        Student.objects.update({rollno:self})
        self.borrowedBooks = []

    def borrowBooks(self, n):
        print(f"You have borrorwed the Book - {Library.totalBooks[n-1]}")
        self.borrowedBooks.append(Library.totalBooks.pop(n-1))

        print(f"List of Books borrowed by You : ")
        self.displayBorrowedBooks()
    
    def returnBooks(self, n):
        Library.totalBooks.append(self.borrowedBooks[n-1])
        print(f"Your book {self.borrowedBooks.pop(n-1)} has been returned!")
    
    def displayBorrowedBooks(self):
        if(self.borrowedBooks == None):
            print("No Books Borrowed till Now!")
        else:
            for i, item in enumerate(self.borrowedBooks):
                print(f"\t{i+1}. {item}")

if __name__ == "__main__":
    option = True
    while(option!="6"):
        print('''\n*********** Welcome to Library Portal ***********
        1. List the Books Present in Library.
        2. Borrow a Book.
        3. Return a Book.
        4. Student List.
        5. Display Borrowed Books by a particular student.
        6. Exit''')
        option = input("Enter Your option : ")
        if (option == "1"):
            Library.dispalyListOfBooks()
            print("Press Enter to Go to Main Menu and 'q' to quit : ", end = "")
            option = input()

        elif(option == "2"):

            n = input("Enter your RollNo. : ")
            if n in Student.objects.keys():
                oldobj = Student.objects.get(n)
                print(f"Available Books present in the Library :")
                Library.dispalyListOfBooks()
                n = int(input("Enter the number corrsponding to Book You want to Borrow : "))
                oldobj.borrowBooks(n)
            else:
                print("You are not present in Library System!")
                print("We have entered you in the LMS!")
                print(f"Available Books present in the Library : ")
                Library.dispalyListOfBooks()
                book = int(input("Enter the number corrsponding to Book You want to Borrow : "))
                newobj = Student(n, book)
                newobj.borrowBooks(book)
            
            print("Press Enter to Go to Main Menu and 'q' to quit : ", end = "")
            option = input()

        elif(option == "3"):
            n = input("Enter your Roll No. : ")
            x = Student.objects.get(n)
            x.displayBorrowedBooks()
            n = int(input("Enter the number corrsponding to Book You want to Return : "))
            x.returnBooks(n)
            print(f"List of Books borrowed by You : ")
            x.displayBorrowedBooks()

            print("Press Enter to Go to Main Menu and 'q' to quit : ", end = "")
            option = input()

        elif(option == "4"):
            print(list(Student.objects.keys()))

            print("Press Enter to Go to Main Menu and 'q' to quit : ", end = "")
            option = input()

        elif(option == "5"):
            n = input("Enter your Roll No. : ")
            x = Student.objects.get(n)
            x.displayBorrowedBooks()

            print("Press Enter to Go to Main Menu and 'q' to quit : ", end = "")
            option = input()

        elif(option == "6"):
            print("Thanks! Have a nice Day.")

        else:
            print("Please enter a valid choice!")




