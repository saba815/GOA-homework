points = 50        # თავდაპირველი მნიშვნელობა
points = points + 20   # პირველი განახლება
points = points - 10   # მეორე განახლება
print(points)      # საბოლოო მნიშვნელობის დაბეჭდვა



#this is a code that is incorrect
# name = input("რა არის შენი სახელი?)
# print("მოგესალმები", name)
# age = int(input("რამდენი წლის ხარ?"))
# if age > 18
# print("სრულწლოვანი ხარ")
# else
# print("არ ხარ სრულწლოვანი")
# fav_color = inpt("შენი საყვარელი ფერი?")
# print("შენი ფერია", fav_color)


#this is the correct version of this code
name = input("რა არის შენი სახელი?")  # ბრჭყალების დახურვა
print("მოგესალმები", name)
age = int(input("რამდენი წლის ხარ?"))
if age > 18:
    print("სრულწლოვანი ხარ")         # if ბლოკი სწორად ჩამოყალიბებულია
else:
    print("არ ხარ სრულწლოვანი")       # else ბლოკიც სწორად
fav_color = input("შენი საყვარელი ფერი?")  # inpt -> input
print("შენი ფერია", fav_color)
