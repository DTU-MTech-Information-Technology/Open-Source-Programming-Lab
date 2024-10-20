with open("append.txt", "a") as file:
    file.write("Bacon ipsum dolor amet tri-tip cow bacon ribeye chislic alcatra")

with open("append.txt", "r") as file:
    text = file.read()
    print(text)