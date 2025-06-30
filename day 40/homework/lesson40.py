word = input("შეიყვანე სიტყვა: ")
print(word.lower())

word1 = input("შეიყვანე პირველი სიტყვა: ")
word2 = input("შეიყვანე მეორე სიტყვა: ")

print(word1.lower() == word2.lower())


countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

for country in countries:
    print(country.lower())


word = input("შეიყვანეთ სიტყვა: ")
print(word.upper())


countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

for country in countries:
    print(country.upper())


word = input("შეიყვანეთ სიტყვა: ")

is_all_upper = True
for char in word:
    if not ('A' <= char <= 'Z'):
        is_all_upper = False

if is_all_upper:
    print("სიტყვა მთლიანად დიდი ასოებითაა.")
else:
    print("სიტყვა არაა მთლიანად დიდი ასოებით.")

sentence = input("შეიყვანეთ წინადადება: ")
print(sentence.capitalize())


text = "gEoRGia"
result = text.capitalize()
print(result)

countries = ["georgia", "aRMENIA", "greeCE"]

for country in countries:
    print(country.lower().capitalize())

word = input("შეიყვანეთ სიტყვა: ")

position = word.find('a')

if position != -1:
    print("ასო 'a' პირველი პოზიციაზეა: " + str(position))
else:
    print("ასო 'a' სიტყვაში არ არის.")


text = "I visited Georgia, Armenia and Greece"

position = text.find("Armenia")

if position != -1:
    print("Armenia მდებარეობს პოზიციაზე: " + str(position))
else:
    print("Armenia არ არის ტექსტში.")


