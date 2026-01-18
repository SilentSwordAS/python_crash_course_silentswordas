
def send_messages(message_list, sent_messages):
    while message_list:
        msg = message_list.pop()
        print(msg)
        sent_messages.append(msg)

text_msg = [
    "Hope your day is going great, keep smiling and shining!",
    "Just wanted to check in and see how you're doing.",
    "Don't stress too much today, everything will work out fine.",
    "Remember to take breaks and drink water while working hard.",
    "Life feels lighter when you focus on things you can control."
]

sent_msg = []

# Moving the messages from text_msg to sent_msg
send_messages(text_msg, sent_msg)

# Verifying that the messages were moved successfully
print(text_msg)
print(sent_msg)