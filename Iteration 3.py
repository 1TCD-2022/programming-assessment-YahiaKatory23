from doctest import OutputChecker


#Introduction/Setup

print("Welcome to Yahia's driving quiz!")

points = 0
Start = print("Would you like to start?  ")
export = input("Yes/No: " )

Yes = "Yes"
No = "No"

	
#Questions

Q = ["Question 1: On what side of the road do you drive on? Option 1: The left side, Option 2: The right side, Option 3: It doesn't matter",
"Question 2: What is the usual speed for a highway?  Option 1: 80 kmp/h ,  Option 2: 50 kmp/h, Option 3: 100 kmp/h", 
"Quetion 3: Where do you keep your left foot when driving? Option 1: On the brakes, Option 2: To the side, Option 3: On the Gas Pedal.",
"Question 4: In which order do you start the car? Op 1: Brakes, Pedal, Gears, Op 2: Gears, Pedal, Brakes, Op 3: Brakes, Gears, Pedal.",
"Question 5: What is the average amount of exits in a traffic circle? Op 1: 3, Op 2: 4, Op 3: 5?",
"Question 6: What do you call the area of road you drive on? Op 1: Lane , Op 2: Pathway, Op 3: Verge.",
"Question 7: When can you park on the right hand side of the road?: Op 1: When you have your park lights on, Op 2: On a one way street, Op 3: In the Countryside.",
"Question 8: What colour are warning signs?: Op 1: Yellow and orange, Op 2: Blue, Op 3: Red.",
"Question 9: How often must you renew a cars fitness warrant?: Op 1: Once every year, Op 2: Every 3 months, Op 3: Every 6 Months.",
"Question 10: How good do you think this quiz was?: Op 1: Great ,Op 2: Amazing ,Op 3: Fantastic."]

#Answers

A = ['1','3','2','3','2','1','2','1','3','3']

#Starting the code 

if export == Yes:
    print("""
      
      To answer, Type either '1', '2', '3'. 
      
      You have your options, choose wisely
      Goal: have more than 5 points
      """)
    print(Q[0])

elif export == No:
    print("Then Dont")
    	
answer1 = input("answer: ")

#Code  function

if answer1 == A[0]:
    print("Correct, + 1 point")
    points += 1
    print(points)
    print('/10')
    print(Q[1])
else:
    print("Better luck next question")
    print(points)
    print('/10')
    print(Q[1])

answer2 = input("answer: ")

if answer2 == A[1]:
    print("Correct, + 1 point")
    points += 1
    print(points)
    print('/10')
    print(Q[2])
else:
    print("Better luck next question")
    print(points)
    print('/10')
    print(Q[2])
  
answer3 = input("answer: ")
	 
if answer3 == A[2]:
    print("Correct, + 1 point")
    points += 1
    print(points)
    print("/10")
    print(Q[3])
else:
    print("Better luck next question")
    print(points)
    print('/10')
    print(Q[3])

answer4 = input("answer: ")
	 
if answer4 == A[3]:
    print("Correct, + 1 point")
    points += 1
    print(points)
    print("/10")
    print(Q[4])
else:
    print("Better luck next question")
    print(points)
    print('/10')
    print(Q[4])

answer5 = input("answer: ")
	 
if answer5 == A[4]:
    print("Correct, + 1 point")
    points += 1
    print(points)
    print("/10")
    print(Q[5])
else:
    print("Better luck next question")
    print(points)
    print('/10')
    print(Q[5])

answer6 = input("answer: ")
	 
if answer6 == A[5]:
    print("Correct, + 1 point")
    points += 1
    print(points)
    print("/10")
    print(Q[6])
else:
    print("Better luck next question")
    print(points)
    print('/10')
    print(Q[6])

answer7 = input("answer: ")
	 
if answer7 == A[6]:
    print("Correct, + 1 point")
    points += 1
    print(points)
    print("/10")
    print(Q[7])
else:
    print("Better luck next question")
    print(points)
    print('/10')
    print(Q[7])

answer8 = input("answer: ")
	 
if answer8 == A[7]:
    print("Correct, + 1 point")
    points += 1
    print(points)
    print("/10")
    print(Q[8])
else:
    print("Better luck next question")
    print(points)
    print('/10')
    print(Q[8])

answer9 = input("answer: ")
	 
if answer9 == A[8]:
    print("Correct, + 1 point")
    points += 1
    print(points)
    print("/10")
    print(Q[9])
else:
    print("Better luck next question")
    print(points)
    print('/10')
    print(Q[9])

answer10 = input("answer: ")
	 
if answer10 == A[9]:
    print("Great")
    points += 1
    print(points)
    print("/10")

else:
    print("Better luck next question")
    print(points)
    print('/10')

if points > 5:
    print("good job, you reached your goal!")
    
if points < 5:
    print("Sorry man, failed this time around, Try again later.")