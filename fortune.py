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
    caring = scores["caring"]
    social = scores["social"]
    adventurous = scores["adventurous"]

    max_score = max(caring, social, adventurous)

    # count how many have max score
    count = 0
    if caring == max_score:
        count += 1
    if social == max_score:
        count += 1
    if adventurous == max_score:
        count += 1
    
    # if all equal
    if count == 3:
        return "Balanced", "You have a perfectly balanced personality."

    # tie between two traits
    if count > 1:
        return "Mixed", "You have a combination of personalities."

    # single winner cases
    if caring == max_score:
        return "Caring", "Your kindness will bring strong relationships."
    elif social == max_score:
        return "Social", "New connections are coming your way."
    else:
        return "Adventurous", "Exciting experiences are ahead."
    
#view result 
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
def search_result(users):
    if len(users) == 0:
       print("\nNo data found.")
       return
    
    name = input("\nEnter the name to search: ").strip().lower()
    
    found = []
    for user in users :
        if user["name"] == name:
            found.append(user)
    
    if len(found) == 0:
        print("\nNo data found.")
        return
    
    for user in found:
        view_result(user)

#delete result
def delete_result(users):
    if len(users) == 0:
        print("\nNo data found.")
        return
    
    name = input("\nEnter the name to delete: ").strip().lower()
    
    found = []
    for user in users :
        if user["name"] == name:
            found.append(user)
    
    if len(found) == 0:
        print("\nNo data found.")
        return
    
    for user in found:
        users.remove(user)
    
    print(f"\nResult for '{name}' has been deleted successfully.")

#menu
def main():
    while True:
        print("\nWELCOME TO PERSONALITY BASED FORTUNE TELLING SYSTEM")
        print("\n Lets get started !")
        print("\n----- MENU -----")
        print("\n1. Take Test")
        print("\n2. View Result")
        print("\n3. View All User Result")
        print("\n4. Search Result")
        print("\n5. Delete Result")
        print("\n6. Exit")

        try:
            choice = int(input("\nEnter a number: "))
        except ValueError:
            print("\nInvalid input!")

        if choice == 1:
            user = take_test()
            users.append(user)

        elif choice == 2:
            if len(users) == 0:
                print("\nNo result available. Please take a test first.")
            else:
                view_result(users[-1])

        elif choice == 3:
            if len(users) == 0:
                print("\nNo users found.")
            else:
                for user in users:
                    view_result(user)

        elif choice == 4:
            search_result(users)

        elif choice == 5:
            delete_result(users)

        elif choice == 6:
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice!")
  
main()
