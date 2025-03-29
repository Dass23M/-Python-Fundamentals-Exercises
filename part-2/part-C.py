student = 1

while student <= 5:
  mark = int (input("Enter the student of marks :"))
  student = student + 1
  if (mark > 75  ):
    print("A")
  elif (mark > 65):
   print("B")
  elif(mark >55):
    print("C")
  elif(mark > 45):
    print("S")
  else: 
    print("F")