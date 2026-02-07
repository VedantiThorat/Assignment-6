class Student:
    def __init__(self, name, marks):
        self.name = name        
        self.marks = marks     

    def display(self):          
        print("Name:", self.name)
        print("Marks:", self.marks)


# object 
v1= Student("Vedanti Thorat", 85)

# calling 
v1.display()
