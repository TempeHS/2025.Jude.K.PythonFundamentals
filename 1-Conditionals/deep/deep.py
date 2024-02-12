meaning = input("What is The Meaning To Life The Universe and Everything? ")

match meaning.lower():
    case "42" | "forty-two" | "fortytwo":
        print("Yes")
    case _:
        print("No")
