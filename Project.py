# -*- coding: utf-8 -*-
"""
***** STUDENT MANAGEMENT SYSTEM *****

"""
import sys

lessons = ["A", "B", "C", "D", "E"]
list0 = []
student = "Serkan Toraman"

i = 0

while i<3:
    
    name = input("Name Surname: ")
    
    if name == student:
        print(f'\n Welcome {name}\n')
        break
    else:
        i=i+1
        print("Failed.")
    if i==3:
        print("Please try again later...")
        sys.exit()

print("Lessons: ", lessons)

#Choose your lessons!!!

x = 0

while x<5:
    L = input("Choose your lesson: ")
    L=L.upper()
    if L in lessons:
        list0.append(L)
        x=x+1
    elif L == "Q":
        
        if len(list0)<3:
            print(list0, "\nYou failed in class")
            sys.exit()
        
    else:
        print("Wrong choice, choose true one")
        
    if x<len(list0):
        print(list0, "You failed in class!!!")
        
    elif x>=len(list0):
        print(list0)


sL = input("Select Your Lesson: ")

sL = sL.upper()

print( "\n", sL, "\n")

if sL in list0:
    
    grades = {"Midterm":45, "Final":70, "Project":80}
    
    Total_Grade = (grades["Midterm"]*0.30 + grades["Final"]*0.50 + grades["Project"]*0.20)

    if Total_Grade >= 90:
        print("Total Grade: ",Total_Grade, "AA")

    elif Total_Grade>=70 and Total_Grade<90:
        print("Total Grade:",Total_Grade, "BB")
    
    elif Total_Grade>=50 and Total_Grade<70:
        print("Total Grade:",Total_Grade, "CC")
    
    elif Total_Grade>=30 and Total_Grade<50:
        print("Total Grade:",Total_Grade, "DD")
    
    elif Total_Grade<30:
        print("Total Grade:",Total_Grade, "FF", "\nFailed!!!")
        
else:
    print("Wrong choice, choose true one")
        
    








