# 01  display the result to output

 #print("Hello Abdullah")
 #print (34)
 #print (True)
 #print(type(True))

# 02 - legal name of varaiables

# name = "khurram" 
# firstName = "Ali" #camel case;
# FirstName = "aslam" #pascal case;
# first_name= "ali" #snake case;
# name1st= "Ali" #number case; case sensitive

# 03  type of varaibles;

#print (type(23))
#print (type(True))
#print(type("34"))

# 04 data types in python (10)

#a="string" #string 
#b=True     #boolean
#c=34       #integer
#d=1j  #complex
#e=34.5 #float
#f= ["Aslam", "amna", "mehmoona"] #array

#print(len(f))

#g = ("hello", "world" , "!")  #list
#h = {"name":"Abdullah", "age":"20"} # dictionary
#i= b"hellow world" #bites
#j= {"hi","many","fight"} #set
#print(type(j),j)

# 05 math operation

#a=5
#b=4
#sum = a+b
#print(sum, type(sum))

# 06 input type

#a= input("Enter your name :")
#print(a)

#07 if condition

#num=90

#if num == 45:
    #print("you are passed")
#elif num >=90:
    #print("you are passed with Grade A")    
#else :
    #print("you are not passed")   

#num=90

#if (num >= 45 and num <=50):
    #print("you are passed")
#elif ( num >=90 and num > 101):
    #print("you are passed with Grade A")    
#else :

    #print("you are not passed")


#num = 30
#num2 =40
#if num==20:
    #if num2==40:
        #print("You got both right")      #nested
    #else:  
        #print("You ot 2nd wrong")
#else:
    #print("Ypu got both wrong")     

#08 Type casting    

#num ="45"
#num = int(sum)
#print(type(num)) 

#num2 =45
#num2 = str(num2)
#print(type(num2))

#num3 = "43.0"
#num3 = float(num3)
#print(type(num3))

#val= input("Enter your age in numbers :")
#val1 = int(val)
#print(type(val1) , type(val))


#edu = 12
#age = 18-32
#height = 5.6



#if (edu>=12 and age==18-32 and height >= 5.6):
   # print("You are selected")
#else:
    #print ("You are not selected")    

#edu = int(input ("Enter Your education: "))
#age = int(input ("Enter Your age: "))
#height = float(input ("Enter Your height: "))



#if (edu>=12 and (age>=18 and age<=32)):
#    print("Passed")
#elif((age>=18 and age<=32) and height >=5.6):
#    print("Passed")
#elif(height >=5.6 and edu>=12):
#    print("Passed")
#else:
#    print("failed")       

 #09 Multiline String
 
    

#10 concatenation

#a= "hello"
#b= "world"

#print(a+b) # or print(a+" " +b)

#a=42
#b=43
#print(str(a)+ str(b))

# format in string and integers/float

#marks=45
#total="Your total marks is 100 and you get{}"
#obt= total.format(marks)
#print(obt)

#age= 24
#total= 100
#obt= 90

#res= "Your age is{}and your total marks is{} and obtain marks is{}"
#tot= res.format(age,total,obt)
#print(tot)

#age= 24
#total= 100
#obt= 90

#res= "Your age is {2} and your total marks is {1} and obtain marks is {0}"
#tot= res.format(obt,total,age)
#print(tot)

#12 string slicing

#a= "hello world!"
#print(a[0:2])

#a= "hello world!"
#print(a[2:5])  # print(a[0:])   #print(a[:5])

#13 split AI class

#a= "Hello AI clasas"
#b= a.split(",") 
#b= a.split(" ")
#print(a,b)

#Question= P= "Hello world How world is good" Question for Tomorrow

#14 upper case lower case

#st="Helloo world"

#up= st.upper()
#lo= st.lower()
#print(up,lo)

#print(st.upper(), st.lower())


#a= "Hello"
#b= "world"

#print(a.capitalize()+" "+ b.capitalize())

#assignment 2

#a = "jaramala"
#b = "faislabad"
#c = "lahore"

#cap = a[0].upper() + a[1:]
#cap1 = b[0].upper() + b[1:]
#cap2 = c[0].upper() + c[1:]

