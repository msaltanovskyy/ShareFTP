import socket
import os
from datetime import datetime

# create client socket

def create_socket():
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

#find file for send

def file_find():
    
    file_path = "/home/makson"  # Example path to save documents for sending to server
     
    try:
        
        files = os.listdir(file_path)
        
        get_files_list(files,file_path)

        #uantity_files = input("Quentity files: ")
        
        #for quntity_files in i: 
            #  # File name
            #arr_files = []
            #arr_files.append[i]

        file_name = input("Input file name: ")
        
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

#file send 

def file_send():
    address = create_socket()
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



def get_files_list(files,file_path):
        print(f"Available quantity: {len(files)}")
        print(f"Available files: \n")  # List of files
        print("{:<10} {:<30} {:<15} {:<20}".format("file_id", "name", "permissions", "date"))
        for file in files:
            file_stats = os.stat(os.path.join(file_path, file))
            file_id = file_stats.st_ino
            file_date = datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            file_permissions = oct(file_stats.st_mode)[-3:]
            print("{:<10} {:<30} {:<15} {:<20}".format(file_id, file, file_permissions, file_date))

#menu chose function 

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
