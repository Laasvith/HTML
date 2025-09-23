Amount = int(input("Please enter amount of withdraw: "))
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
print("Notes of 100 dllars", note_1)
print("Notes of 50 dllars", note_2)
print("Notes of 10 dllars", note_3)