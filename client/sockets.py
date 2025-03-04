import socket

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
