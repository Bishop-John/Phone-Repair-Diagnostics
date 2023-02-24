print ("Welcome to the Phone Troubleshooting Program. \nPlease answer all questions with a Y or a N.")
print ("If a question doesnt apply to you then press enter to skip it.\n")

userAnswers = []

Q1 = input("QUESTION 1 - Does your phone turn on> ").upper()
Q2 = input("QUESTION 2 - Does your phone keep restarting> ").upper()
Q3 = input("QUESTION 3 - Does the battery have trouble keeping charge> ").upper()
Q4 = input("QUESTION 4 - Is the phone charged up> ").upper()
Q5 = input("QUESTION 5 - Is there a problem with Internet access> ").upper()
Q6 = input("QUESTION 6 - Is there a problem with the screen?").upper()
Q7 = input("QUESTION 7 - Is the Wi-Fi or the 3G/4G enabled> ").upper()
Q8 = input("QUESTION 8 - Is there a problem with the sound> ").upper()
Q9 = input("QUESTION 9 - Is the screen cracked> ").upper()
Q10 = input("QUESTION 10- Is the camera broken> ").upper()
userAnswers.extend([Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10])

userAnswers="".join(userAnswers)
   
print ("You have answered: ", userAnswers)

if userAnswers == "YYNNNNNNNN":
    print ("ADVICE #7 = You may have a faulty power button.")
elif userAnswers == "YYYNNNNNNN":
    print ("ADVICE #2 = Charge the phones battery.")
elif userAnswers == "YNYYNNNNNN":
    print ("ADVICE #3 = Replace the phones battery.")
elif userAnswers == "NNNNNNNNNN":
    print ("ADVICE #1 = Take the phone to a local repair centre.")
elif userAnswers == "YNNYYNYNNN":
    print ("ADVICE #6 = You may have gone over your data allowance.")
elif userAnswers == "YNNYYNNNNN":   
    print ("ADVICE #4 = Turn on your phones Wi-fi or 3G/4G.")
elif userAnswers == "YNNNNYNNYN":
    print ("ADVICE #5 = Send the phone to our repair specialists.")
elif userAnswers == "YNNNNNNYNN":
    print ("ADVICE #8 = You may have the mute button on.")
elif userAnswers == "YNNNNNNNNN":
    print ("ADVICE #9 = Please contact advanced support on 123.")
elif userAnswers == "YNNNYNYNNN":
    print ("ADVICE #10 = Try and adjust the cameras settings.")
else:
    print ("Your answers do not match any diagnostic pattern. Please exit and try again. ")
