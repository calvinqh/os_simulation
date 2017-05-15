class Person():
    
    test = 12

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.fat = False

    def setFat(self, var):
        self.fat = var

    def getFat(self):
        return self.fat

class Student(Person):

    def __init__(self, age):
        Person.setFat(self,True)
        self.age = age
        self.test = 13

p = Person('Calvin','Quach')
c = Student(10)
print(c)
print(c.age)
print(c.getFat())
print(p.test)
print(Person.test)
print(c.test)
print("---------------")
z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(z)
print("Up to 3",z[:3])
print("After 3",z[3:])
print('{}'.format(2))
