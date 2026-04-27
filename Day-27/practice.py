
def add(*args): #*args can take any number of values unlimited argument
    print(args[5])
    sum_of=0
    for x in args:
        sum_of=sum_of+x
    return sum_of

print(add(1,2,7,5,4,78,4,4,58,4,54,5))


def calculate(n,**kwargs):
    print(kwargs) #type is dict
    # for key,value in kwargs.items(): #for loop for dictionary
    #     print(key)
    #     print(value)
    #     print(kwargs["add"])

    n+=kwargs["add"]
    print(n)

calculate(3,add=3,multiply=5,subtract=9)

#
# class Car:
#     def __init__(self,**kw):
#         self.make=kw["make"] #this will give error if key not specified
#         self.model=kw.get("model") #if we use get and if key is not presnet then no error
#
# car=Car(make="lambo")
# print(car.make) #if only this runs no error cause make is mentioned because we used .get() in model
# car1=Car(model="gta5")
# print(car1.model) #car1 will give error cause make is not mentioned but car does not give error with model cause model uses get()
