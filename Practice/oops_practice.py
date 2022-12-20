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

obj_calc = BasicCalculator(15, 10)
meth_sum = obj_calc.sum()
print("The sum of two values is {}".format(meth_sum))
meth_diff = obj_calc.diff()
print("The difference between two values is {}".format(meth_diff))
meth_prod = obj_calc.prod()
print("The product of two values is {}".format(meth_prod))
meth_div = obj_calc.div()
print("The quotient of two values is {}".format(meth_div))

class EmployeeDetails():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def details(self):
        print("The first name of employee is {} and the last name of employee is {}".format(self.first_name, self.last_name))

class EmployeeOfficeDetails(EmployeeDetails):
    def __init__(self, salary, id_number, first_name, last_name):
        self.salary = salary
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name

    def employee_details(self):
        print("the employe name is {} {} and id number is {} and salary is {}".format(self.first_name, self.last_name, self.id_number, self.salary))

objct_child = EmployeeOfficeDetails(50000, 25, "gajendra", "reddy")
det_emp = objct_child.employee_details()

class GrandFather():
    def __init__(self, grand_father_name):
        self.grand_father_name = grand_father_name

    def first_details(self):
        print("grand father name is {}".format(self.grand_father_name))

class Father(GrandFather):
    def __init__(self, father_name):
        self.father_name = father_name


    def second_details(self):
        print("grand father name is {} and father name is {}".format(self.grand_father_name, self.father_name))

class Son(Father):
    def __init__(self, son_name, father_name, grand_father_name):
        self.son_name = son_name
        self.father_name = father_name
        self.grand_father_name = grand_father_name

    def third_detais(self):
        print("grand father name is {} and father name is {} and son name is {}".format(self.grand_father_name, self.father_name, self.son_name))

objct_son = Son("maga", "appa", "tatha")
det_son = objct_son.third_detais()


class Brands():
    def __init__(self, brand_name_1, brand_name_2, brand_name_3):
        self.brand_name_1 = brand_name_1
        self.brand_name_2 = brand_name_2
        self.brand_name_3 = brand_name_3

    # def brands(self):
    #     print("1st brand name is {}, 2nd brand name is {} and 3rd brand name is {}".format(self.brand_name_1, self.brand_name_2, self.brand_name_3))

class Products(Brands):
    def __init__(self, product_1, product_2, product_3):
        self.product_1 = product_1
        self.product_2 = product_2
        self.product_3 = product_3

    # def products(self):
    #     print("1st brand is {} and product is {}".format(self.brand_name_1, self.product_1))
    #     print("2nd brand is {} and product is {}".format(self.brand_name_2, self.product_2))
    #     print("3rd brand is {} and product is {}".format(self.brand_name_3, self.product_3))

class Popularity():
    def __init__(self, popularity_1, popularity_2, popularity_3,  product_1, product_2, product_3, brand_name_1, brand_name_2, brand_name_3):
        self.popularity_1 = popularity_1
        self.popularity_2 = popularity_2
        self.popularity_3 = popularity_3
        self.product_1 = product_1
        self.product_2 = product_2
        self.product_3 = product_3
        self.brand_name_1 = brand_name_1
        self.brand_name_2 = brand_name_2
        self.brand_name_3 = brand_name_3

    def popularity(self):
        print("{} is an {} popularity of {}".format(self.brand_name_1, self.product_1, self.popularity_1))
        print("{} is an {} popularity of {}".format(self.brand_name_2, self.product_2, self.popularity_2))
        print("{} is an {} popularity of {}".format(self.brand_name_3, self.product_3, self.popularity_3))

brnd_details = Popularity(95, 90, 88, "online Ecommerce store", "online shop", "online shopping app", "Amazon", "flipkart", "ajio")
final_brand_details = brnd_details.popularity()

class Vehicle():
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

class VehicleName():
    def __init__(self, vehicle_type, vehicle_name, model):
        self.vehicle_type = vehicle_type
        self.vehicle_name = vehicle_name
        self.model = model

class VehicleDetails(Vehicle,VehicleName):
    def __init__(self, vehicle_type, vehicle_name, model, color, fuel_type):
        self.vehicle_type = vehicle_type
        self.vehicle_name = vehicle_name
        self.model = model
        self.color = color
        self.fuel_type = fuel_type

    def vehicle_details(self):
        print("vehicle type is {},vehicle name {}, model {}, color {}, and fuel_type is {}".format(self.vehicle_type, self.vehicle_name, self.model, self.color, self.fuel_type))

obj_vehicle = VehicleDetails("car", "Audi", 2020, "white", "petrol")
det_vehicle = obj_vehicle.vehicle_details()


