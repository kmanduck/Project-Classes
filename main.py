
class patient:
    __id=0
    __name=""
    __diagnosis=""
    __gender=""
    __age=0

    def __init__(self,id,name,diagnosis,gender,age):
        self.__id=id
        self.__name = name
        self.__diagnosis=diagnosis
        self.__gender=gender
        self.__age=age
    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_diagnosis(self,diagnosis):
        self.__diagnosis=diagnosis
    def get_diagnosis(self):
        return self.__diagnosis
    def set_gender(self,gender):
        self.__gender=gender
    def get_gender(self):
        return self.__gender
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age

    def __str__(self):
        print("ID:\t\t", self.__id)
        print("Name:\t\t", self.__name)
        print("Diagnosis:\t\t", self.__diagnosis)
        print("Gender:\t\t", self.__gender)
        print("Age:\t\t", self.__age)
        print("\n")
        return str("")


p1 = patient('id', 'name', 'diagnosis', 'gender', 'age')
p1.set_id(12)
p1.set_name("Pankaj")
p1.set_diagnosis("Leukemia")
p1.set_gender("Male")
p1.set_age(30)

p2 = patient('id', 'name', 'diagnosis', 'gender', 'age')
p2.set_id(13)
p2.set_name("Janina")
p2.set_diagnosis("Cold")
p2.set_gender("Female")
p2.set_age(23)

p3 = patient('id', 'name', 'diagnosis', 'gender', 'age')
p3.set_id(14)
p3.set_name("Alonna")
p3.set_diagnosis("Malaria")
p3.set_gender("Female")
p3.set_age(45)

p4 = patient('id', 'name', 'diagnosis', 'gender', 'age')
p4.set_id(15)
p4.set_name("Ravi")
p4.set_diagnosis("Diabetes")
p4.set_gender("Male")
p4.set_age(65)

on = 1

while on == 1:
    option = int(input("Patient Menu\n 0 - Return to Main Menu\n 1 - Display patient's list\n 2 - Search for patient by ID\n 3 - Add patient\n 4 - Edit patient info"))

    if option == 0:
        on = 0

    if option == 1:
        print(p1, p2, p3, p4)

    if option == 2:
        id = int(input("Enter the Patient ID"))
        if id == p1.get_id():
            print(p1)
        if id == p2.get_id():
            print(p2)
        if id == p3.get_id():
            print(p3)
        if id == p4.get_id():
            print(p4)
        else:
            print("Patient with ID " + str(id) + " not in patient file")
    if option == 3:
        pid = input("Enter Patient ID")
        pname = input("Enter Patient Name")
        pdiag = input("Enter Patient Diagnosis")
        pgender = input("Enter Patient Gender")
        page = input("Enter Patient Age")
        p5 = patient(pid, pname, pdiag, pgender, page)
        print("\nYour new patient!:\n")
        print(p5)

    if option == 4:
        id = int(input("Enter the Patient ID"))
        if id == p1.get_id():
            pid = id
            pname = input("Enter new Patient Name")
            pdiag = input("Enter new Patient Diagnosis")
            pgender = input("Enter new Patient Gender")
            page = input("Enter new Patient Age")
            p1 = patient(pid, pname, pdiag, pgender, page)
        if id == p2.get_id():
            pid = id
            pname = input("Enter new Patient Name")
            pdiag = input("Enter new Patient Diagnosis")
            pgender = input("Enter new Patient Gender")
            page = input("Enter new Patient Age")
            p2 = patient(pid, pname, pdiag, pgender, page)
        if id == p3.get_id():
            pid = id
            pname = input("Enter new Patient Name")
            pdiag = input("Enter new Patient Diagnosis")
            pgender = input("Enter new Patient Gender")
            page = input("Enter new Patient Age")
            p3 = patient(pid, pname, pdiag, pgender, page)
        if id == p4.get_id():
            pid = id
            pname = input("Enter new Patient Name")
            pdiag = input("Enter new Patient Diagnosis")
            pgender = input("Enter new Patient Gender")
            page = input("Enter new Patient Age")
            p4 = patient(pid, pname, pdiag, pgender, page)