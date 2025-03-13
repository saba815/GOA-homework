for i in range(20, 41, 2):
    print(i)

    summa = 0  

for i in range(1, 16):  
    summa += i  

print("result:", summa)

umma = 0  
i = 1  

while i <= 15:  
    umma += i  
    i += 1  

print("result:",umma)

num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))


small = min(num1, num2)
large = max(num1, num2)


summa = 0
for i in range(small, large + 1):
    summa += i


print("result:", summa)


password = "saba2301"  


attempts = 0  

while True:
    user_input = input("enter password: ")  
    attempts += 1  
    
    if user_input == password:
        print("Logged in successfully!")
        print("number of tries:", attempts)
        break  
    else:
        print("wrong password pls try again!")

        
