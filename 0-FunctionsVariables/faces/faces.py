def main():
    convert()


def convert():
    new = face.replace(":)", "😊").replace(":(", "😔")
    print(new)


face = input("Write a happy of sad face for an emoji!")
main()
