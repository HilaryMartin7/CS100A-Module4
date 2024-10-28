class Faculty:
    def __init__(self, list):
        """
        Create a default faculty member
        """

        self.name = ''
        self.list = []
       

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
    import datetime

    def input_faculty(self):
        """ 
        Prompt to input faculty members one at a time and store to list
        """
        while True:
            faculty_name = input("Enter the faculty member name (or 'done' to finish): ")
            if faculty_name.lower() == "done":
                break
            faculty_id = input(f"Enter {faculty_name}'s employee ID: ")
            while True:
                    try:
                        faculty_start = input (f"Enter {faculty_name}'s start date (YYYY-MM-DD):  ")
                        import datetime
                        faculty_start_date = datetime.datetime.strptime(faculty_start, "%Y-%m-%d").date()
                        return faculty_start
                    except ValueError:
                        print("Invalid date format.  Please use YYYY-MM-DD")
            self.fac_member = (faculty_name, faculty_id, faculty_start)
            self.list.append(self.fac_member)

    def print_list(self):
        """
        Display the list of faculty for the department using tabulate format
        """

        print(f"\nFaculty List for {self.name}:")
        from tabulate import tabulate
        table = tabulate (self.list)
        print(table)


if __name__ == "__main__":
    dept_name = input("Enter the department name: ")
    dept = Faculty(dept_name)
    dept.input_faculty()
    dept.print_list()
    

# # Initialize a facilty object 
# fac = Facilty()

# # Change the facilty properties
# fac.name = 'Bob'
# fac.ID = 45010
# fac.hire = '1/1/1999'

# print(f'#{fac.ID}: {fac.name}')

# fac.grade()
# fac.submitgrade('MA110')


