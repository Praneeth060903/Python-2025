username = input("Enter Username: ")

# check if given username has more than 4 characters
if len(username) >= 4:
    print("Actual Given", username)
    print("Fromatted Output", username.lower())
    if username.lower().find("@") != -1:
        print("Valid Email")
    else:
        print("InValid Email")
else:
    print("Username should be atleast 4 or above chars")

pan = input("Enter PAN: ")
formatted_pan = pan.upper()
print("Fromatted PAN", formatted_pan)

mobile = input("Enter Mobile Number: ")
if mobile.startswith("+86"):
    print("Redirect To China")
elif mobile.startswith("+91"):
    print("Redirect To India")
else:
   print("Calling Not Possible")     

email = input("Enter Email: ")
# gmail sync
if email.endswith("@gmail.com"):
    print("Synchronizing account to new gmail")
else:
   print("Synchronizing only there for Gmail") 