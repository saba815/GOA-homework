
for i in range(0, 21):
    if i % 2 == 0:
        print(f"{i} even")
    else:
        print(f"{i} odd")
        

i = 0
while i <= 20:
    if i % 2 == 0:
        print(f"{i} even")
    else:
        print(f"{i} odd")
    i += 1


name = input("Enter your name: ")
if name == "saba":
    print("coincidence")
else:
    print("not coincidence ")



    score= int(input("enter your score: "))

    if  (score) > 70:
        print("you have passed")
    else:
     print("you have failed")



     score=(input("enter your score: ")) 
     if score > 80:
         print("you have got A as your grade")

         if score > 60 and score < 80:
             print("you have B as your grade")

             if score > 40 and score < 60:
                 print("you have C as your grade")

                 if score > 20 and score < 40:
                     print("you have D as your grade")
                     
                     if score < 20:
                         print("you have F as your grade")

