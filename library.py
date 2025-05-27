class member:
    def __init__ (self,name,id):
        self.name = name
        self.id = id
        
class Student(member):
    def __init__ (self,name,id,books):
        super().__init__(name,id)
        self.books = [books]

    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book}' has been added to {self.name}'s collection.")

    def return_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' has been returned by {self.name}.")
        else:
            print(f"Book '{book}' not found in {self.name}'s collection.")

    def display_books(self):
        if self.books:
            print(f"{self.name}'s book collection:")
            for book in self.books:
                print(f"- {book}")
        else:
            print(f"{self.name} has no books in their collection.")

student = Student("John Doe", 123, [])
student.add_book("Python Programming")
student.add_book("Data Structures")
student.display_books()
student.return_book("Python Programming")
student.display_books()