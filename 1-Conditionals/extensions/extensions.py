def main():
    file = input("What file do you have? ")
    file = file.lower().strip(" ")
    if file.endswith(".jpg"):
        print("image/jpeg")
    elif file.endswith(".pdf"):
        print("application.pdf")
    elif file.endswith(".gif"):
        print("gif/gif")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".txt"):
        print("text/txt")
    elif file.endswith(".zip"):
        print("file/zip")
    elif file.endswith(".jpeg"):
        print("image.jpeg")
    else:
        print("application/octet-stream")


main()
