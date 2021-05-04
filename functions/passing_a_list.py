# Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(),
# which prints each text message.

def show_messages(texts):
    for text in texts:
        print(f'{text}')

messages = ['what would you like for dinner?', 'meet me by the bridge', 'i\'m 5 minutes away']
show_messages(messages)

# Sending Messages: Start with a copy of your previous programming. Write a function called send_messages() that prints 
# each text message and moves each message to a new list called sent_message as it's printed. After calling the function
# print both of your lists to make sure the messages were moved correctly.

def send_messages(texts, sent_texts):
    while texts:
        received = texts.pop()
        sent_texts.append(received)

def list_of_messages(list_messages):
    for message in list_messages:
        print(f'{message}')

messages = ['what would you like for dinner?', 'meet me by the bridge', 'i\'m 5 minutes away']
sent_messages = []

send_messages(messages, sent_messages)
list_of_messages(sent_messages)

print(messages)
print(sent_messages)

# Archived Messages: Call the function send_messages() with a copy of the list of messages. After calling the function,
# print both of your lists to show that the original list has retained its messages.

def send_messages(texts, sent_texts):
    while texts:
        received = texts.pop()
        sent_texts.append(received)

def list_of_messages(list_messages):
    for message in list_messages:
        print(f'{message}')

messages = ['what would you like for dinner?', 'meet me by the bridge', 'i\'m 5 minutes away']
sent_messages = []

send_messages(messages[:], sent_messages)
list_of_messages(sent_messages)

print(messages)
print(sent_messages)
    