# SPY GRID : cn-mini-project 
This is a mini-project based on Socket Programming in Python for the subject Computer Networks. 

The code produces a user-friendly interface where two players on different systems connected via the same network can play this unique game called **SPY GRID**.
## How the Game works
In this game the players have to choose two spying positions out of the total 16 spy spots.

Then the users go ahead and guess the opponents spy spot.

The user who guesses both of the spy spots of the opposition correctly first wins the game.

## Technicalities
The game was made possible with the *tkinter* library for the interface and socket programming library for message passing between the two systems.
We use a client-server architecture but the server is a rendezvous server i.e it is a server that connects two clients by sending their IPs to one another.
After the two clients have the IP address and port number of the other, they can pass messages to each other using UDP using a technique called
*UDP punch hole*.

The management of data is done on both the client systems thus leaving the server free to accept more requests from clients that want to play.

## Team
1. <a href="https://github.com/n1haldev/" target="_blank">Nihal TM</a>
2. <a href="https://github.com/arorapallavi" target="_blank">Pallavi Arora</a>
3. <a href="https://github.com/niveditha-17" target="_blank">Niveditha Deepak</a>


## How to play this on your system?

1. git clone the repo on three systems that run on the SAME NETWORK.
2. One system will have to be server and the other two client.
3. In the server machine run the command: ip addr show | awk '/inet /{print $2}' | cut -d/ -f1
4. Copy the ip address (not 127.0.0.1 as this address is loopback) which is output of the above command and paste it onto line 4 replacing existing address in the UDP_IP_ADDRESS = '{to paste what you copied!}'
(IP address in the second line, 192.168.0.106 here)

   ![image](https://user-images.githubusercontent.com/97780641/228596684-caaaa40c-f76d-4264-b752-622446b10c13.png)

5. Run the server code on the server machine using the command: python server_udp.py
6. Run the client code on the client machines using the command: python gui_client.py
7. ENJOY!!!
