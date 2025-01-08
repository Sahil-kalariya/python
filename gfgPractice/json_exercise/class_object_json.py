import json

class Student: 
    def __init__(self, roll_no, name, batch): 
        self.roll_no = roll_no 
        self.name = name 
        self.batch = batch 



if __name__ == "__main__":
    st1 = Student(1,"a",2)        
    st2 = Student(1,"asdf",2)        
    st3 = Student(1,"as",2)        

    json_st1 = json.dumps(st1.__dict__)        
    json_st2 = json.dumps(st2.__dict__)           
    json_st3 = json.dumps(st3.__dict__)        

    print(json_st1)
    print(json_st2)
    print(json_st3)