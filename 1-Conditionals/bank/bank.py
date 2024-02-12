def main():
    response = input("Hello There! ")
    response = response.lower().lstrip(" ")

    if response.startswith("hello"):
        print("$0")
    elif response.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
