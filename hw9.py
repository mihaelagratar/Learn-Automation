def daddy():
    names = {"adi": ["adrian", "petre"], "mitza": ["mihai", "marian"], "ion": ["ionut", "ionel"]}
    print("What do you want to do?\n")
    choice = input("a: look up father-son pair,\nb: add a pair,\nc: delete a pair,\nd: replace a father-son pair,\ne: look for grandfather\n")
    if choice == 'a':
        name = input("What is the name of the son? ")
        if name in names:
            print(name, "is the child of", names[name][0])
        else:
            print("Sorry,try again")
            daddy()
    elif choice == "b":
        new_son = input("What is the name of the son?")
        if new_son not in names:
            father = input("\nWho's the father?: ")
            names[new_son] = father
            print(new_son, "has been added")
            print(names)
        else:
            print("I already know that name!")
    elif choice == "c":
        aaa = input("Who would you like to delete?: ")
        if aaa in names:
            del names[aaa]
            print("I deleted", aaa)
            print(names)
        else:
            print("Sorry, name does not exist")
    elif choice == "d":
        bbb = input("Which father-son pair do you want to replace?: ")
        if bbb in names:
            father = input("Who is the new father?: ")
            names[bbb] = father
            print(bbb, "has a new father.")
            print(names)
        else:
            print("Sorry, you must enter the name of the son")
    elif choice == "e":
        ccc = input("Who's grandfather are you looking for? ")
        if ccc in names:
            father = names[ccc][1]
            print("\n", ccc, "is grandson of:", father)
        else:
            print("\nSorry, I don't know", ccc)
    else:
        print("Sorry,", choice, "isn't a choice. Please try again.")
    input("\n\nPress the enter key to exit.")
daddy()