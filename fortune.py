# project title : personality based fortune telling system 
# group members : samiksha shrestha and bina maya ghale

users = []
#take test -> asks questions
def take_test():
    name = input("\nEnter your name: ").strip().lower()

    #scores
    scores = {
        "caring" : 0, "social" : 0, "adventurous" : 0
    }

    #questions -> dictionary of lists
    questions = {
        "caring" : [
            "Do you notice when someone in the room is feeling left out?",
            "Would you alter your plans to support a friend going through a tough time?"
        ],
        "social" : [
            "Are you usually the one to start a conversation in a group?",
            "Do you feel energized after spending an evening at a crowded event?"
        ],
        "adventurous" : [
            "Would you go on a spontaneous road trip with zero planning?",
            "Do you actively look for thrilling activities like extreme sports or amusement parks?"
        ]
    }

    print("\nQUESTIONS (Enter y/Y for yes and n/N for no)")

    for trait in questions:
        for question in questions[trait] :

            while True:
                answer = input(f"\n{question} (y/n): ").strip().lower()
                if answer == 'y':
                    scores[trait] += 1
                    break
                elif answer == 'n':
                    break
                else:
                    print("\nInvalid input! Please enter only 'y' or 'n'.\n")

    # Get personality type and fortune message based on final scores
    personality, fortune = get_result(scores)

    # Store all user data in a dictionary and return it
    return {"name" : name, "score" : scores, "personality": personality, "fortune": fortune }

#decide personality and fortune
def get_result(scores):
    if scores["caring"] > scores["social"] and scores["caring"] > scores["adventurous"] :
        return "Caring" , "Your kindnes will bring stronger relationships."
    
    elif scores["social"] > scores["caring"] and scores["social"] > scores["adventurous"] :
        return "Social" , "New connections are coming your way."
    
    elif scores["adventurous"] > scores["caring"] and scores["adventurous"] > scores["social"] :
        return "Adventurous" , "Exciting experiences are ahead."
    
    else : 
        return "Balanced", "You have a well balanced personality."
    
#view result -> current test result
def view_result(user):
    print("\n--------RESULT--------")
    print("Name: ", user["name"])
    print("Personality: ", user["personality"])
    print("Fortune: ", user["fortune"])

    print("Scores")
    print("Caring: ", user["score"]["caring"])
    print("Social: ", user["score"]["social"])
    print("Adventurous: ", user["score"]["adventurous"])
  
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
        user = take_test()
        users.append(user)

    elif choice == 2:
        view_result(users[-1])

    elif choice == 3:
        search_result()

    elif choice == 4:
        delete_result()

    elif choice == 5:
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice!")

        

