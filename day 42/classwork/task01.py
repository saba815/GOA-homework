# საყვარელი სპორტსმენების სია
athletes = ["Lionel Messi", "Sergio Ramos", "Wilt Chamberlain"]

# 1) append - ამატებს ელემენტს სიას ბოლოში
athletes.append("Michael Jordan")  # სიაში ემატება მაიკლ ჯორდანი ბოლოში
athletes.append("White Lenon")
athletes.append("Cristiano Ronaldo")

print("append-ის შემდეგ:", athletes)

# 2) insert - აღნიშნულ პოზიციაზე ამატებს ელემენტს, სხვა ელემენტები გადაადგილდება
athletes.insert(1, "Sonia Gomes")  # 1-ელ ინდექსზე ემატება სონია გომესი
athletes.insert(0, "LeBron James") # 0-ელ პოზიციაზე ემატება ლებრონ ჯეიმსი
athletes.insert(3, "Cindy Crawford") # 3-ელ პოზიციაზე ემატება სინდი კროუფორდი

print("insert-ის შემდეგ:", athletes)

# 3) pop - ამოღებს და აბრუნებს ელემენტს, თუ ინდექსი არაა მითითებული, წაშლის ბოლო ელემენტს
removed1 = athletes.pop()      # წაშლის და დააბრუნებს ბოლო ელემენტს
removed2 = athletes.pop(2)     # წაშლის და დააბრუნებს 2-ელ ინდექსის ელემენტს
removed3 = athletes.pop(4)     # წაშლის და დააბრუნებს 4-ელ ინდექსის ელემენტს

print("pop-ის შემდეგ:", athletes)


