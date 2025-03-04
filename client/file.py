import os
from datetime import datetime
from sockets import create_socket


def chose_dir():
  
    while True:
        file_path = input("Choose directory (example: '/home/'): ").strip()
        if not file_path:
            print("Path cannot be empty.")
            continue

        file_path = os.path.abspath(file_path)

        if os.path.exists(file_path):
            return file_path
        else:
            create_dir = input("Directory does not exist. Create it? (y/n): ").strip().lower()
            if create_dir == 'y':
                try:
                    os.makedirs(file_path)
                    print(f"Directory created: {file_path}")
                    return file_path
                except Exception as e:
                    print(f"Error creating directory: {e}")
                    return False
            else:
                print("Please choose an existing directory.")


def check_correct_dir(file_path):
   
    check_dir = input(f"Is this the correct directory '{file_path}'? (y/n): ").strip().lower()
    if check_dir == 'y':
        return file_path
    else:
        return chose_dir()


def file_find():
    
    try:
        file_path = chose_dir()
        if not file_path:
            return False

        file_path = check_correct_dir(file_path)
        if not file_path:
            return False

        files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
        if not files:
            print("No files in the directory.")
            return False

        get_files_list(files, file_path)

        file_name = input("\nInput file name: ").strip()
        if file_name in files:
            full_file_path = os.path.join(file_path, file_name)
            return full_file_path
        else:
            print("File not found.")
            return False

    except FileNotFoundError:
        print("Directory not found.")
        return False
    except PermissionError:
        print("No permission to access this directory.")
        return False


def file_send():
   
    address = create_socket()
    if not address:
        print("Failed to create socket.")
        return

    try:
        file_path = file_find()
        if not file_path:
            return
        
        file_name = os.path.basename(file_path)
        address.send(file_name.encode())
        
        with open(file_path, "rb") as f:
            print("Sending file...")
            while (data := f.read(1024)):
                address.sendall(data)
            print("File sent successfully.")
    except Exception as e:
        print(f"Error during file sending: {e}")
    finally:
        address.close()


def get_files_list(files, file_path):
    
    print(f"\nAvailable quantity: {len(files)}\n")
    print("{:<10} {:<30} {:<15} {:<20}".format("file_id", "name", "permissions", "date"))
    for file in files:
        full_path = os.path.join(file_path, file)
        file_stats = os.stat(full_path)
        file_id = file_stats.st_ino
        file_date = datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        file_permissions = oct(file_stats.st_mode)[-3:]
        print("{:<10} {:<30} {:<15} {:<20}".format(file_id, file, file_permissions, file_date))
