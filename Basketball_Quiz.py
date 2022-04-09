print("Welcome to the ultimate quiz!")
playing = input("Do you want to play? ")
print(playing)
if playing.lower() != 'yes':
    quit()
print("Lets play!")
score = 0
answer = input("What year was basketball made? ")
if answer == '1891':
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many total players can be on the court? ")
if answer == '10':
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the all time leader in total points? ")
if answer.lower() == "lebron james":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the all time leader in 3pt field goals made? ")
if answer.lower() == "stephen curry":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")