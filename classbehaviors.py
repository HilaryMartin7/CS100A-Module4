class Student:
    def __init__(self):
        """
        Initialize a Student
        """
        
        self.name = ''
        self.ID = -1
        self.birthdate = '1/1/2000'

    def study(self):
        """
        Time to study
        """

        print(f'{self.name} is studying')

    def do_homework(self, course):
        """
        Time to do homework

        Parameters:
            course (str): The course to do homework for
        """

        print(f'{self.name} is doing homework for their {course}  course.')

    def ask_question(self):
        """
        This student has a question for the instructor
        """

        print('Wait, what?')

stud = Student()
# Set the student's properties
stud.name = 'Mary'
stud.ID = 10101
stud.birthdate = '1/1/1999'

print(stud.name)

# Time to be a student
stud.study()
stud.do_homework('CS100A')
stud.ask_question()

