print ("Welcome to the Phone Troubleshooting Program.")
print ("Please answer all questions with a Y or a N.\n")

Q1 = input("QUESTION - Does your phone turn on> ").upper()
if Q1 == "N":
    print ("Advice #1 = Take the phone to a local repair centre.")    
elif Q1 == "Y":
    Q2 = input("QUESTION - Does your phone keep restarting> ").upper()
    if Q2 == "N":
        Q3 = input("QUESTION - Does the battery have trouble keeping charge> ").upper()
        if Q3 == "N":
            Q5 = input("QUESTION - Is there a problem with Internet access> ").upper()
            if Q5 == "N":
                Q6 = input("QUESTION - Is there a problem with the screen?").upper()
                if Q6 == "N":
                    Q8 = input("QUESTION - Is there a problem with the sound> ").upper()
                    if Q8 == "N":
                        print ("ADVICE #9 = Please contact advanced support on 123.")
                    elif Q8 == "Y":
                        print ("ADVICE #8 = You may have the mute button on.")
                    else:
                        print ("An error has occured. Program closing...")
                        exit()
                elif Q6 == "Y":
                    Q9 = input("QUESTION - Is the screen cracked> ").upper()
                    if Q9 == "N":
                        Q10 = input("QUESTION - Is the camera broken> ").upper()
                        if Q10 == "N":
                            print ("ADVICE #9 = Please contact advanced support on 123.")
                        elif Q10 == "Y":
                            print ("ADVICE #10 = Try and adjust the cameras settings.")
                    elif Q9 == "Y":
                        print ("ADVICE #5 = Send the phone to our repair specialists.")
                    else:
                        print ("An error has occured. Program closing...")
                        exit()
            elif Q5 == "Y":
                Q7 = input("QUESTION - Is the Wi-Fi or the 3G/4G enabled> ").upper()
                if Q7 == "N":
                    print ("ADVICE #4 = Turn on your phones Wi-fi or 3G/4G.")
                elif Q7 == "Y":
                    print ("ADVICE #6 = You may have gone over your data allowance.")
                else:
                    print ("An error has occured. Program closing...")
                    exit()
        elif Q3 == "Y":
            print ("Advice #3 = Replace the phones battery.")
        else:
            print ("An error has occured. Program closing...")
            exit()
    elif Q2 == "Y":
        Q4 = input("QUESTION - Is the phone charged up> ").upper()
        if Q4 == "N":
            print ("Advice #2 = Charge the phones battery.")
        elif Q4 == "Y":
            print ("Advice #7 = You may have a faulty power button.")
        else:
            print ("An error has occured. Program closing...")
            exit()
    else:
        print ("An error has occured. Program closing...")
        exit()
else:
    print ("An error has occured. Program closing...")
    exit()
