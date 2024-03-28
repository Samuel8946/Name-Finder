def main():
    userInput = input("Search Name Here: ")
    lockers = ["Samuel", "Yoshi", "Dogs", "Cats", 'C', "Scarborough", "samuel", "sAmuEl"]
    lockers = [locker.lower() for locker in lockers]

    print(lockers)

    number_of_samuel = 0
    
    for i in lockers:
        if i == userInput:
            number_of_samuel += 1

    print(f"There are {number_of_samuel} '{userInput}' in this list")


main()


# Will update this so you can input a file and you can search for certaint in the file

