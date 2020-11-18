import irc


client = irc.IRC()

client.connect("chat.freenode.net", "#mad-kamel-irc-bots:matrix.org", "madkamel_irkbot")

while True:
  if client.get_text() == 'irk-test':
    print("message recieved")