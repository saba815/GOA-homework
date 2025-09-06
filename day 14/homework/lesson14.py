
for i in range(10):  
    print("saba Sesitashvili")


for i in range(1, 21):
    print(i)


for i in range(20, -1, -1):
    print(i)

    
num = 10
while num <= 15:
    print(num)
    num += 1


num = 50
while num >= 0:
    print(num)
    num -= 1

# 3) Counter ცვლადი
# Counter ცვლადი არის ისეთი ცვლადი, რომელიც გამოიყენება
# While Loop-ში იმისთვის, რომ ვიცოდეთ რამდენჯერ იმუშავოს ციკლმა.
# მაგალითად, ციკლი გაგრძელდება მანამ, სანამ counter არ მიაღწევს
# წინასწარ განსაზღვრულ მნიშვნელობას.


num = 10
while num <= 70:
    if num % 2 == 0:
        print(num)
    num += 1


num = 25
while num <= 55:
    if num % 2 != 0:
        print(num)
    num += 1
