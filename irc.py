import socket
import sys


class IRC:

    irc = socket.socket()
  
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " " + msg + "n")

    def connect(self, server, channel, botnick):
        print("connecting to: " + server)
        self.irc.connect((server, 6667))
        print("connection complete.")
        self.irc.send("USER " + botnick + " " + botnick + " " + botnick + " " + botnick + "n")
        self.irc.send("NICK " + botnick + "n")
        self.irc.send("JOIN " + channel + "n")

    def get_text(self):
        text = self.irc.recv(2040)

        if text.find('PING') != -1:                      
            self.irc.send('PONG ' + text.split()[1] + 'rn') 

        return text