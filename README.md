# Socket-Programming
This repo is meant for hosting all the client and server codes written with socket programming.
The server and client files are added.
The server is written in python and the client in written in c++.
TO run the client and server just clone the repo and and run the files in your terminals.
For server:-
`run the command : python server.py`
The output will be : 
`Socket created
Socket bind complete
Socket now listening`
The server is waiting for the client.

For client:-
`run the command: g++ client.cpp`
This is done is compile the client and create the excutable a.out.Now 
`run the command: ./a.out`
The output will be:
`Connected
 Enter the file`
 Now enter the file having numbers in each line
 The server will sort the data and return to the client.
 The client will then print the returned data in the terminal.
 After the process is over the server will be ready for next client.
 To stop server press `Ctrl+C`
