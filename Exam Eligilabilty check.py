medical_cause=input("did you have a medical cause Y or N")
#Take the user input predicting output accordingly
if medical_cause == 'Y': #checking the condition 1
    print ("You are allowed")
else:
    if atten>=75: #checking the condition 2
        print ("ALlowed")
else:
    print("Not allowed")