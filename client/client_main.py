from files_send import FileHandler

def chose_func():
    options = input("Choose function (1-send, 2-not): ")
    match options:
        case "1":
            handler = FileHandler()
            handler.file_send(chose_func)
        case "2":
            print("Additonal func")
            chose_func()
        case _:
            print("Choose a valid function!")
            chose_func()

if __name__ == "__main__":
    chose_func()  # Choose function
