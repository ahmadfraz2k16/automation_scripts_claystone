import re

def input_fname():
    first_name = input("enter first name")
    return first_name

def input_lname():
    last_name = input("enter last name")
    return last_name

def input_email():
    email = input("enter email")
    return email

def input_age():
    age = input("enter age")
    return age

def input_mobile_number():
    mobile_number = input("enter mobile number")
    return mobile_number

def input_landline_number():
    landline_number = input("enter landline number")
    return landline_number

check = False
while(check == False):
    first_name = input_fname()
    if len(first_name) < 3:
        print("too short, use length atleast 3 characters")
        check = False
    else:
        if (re.findall(r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$", first_name)):
            print("valid user name")
            check = True
        else:
            print("don't use special characters, digits")
            check = False

check2 = False
while(check2 == False):
    last_name = input_lname()
    if len(last_name) < 3:
        print("too short, use length atleast 3 characters")
        check2 = False
    else:
        if (re.findall(r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$", last_name)):
            print("valid user name")
            check2 = True
        else:
            print("don't use special characters, digits")
            check2 = False

check3 = False
while(check3 == False):
    email = input_email()
    if (re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)):
        print("valid email")
        check3 = True
    else:
        print("invalid email")
        check3 = False

check4 = False
while(check4 == False):
    age = input_age()
    if (re.search(r"^(?:1[01][0-9]|90|1[7-9]|[2-9][0-9])$", age)):
        print("valid age")
        check4 = True
    else:
        print("invalid age, enter whole number, minimum age 17 to 90")
        check4 = False

check5 = False
while(check5 == False):
    mobile_number = input_mobile_number()
    if (re.search(r"^((\+92)|(0092))-{0,1}\d{3}-{0,1}\d{7}$|^\d{11}$|^\d{4}-\d{7}$", mobile_number)):
        print("valid mobile Pakistani number")
        check5 = True
    else:
        print("invalid mobile number lenght, enter Pakistani mobile number only, 11 to 14 digits only")
        check5 = False

check6 = False
while(check6 == False):
    landline_number = input_landline_number()
    if not (re.search(r"/^[0-9]+$/", landline_number)):
        if(len(landline_number) == 10):
            print("valid landline Rawalpindi / Islamabad number")
            check6 = True
        else:
            print("landline no Length is not equal to 10")
            check6 = False
    else:
        print("invalid landline number lenght")
        check6 = False

print(first_name)
print(last_name)
print(email)
print(age)
# masking applied to phone no and landline no
if(len(mobile_number) ==11):
    print(mobile_number[0:4]+"-"+mobile_number[4:])

if(len(mobile_number) ==13):
    print(mobile_number[0:3]+"-"+mobile_number[3:6]+"-"+mobile_number[6:])

if(len(mobile_number) ==14):
    print(mobile_number[0:4]+"-"+mobile_number[4:7]+"-"+mobile_number[7:])

if(len(landline_number) ==10):
    print(landline_number[0:3]+"-"+landline_number[3:])

if( check == True and check2 == True and check3 == True and check4 == True and check5 == True and check6 == True):
    print("form submitted successfully")
