'''Rob-roy Baetge'''
def main():
    name = str(input("Please enter your name"))
    while name == "":
        print("Invalid name")
        name = str(input("Please enter your name"))
    for letter in range(1, len(name), 2 ):
        print("{}".format(name[letter]))

main()