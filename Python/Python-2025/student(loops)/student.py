#student garde tracker using  all simple data structures 
#calculate students grades for multiple subjects
print("=== Student Grade Tracker===")
#defining variables
Student_ID = int(input("Enter Student ID:"))
Student_Name = input("Enter a student name:")

#by using loops
#if they are true
while True:
    Attendance_status = float(input("Enter Attendance percentage(%):"))
    if Attendance_status <= 0 or Attendance_status <= 100:
        break
    print("WARNING: Attendance must be between 0 and 100.")
Total_score = 0
Number_of_Subjects = 0

#calculate subject inputs
while True:
    #here we increment by 1 
    Total_score = float((input(f"Enter your score for your subject{Number_of_Subjects + 1}:")))
    if Total_score < 0 or Total_score > 100:
        print("WARNING: score must be between 0 and 100.")
        continue
    Total_score += Total_score
    Number_of_Subjects += 1

    #here accept yes or no:
    continuation = input("Do you want to enter another score?(yes/no):")
    if continuation != "yes" :
        break

#calculate average score
if Number_of_Subjects > 0:
        average_score = Total_score/Number_of_Subjects
else:
        average_score = 0

#using conditional statements
if Total_score >= 95:
    performance = "Excellent"
elif Total_score >= 85:
    performance = "Good"
elif Total_score >= 75:
    performance = "Average"
elif Total_score >= 50:
    performance = "Needs Improvement"
else:
    print("FAIL")

# warnings for attendanec using conditional statements:
if Attendance_status < 75:
    print("WARNING: Low Attendance") 
else:
    print("OK: Attendance Satisfied") 

#final results
print("=== Student Grade Tracker===")
print(f"Student ID:{Student_ID}")
print(f"Student Name:{Student_Name}")
print(f"Attendance:{Attendance_status}")
print(f"Total Subjects:{Number_of_Subjects}")
print(f"Total Score:{Total_score}")
print(f"Average Score:{average_score}")
print(f"Performance:{performance}")