#print(cap, cap1, cap2)

                       #or

#a= "jaranwala faislabad lahore"

#print(a[0:1].upper()+a[1:9] , a[10:11].upper()+a[11:20], a[20:21].upper()+a[21:])

#a= "Jaranwala Faislabad Lahore"

#print(a[0:1].lower()+a[1:9].upper() , a[10:11].lower()+a[11:20].upper(), a[20:21].lower()+a[21: ].upper())

#15 replace method

#a= "hello"
#b= a.replace("h" , "p")
#print(b)

#a= "jaranwala"
#b="faislabad"
#c="lahore"
#cap1= a.replace("j","J")
#cap2= b.replace("f","F")
#cap3= c.replace("l","L")
#print(cap1,cap2,cap3)

#b=15000
#perc=22
#print((b/perc)*100)

                        #or
#b= input("Enter bonus:")
#perc= input("Enter percentage: ")
#print((b/perc)*100)       

#assignment 03

#st="Jaranwala Faislabad Lahore Karachi Multan" # dont use slice or others and replace first letters in small

#st=(st.replace("J","j").replace("F","f").replace("L","l").replace("K","k").replace("M","m"))

#print(st)

#15   lists  (VIP)

#ls= ["Lahore","Faislabad","Jaranwala"]
#ls= []
#print(type(ls),ls)
#print (type(ls),ls)

#ls1= list(("Lahore","Faislabad","Jaranwala"))  # constructor method
#print(ls1)

#ls=["Lahore","Faislabad", "Jaranwala"]
#print(ls[2:3])

#ls=["Lahore","Faislabad","Jaranwala"]
#ls[1:2]=["Multan"]
#ls[2:3]=["Islamabad"]
#ls[0:1]=["Chakwal"]
#ls[0:]=["Multan","Islamabad","Chakwal"]
#print (ls)

#ls=["Lahore","Faislabad","Jaranwala"]
#ls.append("Chakwal") # add at end
#print(ls)


#ls=["Lahore","Faislabad","Jaranwala"]
#ls.insert(2,"Chakwal") #add where you want
#print(ls)

#ls=["Lahore","Faislabad","Jaranwala"]
#ls.pop(0) # remove
#print(ls)

#ls=["Lahore","Faislabad","Jaranwala"]
#ls.remove("Jaranwala")
#print(ls)

#ls=["Lahore","Faislabad","Jaranwala"]
#ls.clear()
#print(ls)

#la=["apple","banana","mango"]

#for item in la:
    #print(item)    #it also for loop and for in loop

#ls=["lahore","faislabad","jaranwala"]
#ls[0:1]=["LahorE"]
#ls[1:2]=["FaislabaD"]
#ls[2:3]=["JaranwalA"]
#print(ls)


#ls=["lahore","faislabad","jaranwala"]
#lp=[]
#for x in ls:
    #p=x[0:1].upper()+x[1:-1].lower()+x[-1:].upper()
    #lp.append(p)
    #print(p)

#print(lp)    

#ls = ["lahore", "faislabad", "jaranwala"]
#lp = []

#for x in ls:
   # p = x[0:1].lower() + x[1:2].upper() + x[2:-2].lower()+x[-2:-1].upper()+x[-1:].lower()
    #lp.append(p)
    #print(p)
#print(lp)  

#ls= ["Lahore","Faislabad","Peshawar","Islamabad","Jaranwala"]
#ls[0:1]=["Jaranwala"]
#ls[1:2]=["Islamabad"]
#ls[2:3]=["Peshawar"]
#ls[3:4]=["Faislabad"]
#ls[4:5]=["Lahore"]
#print(ls)

#ls= ["Lahore","Faislabad","Peshawar","Islamabad","Jaranwala"]
#lp=[]

#for x in ls:
   # lp.insert(0,x)
#print(lp)    
 
 #write 10 cities first reverse this and then first and ast letter is capital (if it is mistaken capital in between letters so it will automatically small)

#Cities =["Lahore", "Karachi", "Islamabad", "Faisalabad", "Peshawar", 
     #   "Quetta", "Multan", "Rawalpindi", "Sialkot", "Hyderabad"]
