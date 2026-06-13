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
    print("1. Take Test")
    print("2. View Result")
    print("3. Search Result")
    print("4. Delete Result")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        take_test()

    elif choice == "2":
        view_result()

    elif choice == "3":
        search_result()

    elif choice == "4":
        delete_result()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

        

