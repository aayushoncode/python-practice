# learning classes and object 

# class student ():
#     def __init__(self,name,cgpa,subject,course): # parameterizes constructor
#         self.name = name 
#         self.cgpa=cgpa
#         self.subject=subject
#         self.course=course

# stu1 = student("ayush",9.0,"python","bca")
# print(f"{stu1.name} has {stu1.cgpa} cgpa \nsubject : {stu1.subject} \ncourse : {stu1.course}")


# methods instance , class and static

# class laptop :
#     storage_type = "ssd"
#     def __init__(self,RAM,STORAGE,GRACPHICS):
#         self.RAM = RAM
#         self.STORAGE = STORAGE
#         self.GRACPHICS = GRACPHICS
#     @classmethod
#     def get_storage(cls):
#         print(f"the storage_type of laptop is : {cls.storage_type}")
#     def get_info(self):
#         print(f"the laptop has ram = {self.RAM} storage {self.STORAGE} {self.storage_type} and graphics is {self.GRACPHICS}")
#         return ""
#     @staticmethod
#     def calc_price(price,discount):
#         final_price = price - (discount*price/100)
#         print(f"the final price is {final_price}")
        

# lap1 = laptop("32gb","1tb","NVIDIA 4060")
# # laptop.get_storage()

# lap1.calc_price(50_000,10)






# design and create an online store for product (name , price)
#track total products being created 
#create a stactic method to calculate discount on each product based on 
# a % parameter 





# class Rented_cars :
#     def __init__(self,LdPRICE):
#         self.BMW=40_00000
#         self.BMW_PRICE=PRICE
#     def get_info(self):
#         print(f"{self.BMW} : {self.PRICE}")
#     @staticmethod
#     def calc_price(price):


# class students :
#     subject = "science"
#     course = "bca"
#     year = "3rd"

# stu1 = students()
# print(f"course : {stu1.course}\nsubject : {stu1.subject}\nyear = {stu1.year}")




# class students :
#     college_name = "shri shankaracharya professional university"
#     def __init__(self,name):
#         self.name = name


# stu1 = students("ayush")
# stu2 = students("ridhi")
# stu3 = students("ayushi")

# print(stu1.name)
# print(stu2.name)
# print(stu3.name)




# class laptop :
#     laptop_name = "asus"
#     laptop_storage = "ssd"

#     def __init__(self,RAM,STORAGE):
#         self.RAM = RAM
#         self.STORAGE = STORAGE

# L1 = laptop("16GB ","512GB")

# print(f"laptop name : {laptop.laptop_name} \nram : {L1.RAM} \nstorage : {L1.STORAGE} {laptop.laptop_storage}")






# class company :
#     company_name = "AK production"

#     def __init__(self,emp_name,emp_designation,emp_id,emp_salary):
#         self.emp_name = emp_name
#         self.emp_designation = emp_designation
#         self.emp_id = emp_id
#         self.emp_salary = emp_salary
#     @classmethod
#     def get_company_name(cls):
#         return f"company name : {cls.company_name}"
#     def get_info(self): #instance method 
#         return f"\nemployee name : {self.emp_name}\nemployee designation : {self.emp_designation}\nemployee id : {self.emp_id}\nemployee salary : {self.emp_salary}"


# emp1= company("ayush", "software engineer", "001", "35lpa")

# print(company.get_company_name(), emp1.get_info())



"""
design and create an online store for products (name , price ).
track total products being created. 
create a static method to calculate discount on each product based on a % paramenter

"""


# class online_store :

#     def __init__(self,name,price):
#         self.name = name 
#         self.price = price

#     @staticmethod
#     def calc_discount(price, discount):
#         return price - (discount *(price/100))
         
    
#     def get_info(self):
#         fp = online_store.calc_discount(self.price,10)
#         return f"product name : {self.name}\nproduct price : {self.price}\nprice after discount : {fp} "



# p1 = online_store("samsung s22 ultra", 50_000)

# print(p1.get_info())





class product :
    product_name = "super_bike"
    count = 0

    def __init__(self,name,engine,price):
        self.name = name
        self.engine = engine
        self.price = price
        product.count+=1

    
    @staticmethod
    def calc_discount (price) :
        return int(price - (10 * (price/100)))
    
    def get_info(self):
        return f"bike : {product.product_name}\nname : {self.name}\nengine : {self.engine}\nprice : {self.price}\nprice after 10% discount : {self.calc_discount(self.price)}"
    
    @classmethod
    def product_count(cls):
        return f"the no. of products are : {cls.count}"

    

b1 = product("GT","650cc",5_00000)
b2 = product("royal enfield classic","350cc",2_44000)
b3 = product("royal enfield standard","350cc",2_06000)


print(b1.get_info())
print(b2.get_info())
print(b3.get_info())
print(product.product_count())