#b=[]
#for x in Cities:
 #   b.insert(0,x)
#print(b)    

#c=[]
#for x in Cities:
   # p=x[0:1].upper()+x[1:-1].lower()+x[-1:].upper()
   # c.append(p)
   # print(p)
#print(c)

# 17 for loop while loop

#ls= ["Karachi", "Jaranwala","Fiaslabad"]

#for x in range(len(ls)):
   # print(ls[x], x+1)

#i=0
#while i < len(ls):
   # print(ls[i])
   # i=i+1

    # 18 range

#for x in range(1,10):
      #  print(x)

#for x in range(1,10,2):
 #print(x)

#for x in range(0,21,2):
 # print(x)

# 19 list comprehension

#ls=[x for x in range(2,10,2)]
#print(ls)

#ls=["Karachi", "Islamabad", "Multan", "kivi","test"]
#ls2=[x for x in ls if "a" in x]

#for x in ls:
    #if "a" in x:
       # ls2.append(x)

#print(ls2)        


#ls=["Karachi", "Islamabad", "Multan", "kivi","test"]
#ls2=[x for x in ls if "i" in x]

#for x in ls:
    #if "a" in x:
       # ls2.append(x)

#print(ls2)

#ls=["Karachi", "Islamabad", "Multan", "kivi","test"]
#[print(x) for x in ls if "i" in x]

#for x in ls:
    #if "a" in x:
       # ls2.append(x)

#print(ls2)


#ls=["Karachi", "Islamabad", "Multan", "kivi","test"]
#ls2= [x for x in ls if x!="Karachi"]
#print(ls2)

#ls=["karachi", "islamabad", "multan", "kivi","test"]
#ls2= [x[0].upper()+x[1:] for x in ls ]
#print(ls2)

#ls=["karachi", "islamabad", "multan", "kivi","test"]
#ls2= [x.capitalize() for x in ls]
#print(ls2)


#ls=["karachi", "islamabad", "multan", "kivi","test"]
#ls2=[x[0].upper()+x[1:-1].lower()+x[-1:].upper() for x in ls]
#print(ls2)

#ls=["2*1=2","2*2=4","2*3=6","2*4=8","2*5=10","2*6=12","2*7=14","2*8=16","2*9=18","2*10=20"]
#[print(x) for x in ls if "2"in x]

#ls=[]

#ls.append(input("Enter number: "))
#ls.append(input("Enter number: "))
#print(ls)



# 20 tuples

#tup=("hello","world")  # tup("hello",) then we show it tuple

#print(type(tup))
#print(tup[1])
#print(tup[0:-1])

#tup=("hello",)

#del tup

#print(tup)

#tp=tuple(("hello"),)

#print(type(tp))

#tp=tuple(("hello"),)
#ls= list((tp))
#print(ls)                   MIT Question 1: What is deep copy and shell copy

#tp=tuple(("hello"),)
#ls= list((tp))
#ls.append("guru99")
#print(ls)

#tup1=("tup 1",)
#tup2=("tup 2",)
#tup3= tup1 + tup2
#print(tup3)

#tup=("yellow","orange","blue","green","violet",)
#print(tup,)

#tup=("pythons",)
#print(type(tup))

#tup2=("apple", "banana", "cherry")
#tup3=list((tup2))
#print(type(tup3), tup3)

#tup= ("semester","annual","master")
#(tup1,tup2,tup3)=tup

#print(tup1)

#tup= ("semester","annual","master","mphil")
#(tup1,tup2,*tup3)=tup
#print(tup3)

# 21 Sets

#st={"hello","world"}
#st=set(("hello","world","!"))

#print(type(st))
#print(st)

#st=set(("hello","world","!"))
#st.add("philosphere")
#st.add("menus")

#print(st)

#st=set(("hello","world","!"))
#st2=set(("Philosphere","hello menu"))
#st.update(st2)
#print(st)

#st=set(("hello","world","!"))
#st2=set(("Philosphere","hello menu"))
#st.update(st2)
#st.remove(("world"))
#print(st)

