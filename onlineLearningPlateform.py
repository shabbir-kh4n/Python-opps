class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}")
    
class instructor(user):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def upload_content(self, content):
        print(f"Instructor {self.name} has uploaded new content: {content}")
    
    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

class CourseCreator(instructor):
    def __init__(self, name, email, subject, course_name):
        super().__init__(name, email, subject)
        self.course_name = course_name
    
    def create_course(self):
        print(f"Course '{self.course_name}' has been created by {self.name} in {self.subject}.")

    def display_info(self):
        super().display_info()
        print(f"Course Name: {self.course_name}")

x = CourseCreator("Alice", "xyz@mail.com", "Mathematics", "Calculus 101")
x.create_course()
x.upload_content("Lecture 1: Introduction to Calculus")
x.display_info()

y = instructor("Bob", "abc@gmail.in", "Physics")
y.upload_content("Lecture 1: Introduction to Physics")
y.display_info()

z= user("Charlie", "pqr@hotmail.com")
z.display_info()

