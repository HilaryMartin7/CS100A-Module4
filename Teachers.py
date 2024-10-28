class Facilty:
    def __init__(self):
        """
        Create a default faculty member
        """

        self.name = ''
        self.ID = -1
        self.hire = '1/1/2000'
        self.department = ''

    def grade(self):
        """
        Set time for grading
        """
        print(f'{self.name} is grading exams')

    def submitgrade(self, course):
        """
        Submitting grades for a course
        Parameters: course(str) the course to submit grades for
        """
        print(f'{self.name} grades are due for {course} course.')

# Initialize a facilty object
fac = Facilty()

# Change the facilty properties
fac.name = 'Bob'
fac.ID = 45010
fac.hire = '1/1/1999'

print(f'#{fac.ID}: {fac.name}')

fac.grade()
fac.submitgrade('MA110')


