class Employee:
    count=0 
    fcount=0
    scount=0
    dcount=0

    def __init__(self, name, des, salary, gender):

        self.name=name
        self.des =des
        self.salary=salary 
        self.gender=gender
        Employee.count= Employee.count + 1
        if self.gender=="Female": 
            Employee.fcount=Employes.                         fcount+1
        if self. salary>10000:
            Employee.scount 
            Employee.dcoust       
        if self.des"Asat Manager":
            Employee.dcount Employee.                         dcount+1 
    def displayCount (self):
            print("The number of employees in the organization are: "
            self.count()
    def displayCount Female(self):                         print("Pomale counts", self.fcount)
    def displayCountSalary (self):
        print ("Salary greater than 10,000, self.scount) def displayCountDes (self):
        print("Designation as Asst Manager count=", self.dcount) def displayp (self):
        print ("Name of Employee is: ", self.name)
        print ("Designation of Employee: ", self.des) 
        print ("Salary of Employee: ", self.salary)

e1= Employee ("Dhara", "Manager", 20000, "Female")"

e2= Employee ("Rahul", "Team Leader", 30000,"Male")

print("Employee Details is:")

e1.displayEmp ()

e2.displayEmp()

print("\n")

e1. displayCount() 
e1.displayCountFemale()

e1.displayCountSalary()

e1.displayCountDes ()