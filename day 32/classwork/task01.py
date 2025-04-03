# # პირველ სია - Strings სტრინგების სია
# strings_list = ["apple", "banana", "cherry", "date", "elderberry"]

# # მეორე სია - Integers ინტეჯერების სია
# integers_list = [1, 2, 3, 4, 5]

# # მესამე სია - Floats ფლოათების სია
# floats_list = [1.1, 2.2, 3.3, 4.4, 5.5]

# # მეოთხე სია - Booleans ბულიანების სია
# booleans_list = [True, False, True, False, True]

# # დიდი სია,
# big_list = [strings_list] + integers_list + floats_list + booleans_list


"""1) შექმენით 5 სია, პირველ სიაში შეინახეთ strings, მეორე სიაში integers, მესამეში floats, მეოთხეში booleans (თითოეულ სიაში უნდა იყოს 5 ელემენტი) საბოლოოდ კი შექმენით დიდი სია რომელშიც იქნება ყველა ზევით მყოფ სიაში არსებული ელემენტები. აქედან მხოლოდ strings უნდა იყოს ცალკეულ სიად დიდ სიაში, დანარჩენების კი მხოლოდ ელემენტები გადმოიტანეთ"""

strings = ["Luka", "Tornike", "Barbare", "Giorgi", "Tamar", "Saba"]

integers = [1, 2, 3, 4, 5]
floats = [1.2, 2.2, 3.2, 4.2, 5.2]
booleans = [True, True, False, False, True]

data = [
    ["Luka", "Tornike", "Barbare", "Giorgi", "Tamar", "Saba"], 1, 2, 3, 4, 5, 1.2, 2.2, 3.2, 4.2, 5.2,
    True, True, False, False, True
]

print(data)