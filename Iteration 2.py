from doctest import OutputChecker


print("Welcome to Yahia's Driving Quiz!")
points = 0
Start = input(print("Would you like to start? Yes/No "))

#Starting the code 
if Start == "Yes":
    print(Questions[0])
answer1 = input("answer: ")
if Start == "No":
    print("Then Dont")

#Questions list


Questions = ['Question 1: On what side of the road do you drive in? Option 1: The left side,    Option 2:The right side, Option 3: It doesnt matter.',]
print("""
      
      To answer, Type either '1', '2', '3' 
      
      """)
Q2 = ("""Question 2: What is the usual speed for a highway?
      Option 1: 80 kmp/h,
      Option 2: 50 kmp/h
      Option 3: 100 kmp/h""")

Q3 = ("""Question 3: What is the average driving speed in a school zone?""")
Q4 = ("""Question 4: """)
Q5 = ("""Question 5: """)
Q6 = ("""Question 6: """)
Q7 = ("Question 7: ")
Q8 = ("Question 8: ")
Q9 = ("Question 9: ")
Q10 = ("Question 10: ")

if Start == "Yes":
    print(Questions[0])
answer1 = input("answer: ")
if Start == "No":
    print("Then Dont")
    
print("You have your options, choose wisely")
    
if answer1 == "1":
    print("Correct, + 1 point")
points += 1
print(points)
print('/10')

Question_2 = print(Questions[1])
answer2 = input("answer: ")
if answer2 == "3":
     print("Correct, + 1 point")
     points += 1
print(points)