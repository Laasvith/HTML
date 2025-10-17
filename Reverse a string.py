String = input("Please enter your own string")

String2 = ('')
#loop for  printing in reverse
for i in String:
    String2 = i + String2
    
print("\nThe Original String = ", String)
print("The reversed String = ", String2)