#st1={'hello','world','!'}
#st2={'menu','food','!'}
#st3=st1.union(st2)
#st3=st1.intersection(st2)
#st3=st1 & st2
#st3=st1.difference(st2)
#st3=st1-st2
#print(st3)

# 22 dictionaries

#dic = {"name":"amna"}
#dic =set({"name","amna"})
#print(type(dic))

# dic =list([{"name","amna"}])
# print(type(dic),dic)

#dic = {"name":"amna","age":24}
#print((dic),len(dic))              CRUD= Create Read Update Delete

# dic = {"name":"amna","age":24}     for create
# #print(dic["name"]) or 
# print(dic.get("age")) 

# dic = {"name":"amna","age":24}   # for update
# # dic["name"]="bushra"
# dic["color"]="green"
# print(dic)

# dic = {"name":"amna","age":24}
# # dic.update({"height":5.7,})
# # dic.pop("name")
# # dic.popitem()
# print(dic.keys())  #give keys
# print(dic.values()) #get values
# print(dic.items())  #get items with seperate names

# pass by reference /pass by value ----------------------------------------------------------------

# a=10       pass by value ----------------------------------------------------------------
# b=a
# a=20
# print(a,b)

# dic1={"name":"amna","age":"20"}     # pass by reference
# dic2=dic1

# dic1["name"]="kubran"
# print(dic1,dic2)

#24  copy dictionary----------------------------------------------------------------

# dic1={"name":"amna","age":"20"}
# # #dic2=dic1.copy()                             it gives different names
# # dic2={"name":"amna","age":"20"}
# dic2= dict(dic1)
# dic1["name"]="kubran"

# print(dic1,dic2)

# 25 function----------------------------------------------------------------

#kivi android apps

# def s():
#     print("Hello world")

# s()   

# def func(name,age):
#     print( "hello world" + name + str(age ) )
    
# func("akash", 25)    

# def func(name="Ali",age=24):
#     print( "hello world" + name + str(age ) )
    
# func("akash", 25)
# func()

# def func(name,age,scale):
#     print(name+str(age)+str(scale))
# func("akash", 25, 16)    

# def func(name,*age):
#     print(name+ " "+ str(age[1]))
# func("akash", 25, 16)

# def func(**krgs):
#     print(krgs)

# func(name="akash", age= 34)    

# def func(**krgs):
#     print(krgs["name"]+" "+ str(krgs["age"]))

# func(name="akash", age= 34)

# def fun():
#     pass
# fun()
# 26 exception handling----------------------------------------------------------------

# x=23
# try:
#     print(x)
# except:
#     print("koi answer nahi") 
# finally:
#     print("This is always executed")   

#27 anonymous function

# x= lambda a: a*2

# print(x(5))

# x= lambda a,b: a**b

# print(x(5,2))

# x= lambda a,b,c: a*b/c

# print(int(x(5,2,2))


# def sum():
#     print("Hello World")    
# sum()
    
# def sum():
#     print(("42"))
# sum()    

# def num():
#     a=10
#     b=90
#     print(a+b)
# num()

# def sum(c,d):         # parameters
#     print(c+d)
# sum(10,99)    # arguments

# def sum(e=20,f=5):
#     print(e+f)
# sum(100,100)    

# def sum(g,h):
#     print("hello world {} : {}".format(g,h))
# sum(10,20)    

# def sum(g,*h):
#     print(f"hello world {g} : {h[0]} : {h[1]}")
# sum(10,20,40)       
     
# def sum(g,*h):
#     print(f"Hello world {g} : {h}")
# sum(10,20,30,40)    

# def sum(i,**j):
#     print(f"Hello world how are you. {j}")
# sum(10,nume="Abdullah",age=20)    

# def mul():
#     a=20
#     b=5
#     print(a*b)
# mul()    

# def name(first_name,last_name):
#     print("My name is:", first_name , last_name)
# name("Abdullah","Nadeem")    

# def num():
#     a=2
#     a=a*a
#     print("The square of 2 is:",a)
# num()    

# def ap():
#     a=23
#     if a%2==0:
#         print("The number is even")
#     else:
#         print("The number is odd")
# ap()        

