"""
You are a secret agent, and you receive an encrypted message that needs to be decoded.
The code that is being used flips the message backwards and inserts non-alphabetic characters in the message to make it hard to decipher.
"""
import string


def decode_message(msg):
    msg_reversed = msg[::-1]
    msg_cleaned = ''
    for char in msg_reversed:
        if char.lower() in string.ascii_lowercase or char == ' ':
            msg_cleaned += char
    return msg_cleaned


message_received = 'etome %^&^&*l^&E!D- -enozzaf'
print(decode_message(message_received))