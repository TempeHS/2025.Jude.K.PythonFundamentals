def main():
    print(
        f"What would you pick? ",
        "Option.1",
        "Option.2",
        "Option.3",
        "Option.4",
        sep="\n",
    )
    while True:
        User_input = input("")
        if User_input.startswith("1"):
            print("Thank You For Choosing 1")
        elif User_input.startswith("2"):
            print("Thank Your For Choosing 2")
        elif User_input.startswith("3"):
            print("Thank you for choosing 3")
        elif User_input.startswith("4"):
            print("Thank You")
            break


main()
