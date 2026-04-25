question = input("Would you like to travel (yes/no)? ").lower()

if question == "yes":
    options = (input("\nSee the options:"
        "\n1: break city\n2: beach front\n3: camping"
                "\nWhich type of travel do you prefer? "))
    if options == '1' and question == "Yes":
        print("You are going to have an excited holiday!")
    elif options == '2':
        print("You are going to habe a relaxed holiday!")
    elif options == '3':
        print("You are going to have a calm holiday!")
    else:
        print("Enter one valid option!")

if question == "no":
    options = (input("\nSee the options:"
                     "\n1: stay home\n2: stay working\n3: planning future travel"
                     "\nWhich option is suitable for you? "))

    if options == '1' or options == '2':
        print("I hope you can planning your next travel soon.")

    # NOT example
    elif not options == '3':
        print("I hope you take some time to travel in the future.")
    else:
        print("I hope you already have some ideas for your next holiday.")

else:
    print("Please answer Yes or No.")