# def h(width,height):
#     area=width*height
#     print("The area of rectangle is",area)
# h(5,10)    

# def greet(name="Guest"):
#     print("Hello" + "" + name + "" + "Congrats!") 
# greet("Abdullah")    

# def num(*numbers):
#     print("The total sum is:",sum(numbers))
# print(10,20,30)    

# def num(*numbers):
#     print("the maximum value among is:",min(numbers))
# num(10,30,50,70)    


# def person(a, **b):
#     print(f"His name is {a}")
#     print(f"His age is {b['age']}")
#     print(f"He lives in {b['city']}")

# person("Abdullah", age=20, city="Lahore")
  

#28 OOPs in Python--------------------  class and objects with using of set and get

# class Employee:
#     #pass
#     def setEmp(self,name,age):
#         self.name= name
#         self.age=  age
#     def getEmp(self):
#         print(f"{self.name}:{self.age}")    

# ab=Employee()
# ab.setEmp("Abdullah",23)
# ab.getEmp()


# class Person:
#     def setper(self,location,city):
#         self.location=location
#         self.city=city
#     def getper(self):
#         print(f"his live location is {self.location} and city is {self.city}")

# ab=Person()
# ab.setper("Jaranwala","Faislabad")
# ab.getper()

# class me:
#     def setme(self,name,age):
#         print(f"my name is {name} and age is {age}")
# ab=me()
# ab.setme("Abdullah",20)


# class Employee:
#     #pass
#     def setEmp(self):
#         self.name= "Abdullah"
#         self.age=  20
#     def getEmp(self):
#         print(f"{self.name}:{self.age}")    

# ab=Employee()
# ab.setEmp()
# ab.getEmp()

# #now using constructor method

# class Employee:
#     #pass
#     def __init__(self):
#         self.name= "Abdullah"
#         self.age=  20
#     def getEmp(self):
#         print(f"{self.name}:{self.age}")    

# ab=Employee()
# ab.getEmp()

# # class Employee:
# #     #pass
# #     def __init__(self):
# #         self.name= input("Enter name:")
# #         self.age=  int(input("Enter age: "))
# #     def getEmp(self):
# #         print(f"{self.name}:{self.age}")    

# # ab=Employee()
# # ab.getEmp()

# # polymorphism using

# class Car:
#     def __init__(self,name):
#         self.name=name
#     def func(self):
#         print(f"hello sky man {self.name}")    
# class Bus:
#     def __init__(self,name):
#         self.name=name
#     def func(self):
#         print(f"hello drown man {self.name}")       
# ab=Car("Cultus")
# ac= Bus("Speedo")

# ab.func()
# ac.func()

# class Car:
#     def __init__(self):
#         self.name="Cultus"
#     def func(self):
#         print(f"hello sky man {self.name}")    
# class Bus:
#     def __init__(self):
#         self.name="Speedo"
#     def func(self):
#         print(f"hello drown man {self.name}")       
# ab=Car()
# ac= Bus()

# ab.func()
# ac.func()

#by using inheritence
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         print(f"Your {self.name} voice is meow")    
# class Cat(Animal):
#     def __init__(self,name):
#         self.name=name
#     def sound (self):
#         print(f"Hello {self.name} your voice is waoh")    

# class Dog(Animal):
#     def __init__(self,name):
#         self.name=name

#     def sound(self):
#         print(f"hello {self.name} your voice is bark")

# ab= Cat("cat")
# ac= Dog("dog") 
# ad= Animal("Elephant")   

# ab.sound()
# ac.sound()
# ad.sound()

# class Sum:
     
#     def setSum(self,a,b):
#          self.a= a
#          self.b= b
         
#     def getSum(self):
#          sum=self.a+self.b
#          print(f"The sum is : {sum}")    

# ab=Sum()
# ab.setSum(15,20)
# ab.getSum()

# class Sum:
     
#      def setSum(self):
#           self.a= int(input("Enter a Number "))
#           self.b= int(input("Enter a Number "))
         
#      def getSum(self):
          
#           print(f"The sum is : {self.a+self.b}")    

# ab=Sum()
# ab.setSum()
# ab.getSum()

