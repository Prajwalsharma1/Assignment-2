print("Question.1")
input_string="Python is a case sensitive language"

print("(a) part")
#to find the length of string we use a inbuilt funtion len()
print("length of string is:",len(input_string))

print("(b) part")
# to reverse the string we use slicing method
print(input_string[::-1])

print("(c) part")
# to make a new string of " a case sensitive " we use slice method
# index of 'a' is 10 and index of 'e' in sensitive is 25

new_string=input_string[10:26]   # word at index 26 is excluded
#to prove our code we print new_string
print(new_string)

print("(d) part")
# to replace "a case sensitive" by "a object oriented" we use a inbuit funtion named as replace()
print(input_string.replace('a case sensitive', 'a object oriented'))

print("(e) part")
#to find index of "a" in input_string we use find() function
print(input_string.find('a'))

print("(f) part")
# to remove whitespaces we again use replace() function
print(input_string.replace(" ",""))


print("Question.2")
name="Prajwal sharma"
sid=21103020
cgpa=9.0
 #used formatintg strings

print(f'''Hey,{name} is Here!
My SID is {sid}
I am from CSE department and my CGPA is {cgpa}''') 


print("Question.3")
a=56
b=10

print("(a) part")
print(a&b)

print("(b) part")
print(a|b)

print("(c) part")
print(a^b)

print("(d) part")
a = a << 2
b = b << 2

print("(e) part")
a = a >> 2
b = b >> 4


print("Question.4")
#firtly we take input and make a list of nubers given by user

numbers=[]
for count in range(3):
    a=float(input("Please enter your number: "))
    numbers.append(a)
max=numbers[0]            #here we assume that number at index 0 is greatest    
for number in numbers:
    if number > max:
        max=number
print("Greatest number is : ", max)    


print("Question.5")
entry=input("enter someting : " )

#now we make a list named as lis of seperate words present in entry using inbuilt funtion split()

lis=entry.split()

#now we use for loop to check "name" is present in user entry
for word in lis:
    if word == "name":
        print(" yes")
        break  #if name is present then we break next iterations
else:
     print("No")


print("Question.6")
# len_1 means length of first side

len_1=int(input("Enter first side length: "))
len_2=int(input("Enter second side length: "))
len_3=int(input("Enter third side length: "))

if len_1 + len_2 > len_3 and len_1 + len_3 > len_2 and len_3 + len_2 > len_1 :
    print("YES,triangle can be formed")
else:
    print("NO,triangle can not be formed")
