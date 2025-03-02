import socket
import os

def create_socket():
    s = socket.socket()  

    port_input = input("Enter port to bind (default 8080): ")
    port = int(port_input) if port_input else 8080

    ip_input = input("Enter IP to bind (default localhost): ")
    ip = ip_input if ip_input else "localhost"

    s.bind((ip, port))
    print("Server started on {}:{}".format(ip, port))
    s.listen(5)

    while True:
        try:
            c, addr = s.accept()
            print("Client connected ip:<" + str(addr) + ">")
            c.send(b"Hello, welcome to the server")

            # Получаем имя файла
            file_name = c.recv(1024).decode()
            print(f"Receiving file: {file_name}")

            with open(file_name, "wb") as f:
                print("Receiving file...")
                while True:
                    data = c.recv(1024)
                    if not data:
                        break
                    f.write(data)

            print("File received successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            c.close() 

if __name__ == '__main__':
    create_socket()
