ls =[]
class Student:
    def __init__(self,name , roll , m1 , m2):
        self.name = name
        self.roll = roll
        self.m1 = m1
        self.m2 = m2

    def accept(self):
        name = input("enter name of student ")
        roll = int(input("enter roll no "))    
        m1 = int(input("enter marks 1 "))
        m2 = int(input("enter marks 2 "))
        stu  = Student(name , roll , m1 , m2)
        ls.append(stu)

    def display(self , ob):  
        print(f"Name : {ob.name}")
        print(f"roll no : {ob.roll}")
        print(f"marks1 : {ob.m1}")
        print(f"marks2 : {ob.m2}")

    def delete(self , roll):
        student = stu.search(roll)
        del ls[student]

    def search(self , roll):
        for student in ls:
            if(student.roll == roll):
                return student
            
    def update(self , roll , newroll):
        student = stu.search(roll)
        student.roll = newroll

if __name__ == "__main__":
     stu = Student('',0,0,0)      
     stu.accept()       
     stu.update(1,2)
     stu.display(ls[0])