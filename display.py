def display_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)


if __name__ == "__main__":
    file_path = "story.txt"
    display_file(file_path)
