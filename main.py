from irc_class import *
import os
import random

## IRC Config
server = "matrix.org" # Provide a valid server IP/Hostname
port = 6697
channel = "#nodecore"
botnick = "IrkBot"
botnickpass = "breenbot1337"
botpass = "<%= @breenbot1337 %>"
irc = IRC()
irc.connect(server, port, channel, botnick, botpass, botnickpass)

while True:
    text = irc.get_response()
    print(text)
 
    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello!")