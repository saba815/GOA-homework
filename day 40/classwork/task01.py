name = "SABA"
new_name = ""

for letter in name:
    if letter == "A":
        new_name += "a"
    elif letter == "B":
        new_name += "b"
    elif letter == "S":
        new_name += "s"
    else:
        new_name += letter  

print("პატარა ასოებით (for ციკლით):", new_name)

name = "SABA"
new_name = name.lower()

print("პატარა ასოებით (lower მეთოდით):", new_name)


