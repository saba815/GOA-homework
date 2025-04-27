word = input("შემოიტანეთ სიტყვა: ")

if word == word[::-1]:
    print("ეს განსაკუთრებული სიტყვაა! ")
else:
    print("ეს ჩვეულებრივი სიტყვაა.")





    words = ["სიყვარული", "მზე", "წვიმა", "ხე", "მდინარე", "თოლია"]

index = 0

for word in words:
    if index % 2 == 0:
        print(word)
    else:
        print(word[::-1])
    index += 1

    


word = input("შემოიტანეთ სიტყვა: ")
print(word[::-1])





text = "სწავლა არის გზა წარმატებისკენ, იმოქმედე ახლა!"


print(text)


print(text[:10])


print(text[-10:])


print(text[::2])


print(text[::-1])
