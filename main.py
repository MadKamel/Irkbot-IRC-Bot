import irc, os
os.system('clear')

channel = "#mad-kamel-irc-bots:matrix.org"
server = "irc.freenode.net"
nickname = "madkamel-irkbot"

client = irc.IRC()
client.connect(server, channel, nickname)


while True:
  text = client.get_text().decode()
  print(text)

  if "PRIVMSG" in text and channel in text and "hello" in text:
    client.send(channel, "Hello!")