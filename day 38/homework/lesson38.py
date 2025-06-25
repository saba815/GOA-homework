'''ფუნქცია პროგრამირებაში არის კოდის ბლოკი, რომელსაც აქვს სახელი და ასრულებს კონკრეტულ მოქმედებას.'''
'''არგუმენტი არის ის მონაცემი, რომელსაც ვუგზავნით ფუნქციას.
ფუნქციას არგუმენტები ეხმარება, რომ იმუშაოს სხვადასხვა მონაცემზე.'''

'''ფუნქციის გამოძახება ხდება მისი სახელის დაწერით და ფრჩხილებში არგუმენტების გადაცემით (თუ საჭიროა).'''

'''ფუნქცია გამოიყენება:

ერთი და იგივე კოდის თავიდან არაერთხელ გამოყენებისთვის'''

print("გამარჯობა")              # ტექსტის დაბეჭდვა
print(5 + 3)                   # გამოთვლილი შედეგის დაბეჭდვა
print("2 + 2 =", 2 + 2)        # ტექსტთან ერთად შედეგი
print("GOA" * 3)               # ტექსტის გამრავლება
print("Hello", "World")       # რამდენიმე ელემენტის ერთად დაბეჭდვა



name = input("შენი სახელი: ")          # ითხოვს სახელს
print("გამარჯობა", name)

age = input("რამდენი წლის ხარ? ")     # ითხოვს ასაკს
print("შენი ასაკია:", age)

city = input("სად ცხოვრობ? ")
print("შენ ცხოვრობ", city)

color = input("შენი საყვარელი ფერი? ")
print("მეც მომწონს", color)

food = input("საყვარელი საჭმელი: ")
print(food, "გემრიელია!")



print(type("hello"))         # <class 'str'>
print(type(123))             # <class 'int'>
print(type(3.14))            # <class 'float'>
print(type(True))            # <class 'bool'>
x = input("რაიმე ჩაწერე: ")
print(type(x))               # ყოველთვის იქნება str, რადგან input აბრუნებს string-ს




number = int("5")            # ტექსტი -> რიცხვად
print(number + 1)            # 6

age = int(input("ასაკი: "))  # input-დან მიღებული რიცხვი
print(age + 5)

print(int(3.9))              # float -> int (3)

print(int(True))             # True -> 1

print(int(False))            # False -> 0



num = 5
print("რიცხვი არის " + str(num))   # int -> string

age = 18
text = "შენი ასაკია " + str(age)
print(text)

print(str(3.14))                   # float -> string

print(str(True))                  # boolean -> string

print(str(100 + 200))             # შედეგი -> string



x = float("5.7")       # ტექსტი -> float
print(x + 1)           # 6.7

y = float(10)          # int -> float
print(y)               # 10.0

print(float(True))     # True -> 1.0

print(float(False))    # False -> 0.0

z = float(input("ჩაწერე რიცხვი: "))  # მომხმარებლის შეტანა


print(z * 2)

for i in range(5):        # 0-დან 4-მდე
    print(i)

for i in range(1, 6):     # 1-დან 5-მდე
    print(i)

for i in range(0, 10, 2): # ყოველ მეორე რიცხვს
    print(i)

numbers = list(range(3))  # [0, 1, 2]
print(numbers)

print(sum(range(1, 11)))  # 1 + 2 + ... + 10 = 55


# ვთხოვთ მომხმარებელს ორი რიცხვის შეყვანას
start = int(input("შეიყვანეთ საწყისი რიცხვი: "))
end = int(input("შეიყვანეთ საბოლოო რიცხვი: "))

# ვამოწმებთ სწორია თუ არა შუალედი
if end < start:
    print("არასწორი შუალედი")
else:
    total = 0
    print("რიცხვები მოცემულ შუალედში:")
    for i in range(start, end + 1):
        print(i)
        total += i
    print("რიცხვების ჯამი:", total)



    # ხილის სია (კალათა)
basket = ["ვაშლი", "ბანანი", "ფორთოხალი", "ატამი", "საზამთრო"]

# მომხმარებელს შემოატანინეთ თავისი საყვარელი ხილი
favorite_fruit = input("შეიყვანე შენი საყვარელი ხილი: ")

# ცვლადი, რომელიც ამოწმებს არის თუ არა ხილი კალათაში
fruit_in_basket = False

# ვამოწმებთ ყველა ხილს კალათაში
for fruit in basket:
    if fruit == favorite_fruit:
        fruit_in_basket = True 
        break

# საბოლოო შედეგის ჩვენება
if fruit_in_basket:
    print("Good choice")
else:
    print("fruit  not in basket")







