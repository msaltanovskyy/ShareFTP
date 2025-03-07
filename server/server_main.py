import socket


def create_socket():
    s = socket.socket()

    port_input = input("Enter port to bind (default 8080): ")
    port = int(port_input) if port_input else 8080

    ip_input = input("Enter IP to bind (default localhost): ")
    ip = ip_input if ip_input else "localhost"

    s.bind((ip, port))
    print(f"Server started on {ip}:{port}")
    s.listen(5)

    while True:
        connect_client(s)


def connect_client(s):
    try:
        c, addr = s.accept()
        print(f"Client connected ip:<{addr}>")
        c.send(b"Hello, welcome to the server")

        # Получаем количество файлов
        quantity_data = c.recv(1024).decode()
        try:
            quantity = int(quantity_data)
            print(f"Receiving {quantity} file(s)...")
        except ValueError:
            print(f"Invalid quantity received: {quantity_data}")
            c.close()
            return

        for i in range(quantity):
            # Принимаем имя файла
            file_name = c.recv(1024).decode()
            if not file_name:
                print(f"File name missing for file {i + 1}")
                break

            print(f"Receiving file {i + 1} of {quantity}: {file_name}")

            with open(file_name, "wb") as f:
                while True:
                    data = c.recv(1024)
                    if not data:
                        break
                    f.write(data)

            print(f"File {file_name} received successfully.")

        print("All files received.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        c.close()


if __name__ == '__main__':
    create_socket()
