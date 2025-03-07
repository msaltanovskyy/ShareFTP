import os
from datetime import datetime
from sockets import create_socket
from interface.IFile import IFile
from typing import List, Optional


class FileHandler(IFile):

    def select_and_verify_dir(self) -> str:
        while True:
            dir_path = input("Select directory (example: '/home/'): ").strip()
            if not dir_path:
                print("Path cannot be empty.")
                continue

            dir_path = os.path.abspath(dir_path)

            if os.path.exists(dir_path):
                if os.access(dir_path, os.R_OK):
                    print(f"Selected directory: {dir_path}")
                    return dir_path
                else:
                    print("No permission to access this directory.")
            else:
                create_dir = input("Directory does not exist. Create it? (y/n): ").strip().lower()
                if create_dir == 'y':
                    try:
                        os.makedirs(dir_path)
                        print(f"Directory created: {dir_path}")
                        return dir_path
                    except Exception as e:
                        print(f"Error creating directory: {e}")
                else:
                    print("Please choose an existing directory.")

    def get_files_list(self, files: List[str], dir_path: str) -> None:
        print(f"\nAvailable files: {len(files)}\n")
        print("{:<10} {:<30} {:<15} {:<20}".format("file_id", "name", "permissions", "date"))
        for file in files:
            full_path = os.path.join(dir_path, file)
            file_stats = os.stat(full_path)
            file_id = file_stats.st_ino
            file_date = datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            file_permissions = oct(file_stats.st_mode)[-3:]
            print("{:<10} {:<30} {:<15} {:<20}".format(file_id, file, file_permissions, file_date))

    def select_files(self, dir_path: str) -> List[str]:
        files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        if not files:
            print("No files in the directory.")
            return []

        self.get_files_list(files, dir_path)

        file_names = input("\nEnter file names to send (separated by commas): ").strip().split(',')
        file_names = [name.strip() for name in file_names if name.strip()]

        selected_files = []
        for file_name in file_names:
            if file_name in files:
                selected_files.append(os.path.join(dir_path, file_name))
            else:
                print(f"File '{file_name}' not found in the directory.")

        return selected_files

    def send_files(self, address, files: List[str]) -> None:
        quantity = len(files)
        address.sendall(str(quantity).encode())

        for file_path in files:
            file_name = os.path.basename(file_path)
            address.send(file_name.encode())

            with open(file_path, "rb") as f:
                print(f"Sending file {file_name}...")
                while (data := f.read(1024)):
                    address.sendall(data)
                print(f"File {file_name} sent successfully.")

    def file_send(self, chose_func) -> None:
        address = create_socket()
        if not address:
            print("Failed to create socket.")
            return

        try:
            dir_path = self.select_and_verify_dir()
            selected_files = self.select_files(dir_path)

            if not selected_files:
                print("No valid files selected. Aborting.")
                return

            self.send_files(address, selected_files)

        except Exception as e:
            print(f"Error during file sending: {e}")

        finally:
            chose = input("Continue further (C) or close (Q)?: ").strip().lower()
            if chose == 'c':
                chose_func()
            else:
                address.close()
