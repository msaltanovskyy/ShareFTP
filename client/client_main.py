import socket
import os
from file import file_send

def chose_func():
    options = input("Choose function (1-send, 2-not): ")
    match options:
        case "1":
            file_send()
        case "2":
            print("Additonal func")
            chose_func()
        case _:
            print("Choose a valid function!")
            chose_func()

if __name__ == "__main__":
    chose_func()  # Choose function
