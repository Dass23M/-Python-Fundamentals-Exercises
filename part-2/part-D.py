total_sum = 0

while True:
    number = int(input("Enter a number (-999 to stop): "))  

    if number == -999:  
        break  

    total_sum += number  

print("Sum of the numbers entered:", total_sum)
