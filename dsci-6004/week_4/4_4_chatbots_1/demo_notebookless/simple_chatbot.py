#!/usr/bin/env python
""" A chatbot that greets people
"""

import random

greetings = set('hola hello hi Hi hey! hey'.split())
question = {'How are you?','How are you doing?'}
responses = set("Okay | I'm fine".split(" | "))

def conversation_start():
    while True:
        user_input = input(">>> ")
        if user_input in greetings:
            print(random.sample(greetings, 1))
        elif user_input in question:
            print(random.sample(responses, 1))
        elif user_input == 'q':
            print('Talk to you later!')
            break
        else:
            print("I did not understand what you said.")
            
if __name__ == "__main__":
    conversation_start()