# project title : personality based fortune telling system 
# group members : samiksha shrestha and bina maya ghale

#take test -> asks questions
# def take_test():

#view result
# def view_result():


#search result
# def search_result():


#delete result
# def delete_result():


#menu
# while True:
while True:
    print("\nWELCOME TO PERSONALITY BASED FORTUNE TELLING SYSTEM")
    print("\n Lets get started !")
    print("\n----- MENU -----")
    print("\n1. Take Test")
    print("\n2. View Result")
    print("\n3. Search Result")
    print("\n4. Delete Result")
    print("\n5. Exit")

    try:
        choice = int(input("\nEnter a number: "))
    except ValueError:
        print("\nInvalid input!")
        continue

    if choice == 1:
        take_test()

    elif choice == 2:
        view_result()

    elif choice == 3:
        search_result()

    elif choice == 4:
        delete_result()

    elif choice == 5:
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice!")

        

