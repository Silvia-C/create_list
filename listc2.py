List = []


def add_item():
    item = input("Please enter an item: ")
    List.append(item)
    return List

def stay_choice():
    yn = input("Do you wish to save item and continue?")
    while yn == "Y" or yn == "y":
        add_item()
        yn = input("Do you wish to save item and continue?")
    if yn == "N" or yn == "n":
            print("We saved your list")
            return List
    else:
        print("You can only enter Y or N")
        stay_choice()

add_item()
stay_choice()

print(List)
