class Faculty:
    def __init__(self, name):
        """
        Create a default department for faculty 
        """

        self.name = name
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
            faculty_start= input(f"Enter {faculty_name}'s start date: ")
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
    from datetime import datetime
    dept_name = input("Enter the department name: ")
    dept = Faculty(dept_name)
    dept.input_faculty()
    dept.print_list()
    