# class Employee:
#     def __init__(self):
#         self.name="Abdullah"
#         self.age=str((20))
#         self.name1="Ali"
#         self.age1=str((24))
#         self.name2="Ahmad"
#         self.age2=str((25))
#         self.name3="Raza"
#         self.age3=str((26))
#         self.name4="Zohaib"
#         self.age4=str((27))
#     def getEmp(self):
#         print(f"my name is {self.name} and age is {self.age}")
#         print(f"my name is {self.name1} and age is {self.age1}")
#         print(f"my name is {self.name2} and age is {self.age2}")
#         print(f"my name is {self.name3} and age is {self.age3}")
#         print(f"my name is {self.name4} and age is {self.age4}")
# ab=Employee()
# ab.getEmp()    

# class Employee:
#     def setEmp(self,name,age):
#         self.name=name
#         self.age=str((age))
#     def getEmp(self):
#         print(f"my name is {self.name} and age is {self.age}")
        
# ab=Employee()
# ab.setEmp("Abdullah",20)
# ab.getEmp()
# bc=Employee()
# bc.setEmp("Ali",24)
# bc.getEmp()
# cd=Employee()
# cd.setEmp("Ahmad",26)
# cd.getEmp()
# ef=Employee()
# ef.setEmp("Raza",25)
# ef.getEmp()
# gh=Employee()
# gh.setEmp("Riaz",30)
# gh.getEmp()

# class Num:
#     def __init__(self, *Number):  
#         self.number = Number      

#     def getNum(self):
#         print(f"The sum is: {self.number[0]+self.number[1]}")


# ab = Num(23, 24)
# ab.getNum()

# by using **kwargs display name age and marks with above method

# class Person:
#     def __init__(self, **Employee):  
#         self.Employee = Employee      

#     def getPer(self):
#         print(f"The name is {self.Employee["name"]} age is {self.Employee["age"]} and marks is {self.Employee["marks"]}")


# ab = Person(name="Abdullah",age=20,marks=90)
# ab.getPer()

# class Person:
#     def __init__(self, **Employee):  
#         self.Employee = Employee      

#     def getPer(self):
#         print(f"The name is {self.Employee["name"]} age is {self.Employee["age"]} and marks is {self.Employee["marks"]}")
        

#         if self.Employee["marks"]>=90:
#             print("You get a Grade")
#         if self.Employee["marks"]>=80:
#             print("You got B Grade")
#         if self.Employee["marks"]>=70:
#             print("You got C Grade")
#         if self.Employee["marks"]<=70:
#             print("You are failed")    

# ab = Person(name="Abdullah",age=20,marks=78)
# ab.getPer()

# class Student:
#     def setStudent(self,name,rollnumber):
#         self.name=name
#         self.rollnumber=str(rollnumber)
#     def getStudent(self):
#         print(f"The Student name is {self.name} and roll number is {self.rollnumber}")
# ab=Student()
# ab.setStudent("Abdullah",21) 
# ab.getStudent() 

# class Book:
#     def setBook(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#     def getBook(self):
#         print(f"Book name is {self.title}, author is {self.author}, price is {self.price}")

# ab=Book()
# ab.setBook("Rich Dad and Poor Dad", "Williams",2000)
# ab.getBook()

# class Laptop():
#     def __init__(self,):
#         self.brand="Dell"
#         self.model="I5"
#         self.price= 50,000 
#     def getLap(self):
#         print(f"The brand is {self.brand}, the model is {self.model}, the price is {self.price}")   
# ab=Laptop()
# ab.getLap()    

# class Movie():
#     def __init__(self):
#         self.title="Jawan"
#         self.director="Shahrukh Khan"
#         self.rating= 3.5
#     def getMovie(self):
#         print(f"The movie is {self.title} and director was {self.director}, and ratings : {self.rating}")    
# ab=Movie()
# ab.getMovie()        

# class Shape:
#     def __init__(self,area):
#         self.area= area
#     def area(self):
#         print(f"The area is {self.area}")



# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print(f"The area of the rectangle is: {self.length * self.width}")

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         area = 3.14 * self.radius * self.radius
#         print(f"The area of the circle is: {area}")


