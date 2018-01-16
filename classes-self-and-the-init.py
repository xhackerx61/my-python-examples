__Author__ = "Aslan"
# Object Oriented Programming
# some sample codes about classes, __init__ function and the self parameter 
class Student():
    def __init__(self, name, surname, number, school, dept ):
        self.name = name
        self.surname = surname
        self.number = number
        self.school = school
        self.dept = dept


    def seeStudentInfo(self):
        print("""
        -------------------
        -  Student Added  -
        -------------------

        Student Info;
        ------------
        Name : {}
        Surname : {}
        Number : {}
        School Name : {}
        Department : {}
        """.format(self.name, self.surname, self.number, self.school, self.dept))


# lets add a student
developer = Student("Murat", "Aslan", "789456123", "Erciyes University", "Computer Programming")
developer.seeStudentInfo()









