import irc, os
os.system('clear')

channel = "#madkamel-irkbot-testing"
server = "irc.freenode.net"
nickname = "madkamel-irkbot"

client = irc.IRC()
client.connect(server, channel, nickname)


while True:
  text = client.get_text()
  print(text)

  if "PRIVMSG" in text and channel in text and "hello" in text:
    client.send(channel, "Hello!")