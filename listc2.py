List = []


def add_item():
    item = input("Please enter an item: ")
    List.append(item)
    return List

def stay_choice():
    yn = input("Do you wish to save item and continue?")
    while yn == "Y":
        add_item()
        yn = input("Do you wish to save item and continue?")
    if yn == "N":
            print("We saved your list")
            return List

add_item()
stay_choice()

print(List)
