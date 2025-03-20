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

Cities =["Lahore", "Karachi", "Islamabad", "Faisalabad", "Peshawar", 
        "Quetta", "Multan", "Rawalpindi", "Sialkot", "Hyderabad"]
b=[]
for x in Cities:
    b.insert(0,x)
print(b)    

c=[]
for x in Cities:
    p=x[0:1].upper()+x[1:-1].lower()+x[-1:].upper()
    c.append(p)
    print(p)
print(c)    