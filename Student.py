class Student:

    def __init__(self, name='', ID=-1, birthdate='1/1/2000'):
        """
        Initialize this student object
        """

        self.name = name
        self.ID = ID
        self.birthdate = birthdate

    def study(self):
        """
        Time to study
        """
        
        print(self.name + ' is studying')

    def do_homework(self, course):
        """
        Time to do homework

        Parameters:
            course (str): The course to do homework for
        """

        print(self.name + ' is doing homework for their ' + course + ' course.')

    def ask_question(self):
        # I have a question
        print('Wait, what?')

# create a default student
stud = Student('Mary', 34355, '1/1/2004')
# create another student with different properties
stud2 = Student('Susan', 11223, '6/1/2001')

print(stud.name)

# Time to be a student
stud.study()
stud.do_homework('CS100A')
stud.ask_question()

stud2.study()
stud2.do_homework('CS100A')
stud2.ask_question()