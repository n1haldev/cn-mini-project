# cn-mini-project
This is a mini-project based on Socket Programming in Python for the subject Computer Networks. 

The code produces a user-friendly interface where two players on different systems connected via the same network can play this unique game called SPY GRID.

In this game the players have to choose two spying positions out of 8 allotted to each out of the total 16 spy spots. Then the users go ahead and guess the
opponents spy spot and the user who guesses both of the spy spots of the opposition correctly first wins the game.

The game was made possible with the tkinter library for the interface and socket programming library for message passing between the two systems.
We use a client-server architecture but the server is a rendezvous server i.e it is a server that connects two clients by sending their IPs to one another.
After the two clients have the IP address and port number of the other, they can pass messages to each other using UDP using a technique called
UDP punch hole.

The management of data is done on both the client systems thus leaving the server free to accept more requests from clients that want to play.

This project was accomplished with team partners @arorapallavi and @niveditha-17

How to play this on your system?

1. git clone the repo on three systems that run on the SAME NETWORK.
2. One system will have to be server and the other two client.
3. run the server code on the server machine using the command: python server_udp.py
4. run the client code on the client machines using the command: python gui_client.py
5. ENJOY!!!