# rect = Rectangle(5, 4)
# circ = Circle(3)


# rect.area()
# circ.area()



# class Vehicle:
#     def description(self):
#         print(f"This is Beautiful Vehicle")
# class Car(Vehicle):
#     def __init__(self):
#         self.Model= 2014
#         self.name= "Cultus"
#     def description(self):
#         print(f"The car model is {self.Model} and name is {self.name}")
# class Bike(Vehicle):
#     def __init__(self):
#         self.name="Honda 70"
#         self.model= 2020
#     def description(self):
#         print(f"The bike name is {self.name} and model is {self.model}")
# ab=Car()
# bc=Bike()
# ac=Vehicle()
# ab.description()
# bc.description()                       
# ac.description()               


# class Cat:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f"The name of cat is {self.name}")
# class Dog:
#     def __init__(self,name):
#         self.name=name
#     def speak(self): 
#         print(f"The name of Dog is {self.name}") 
# ab=Cat("Tommy")         
# bc=Dog("Archana")       
# ab.speak()
# bc.speak()      

#simple inheritence

# class Father:
#     def ft(self):
#         print("Father Classes")
# class Child(Father):
#     pass

# ab=Child()
# ab.ft()


# #multiple inheritence

# class Father:
#     def ft(self):
#         print("Father Classes")
# class Mother:
#     def mt(self):
#         print("Mother classes")
# class Child(Mother,Father):
#     pass

# ab=Child()
# ab.ft()
# ab.mt()

# class Model:
#     def ft(self):
#         print(2016)
# class Name:
#     def mt(self):
#         print("Cultus")   
# class Car(Model,Name):
#     pass
# ab=Car()
# ab.ft()
# ab.mt()        

# multilevel inheritence

# class Grandpa:
#     def gp(self):
#         print("Fazal Elahi")
# class Parents(Grandpa):
#     def prnt(self):
#         print("Parents")
# class Child(Parents):
#     def chld(self):
#         print("Child")
# class Grandchild(Child):        
#     pass                

# ab=Grandchild()
# ab.prnt()
# ab.gp()
# ab.chld()

# # heirarical inheritance

# class Parent:
#     def prnt(self):
#         print("This is parent class")
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass 

# ab=Child1()
# ab.prnt()

# by using super with adding in parent child after


# class Parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def smt(self,birthday):
#         print(f"Hi {self.name} your age is {self.age} and your birthday is {birthday}")
# class Child(Parent):
#     def __init__(self,name,age,education):
#         self.education=education
#         super().__init__(name,age)
#     def tmt(self):
#         print(f"Your education is {self.education}")    
        
# ab=Child("Abdullah",20,23)
# ab.smt("5th may")        
# ab.tmt()                    

# class Car:
#     def st(self):
#         print("This is car")
# class Model(Car):
#     pass
# ab= Car()
# ab.st()        


# class Model:
#     def st(self):
#         print(2018)
# class Name:
#     def mt(self):
#         print("Prado")
# class Car(Model,Name):
#     pass

# ab=Car()
# ab.mt()
# ab.st()

# class Model:
#     def st(self):
#         print("2019")
# class Name(Model):
#     def mt(self):
#         print("Cultus")
# class Car(Name):
#     def gt(self):
#         print("Black")
# class Foundation(Car):
#         pass   
# ab=Foundation()
# ab.gt()
# ab.mt()
# ab.st()          

# class Car:
#     def tn(self):
#         print("The car color is black")
# class Model(Car):
#     pass
# class Model1(Car):
#     pass

# ab=Model()
# ab.tn()

# class Car:
#     def __init__(self,name,model):
#         self.name=name
#         self.model=model
#     def tm(self,color):
#         print(f"The name of car is {self.name} and model is {self.model} and color is {color}") 
# class Requirement(Car):
#     def __init__(self,name,model,develpement):
#         self.development=develpement
#         super().__init__(name,model)
#     def tmt(self):
#         print(f"The development in {self.development}")
# ab= Requirement("Cultus",2018,"Huandei")
# ab.tm("Black")
# ab.tmt()                     
