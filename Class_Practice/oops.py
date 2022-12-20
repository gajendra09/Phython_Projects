class CreatePass:
    pass


obj1 = CreatePass()
print(obj1)

class Sum():
    def add(self, a, b):
        return a+b

ob_sum = Sum()
meth_add = ob_sum.add(4,5)
print("The value of sum is {}".format(meth_add))

class BasicCalculator:
    def __init__(self, a, b):                              # init function is used to initialise the parameters/arguments
        self.x = a
        self.y = b

    def sum(self):
        return self.x+self.y

    def diff(self):
        return self.x-self.y

    def prod(self):
        return self.x*self.y

    def div(self):
        return self.x/self.y


obj_calc = BasicCalculator(15,10)
meth_sum = obj_calc.sum()
print("The sum of two values is {}".format(meth_sum))
meth_diff = obj_calc.diff()
print("The difference between two values is {}".format(meth_diff))
meth_prod = obj_calc.prod()
print("The product of two values is {}".format(meth_prod))
meth_div = obj_calc.div()
print("The quotient of two values is {}".format(meth_div))


# inheritance

class EmployeeDetails:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def details(self):
        print("The first name of employee is {} and the last name of employee is {}".format(self.first_name, self.last_name))

class EmployeeOfficialDetails(EmployeeDetails):
    def __init__(self, salary, id_number, first_name, last_name):
        self.salary = salary
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name

    def employee_details(self):
        print("The employee name is {} {} and id number is {} and his salary is {}".format(self.first_name, self.last_name,
                                                                                            self.id_number, self.salary))

obj_child = EmployeeOfficialDetails(10000, 23, "Deekshitha", "Manjunath")
det_emp = obj_child.employee_details()

# multiple inheritence
class Vehicle():
    def __init__(self, colour, fuel_type):
        self.colour = colour
        self.fuel_type = fuel_type

    def type_vehicle(self):
        print("the colour of the vehicle is {} and the fuel type of vehicle is {}".format(self.colour, self.fuel_type))

class CarDetails():
    def __init__(self, veh_num, own_name):
        self.veh_num = veh_num
        self.own_name = own_name

    def car_details(self):
        print("the vehicle no of car is {} and owner name of car is {}".format(self.veh_num, self.own_name))

class VehicleDetails(Vehicle, CarDetails):
    def __init__(self, colour, fuel_type, veh_num, own_name):
        self.colour = colour
        self.fuel_type = fuel_type
        self.veh_num = veh_num
        self.own_name = own_name

    def details(self):
        print("the vehicle no of car is {} and owner name of car is {} and the colour of the vehicle is {} and the fuel type of vehicle is {}".format(self.veh_num, self.own_name, self.colour, self.own_name))

obj_veh = VehicleDetails("Red", "Petrol", 20, "ABC")
det_car = obj_veh.details()


# polymorphism

class Cat:
    def __init__(self, name, age):
        self.name = name
        self. age = age

    def food(self):
        print("Cat eats Whiskes")

    def sound(self):
        print("meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def food(self):
        print("Dog eats drools")

    def sound(self):
        print("bark")

obj_cat = Cat("Teddu", 1)
obj_cat.food()
obj_cat.sound()
obj_dog = Dog("Dheera", 1)
obj_dog.food()
obj_dog.sound()

class SumOperation():
    # def _init_(self, a, b, c):
    #     self.a = a
    #     self.b = b
    #     self.c = c
    #method over loading
    def test(self, a=None, b=None):
        print(a)
        print(b)



sum_obj = SumOperation()
sum_obj.test(3, 4)
sum_obj.test(5)

#method over riding

class Car:
    def __init__(self):
        self.model_name = "XUV_500"
        self.model_year = 2010

    def details(self):
        print("Car model name is {} and year of model is {}".format(self.model_name, self.model_year))

class CarTwo(Car):
    def __init__(self):
        self.model_year = 2010
        self.model_name = "Xuv-300"

    def details(self):
        print("Car model name is {} and year of model is {}".format(self.model_name, self.model_year))


obj_car = Car()
obj_car.details()
obj_car_two = CarTwo()
obj_car_two.details()

# Data Encapsulation
class Parent:
    def __init__(self):
        self.a = "without encapsulation"
        self.__b = "with encapsulation"   # private member of own class

    def encap(self):
        print(self.__b)

    def __get_details(self):
        concat = self.__b+self.a
        return concat

    def encap_details(self):
        print(self.__get_details())

class Child(Parent):
    def __init__(self):
        Parent._init_(self)
        print("Calling non-encapsulate variable is {}".format(self.a))
        # print("Calling encapsulated variable is {}".format(self.__b))
        # self.c = self.__b
        # print("C reading encapsulated data is {}".format(self.c))



obj_parent = Parent()
print(obj_parent.a)
obj_parent.encap()
obj_child = Child()
# print(obj_child.encap())
obj_parent.encap_details()


