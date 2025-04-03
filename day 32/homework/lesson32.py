fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]
print(fruits[2])  

numbers = [10, 20, 30, 40, 50]
numbers[1] = 25  
print(numbers)  

colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]

index = int(input("შეიყვანეთ ინდექსი (0-დან 4-მდე): "))

if 0 <= index <= 4:
    print("არჩეული ფერი:", colors[index])
else:
    print("შეყვანილი ინდექსი არასწორია!")

    animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]
animals[-1] = "გემი"  
print(animals)  


colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]

index = int(input("შეიყვანეთ ინდექსი (0-დან 3-მდე): "))
new_color = input("შეიყვანეთ ახალი ფერი: ")

if 0 <= index <= 3:
    colors[index] = new_color  
    print("განახლებული სია:", colors)
else:
    print("შეყვანილი ინდექსი არასწორია!")
