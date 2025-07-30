# Python Strings With LMS
print("="*30)
print("LMS Grade Tracking System")
print("="*30)

# While Reading ID, id should be positive 
student_id_valid = False
while not student_id_valid:
    student_id = input("Enter Your ID: ")
    # check if the given input is only numbers
    if student_id.isdigit():
        student_id = int(student_id)
        # check if the number is positive
        if student_id > 0:
            student_id_valid = True
        else:
            print("Please Enter Positive Number or Above Zero")
    else:
        print("Please Enter Numbers Only, Other characters not allowed")

# print(f"Your ID: {student_id}")

# Fromat Student ID 
institute_code = "DE-"
formatted_id = institute_code+"STU"+str(student_id).zfill(5)
print(formatted_id)

# Implement name validations
student_name_valid = False
while not student_name_valid:
    student_name = input("Enter Your Full Name: ")

    # remove spaces and ravi krishna → Ravi Krishna
    student_name = student_name.strip().title()
    # print(student_name)
    
    # name should be only alaphabets and also spaces allowed
    # name check with only spaces allowed
    name_check = student_name.replace(" ","")

    # Minimum 3 characters length validation
    if name_check.isalpha() and len(student_name) >=3:
        student_name_valid = True
        print("Welcome, "+student_name)
    else:
        if not name_check.isalpha():
            print("Name should contain only letters and spaces")
        elif len(student_name) < 3:
            print("Name should contain atleast 3 characters")

# system generated unique email id
name_parts = student_name.split()
# print(name_parts)
first_name = name_parts[0].lower()
# Generate university email
student_email = first_name + "."+str(student_id)+"@edify.edu"
print(student_email)

# Course Fee Input and Discount Calculation
base_course_fee_valid = False
while not base_course_fee_valid:
    base_course_fee = input("Enter Base Course Fee: ")
    if base_course_fee.isdigit():
        base_course_fee = int(base_course_fee)
        if base_course_fee > 0:
            base_course_fee_valid = True
        else:
            print("Enter Course Fee Above Zero or Positive Number")
    else:
        print("Please Enter Numbers Only, Other characters not allowed")

discount = 0
description = input("Enter Description: ")
description = description.lower()

if "reference" in description:
    discount+= 5000
if "scholarship" in description:
    discount+= 7000
if "promo" in description:
    discount+= 3000
# using in operator     
# if description.find("referal") >=0: --> using in built string method

final_fee = base_course_fee - discount
print("="*30)
print("FEE DETAILS")
print("="*30)

print(f"Actual Fee: {base_course_fee}")
print(f"Discount Given: {discount}")
print(f"Final Fee To Pay: {final_fee}")