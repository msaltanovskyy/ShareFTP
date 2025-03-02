import socket
import os

def create_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port_input = input("Enter port to connect (default 8080): ")
    port = int(port_input) if port_input else 8080

    ip_input = input("Enter IP to connect (default localhost): ")
    ip = ip_input if ip_input else "localhost"

    try:
        s.connect((ip, port))
        print("Connected to the server!")
        return s
    except ConnectionAbortedError:
        print("Connection aborted")
    except ConnectionRefusedError:
        print("Server not started")
    except Exception as e:
        print(f"An error occurred: {e}")

def file_find():
    file_path = "/home/makson"  # Example path to save documents for sending to server
    try:
        files = os.listdir(file_path)
        print("Available files:", files)  # List of files

        file_name = input("Input file name: ")  # File name

        if file_name in files:
            full_file_path = os.path.join(file_path, file_name)  # Full path
            return full_file_path
        else:
            print("File not found")
            return False
    except FileNotFoundError:
        print("Directory not found")
        return False
    except PermissionError:
        print("No permission to access this directory")
        return False

def file_send():
    address = create_connection()
    if address:
        file_path = file_find()
        if file_path:
            with open(file_path, "rb") as f:
                print("Sending file...")
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    address.send(data)
                print("File sent successfully.")
        address.close()  

def file_rec():
    print("Receiving files is handled by the server.")

def chose_func():
    options = input("Choose function (1-send, 2-rec): ")
    match options:
        case "1":
            file_send()
        case "2":
            file_rec()
        case _:
            print("Choose a valid function!")
            chose_func()

if __name__ == "__main__":
    chose_func()  # Choose function
