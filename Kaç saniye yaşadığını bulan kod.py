from datetime import *
birth = datetime.strptime(input("Your birth date (d.m.Y): "), "%d.%m.%Y")
age = datetime.now() - birth

print("You Survived {} seconds.".format(age.total_seconds()))
