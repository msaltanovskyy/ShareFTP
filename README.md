
# File Transfer Server and Client

This project implements a system for file transfer between a client and a server using sockets. The server waits for a connection from the client, accepts the file, and saves it. The client sends a file to the server.

## Installation

1. Ensure that you have Python 3.x installed.
2. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
3. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```

## Running the Server

1. Navigate to the directory where the server file (`server_main.py`) is located.
2. Start the server:
   ```bash
   python3 server_main.py
   ```

The server will begin listening for incoming connections on port 8080 (or another port if specified).

Example output:
```
Server started on localhost:8080
Client connected ip:('<client_ip>', <client_port>)
Receiving file: example.txt
File received successfully.
```

## Running the Client

1. Navigate to the directory where the client file (`file.py`) is located.
2. Start the client:
   ```bash
   python3 file.py
   ```

The client will prompt you for:
- The directory path.
- Confirmation of the selected directory.
- The file name to send.

Example output:
```
Choose directory (example: '/home/'): /home/user/
Is this the correct directory '/home/user/'? (y/n): y
Input file name: example.txt
Sending file...
File sent successfully.
```

## How It Works:

1. **Server**:
   - Listens on port 8080 and waits for a client connection.
   - Upon connection, it receives the file name and data, and saves the file on the server.
   
2. **Client**:
   - Connects to the server.
   - Requests the file name and path to send.
   - Sends the file name and its contents.

## Notes

- The server and client use TCP protocol for data transfer.
- The default listening port is 8080, but it can be changed when starting the server.
- The server saves files in the current directory where the server is started.

## Example Usage:

1. Run the server:
   ```bash
   python3 server_main.py
   ```

2. Run the client:
   ```bash
   python3 file.py
   ```

3. After the client sends the file, it will be saved on the server with the same name as the client provided.

## Future Improvements

- Add a progress bar to display the file transfer status.
- Implement support for transferring multiple files.
- Add logging and error handling features.

## License

This project is licensed under the MIT License.

---

