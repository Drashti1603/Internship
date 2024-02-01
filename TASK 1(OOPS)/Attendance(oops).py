class Person:  #Parent Class
    def __init__(self, person_id, name): #Constructors
        self.person_id = person_id   #objects
        self.name = name
        self.attendance = False

    def mark_attendance(self):
        self.attendance = True

    def display(self):
        print(f"ID: {self.person_id}, Name: {self.name}, Attendance: {'Present' if self.attendance else 'Absent'}")
# here f in above print is string formatting mechanism here ID is a property of self person_id, f'id is {person_id[id]]}'

class Teacher(Person):      #Child Class
    def __init__(self, person_id, name, __employee_id):
        super().__init__(person_id, name)
        self.__employee_id = __employee_id    ## Encapsulation(making a var private)
        self.subjects = [] 

    def add_sub(self, subject):
        self.subjects.append(subject)

    def display(self):  #Polymorphism
        super().display()
        print("Subjects:", ", ".join(subject.sub_name for subject in self.subjects))


class Subject(Person):
    def __init__(self, sub_id, sub_name):
        self.sub_id = sub_id
        self.sub_name = sub_name


class AttendanceSystem:
    def __init__(self):
        self.people = {}

    def add_person(self, person):
        if person.person_id not in self.people:
            self.people[person.person_id] = person
            print(f"{type(person).__name__} {person.name} added successfully.")
        else:
            print(f"{type(person).__name__} {person.person_id} already exists.")

    def mark_attendance(self, person_id):            #Polymorphism
        if person_id in self.people:
            person = self.people[person_id]
            person.mark_attendance()
            print(f"Attendance marked for {person.name}.")
        else:
            print(f"Person with ID {person_id} not found.")

    def display_attendance(self):
        print("Attendance Report:")
        for person_id, person in self.people.items():
            person.display()


if __name__ == "__main__":
    n = int(input("Num of Students:"))
    attendance_system = AttendanceSystem()

    for i in range(n):
        student = Person(int(input("ID:")), input("Name:"))
        attendance_system.add_person(student)

    t = int(input("Num of teachers:"))
    for i in range(t):
        teacher_id = int(input("ID:"))
        teacher_name = input("Name:")
        employee_id = int(input("Emp_ID:"))
        teacher = Teacher(teacher_id, teacher_name, employee_id)
        
        s= int(input("subjects for teacher:"))
        for j in range(s):
            sub_id = input("Subject ID:")
            sub_name = input("Subject Name:")
            subject = Subject(sub_id, sub_name)
            teacher.add_sub(subject)
        
        attendance_system.add_person(teacher)

    n = int(input("Num of Students Present:"))
    for i in range(n):
        attendance_system.mark_attendance(int(input("ID of present student:")))

    t= int(input("Num of teachers present:"))
    for i in range(t):
        attendance_system.mark_attendance(int(input("ID of present Teacher:")))

    attendance_system.display_attendance()
