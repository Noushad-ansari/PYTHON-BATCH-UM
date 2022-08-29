# age = int(input("Enter your age \n"))

# if age >= 18:
#     print("you elegible to vote")
# else:
#     print("you are not elegible to vote")

# 2nd
# if age >= 18:
#     print("you elegible to vote")

# 3rd
# if True:
#     print("you are true")
# else:
#     print("you are false")

# 4th
# age = 0
# age = 51
# if age:
#     print("you elegible to vote")
# else:
#     print("you are not elegible to vote")

# 5th  if-elif-else for more than one condition
# age = int(input('Enter you age'))

# if age >= 18 and age <= 40:
#     print("you are elegible to go on everest")
# elif age<18:
#     print("sorry champ you need to grow more")
# elif age > 40:
#     print('Sorry sir you are senior citizen you cant go there')



# 6th
subject = input("Enter your subject \n")

if subject == "bio":
    print("you are elegible to become a doctor")
    grade = input("Enter your gade \n")
    if grade == "A" or grade =='a':
        print('you are elegible to become neurologist')
elif subject == 'math':
    print("you are elegiblet to become a engineer")
    rank = int(input("Enter you AIR"))
    if rank <= 500:
        print("you are elegible for CS branch")
    elif rank >= 500 and rank <= 1000:
        print("you Elegible for machanical brnach")
    else:
        print('you can choose any branch except CS and MCH ')
elif subject == "commerce":
    print("you can go for bcom")
else:
    print('you can become anything')
  






# Logic building with if Else

# iceCreamPrice = int(input("How much money do you have?"))

# if iceCreamPrice >= 100:
#     print("you can buy ice Creame")
# else:
#     print("you can not buy please collect more rupees")
