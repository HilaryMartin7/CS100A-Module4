class Course:
    def __init__(self):
        """
        Create a default course
        """

        self.name = ''
        self.number = ''
        self.credit = 0.0
        self.day = ''

    def begin(self, time, location):
        """
        Time when course begins
        """
        print (self.name + ' is starting now at ' + time + ' in ' + location)

# Initialize a course object
cour = Course()

# Change the course properties
cour.name = 'Calculus 1'
cour.number = 'MA110'
cour.credit = 3.0
cour.day = "MWF"

print(f'{cour.number}: {cour.name} {cour.day}')

cour.begin('2:30pm', 'Dixon 110')



