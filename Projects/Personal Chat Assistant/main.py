#Rule Based AI Python ChatBot

import datetime
import time

name = input("Welcome, Enter your name : ")
curr_hour = datetime.datetime.now().hour

if 5 <= curr_hour < 11:
    print(f"Good morning, {name}")
elif 11 <= curr_hour < 17:
    print(f"Good afternoon, {name}")
elif 17 <= curr_hour <= 20:
    print(f"Good evening, {name}")
else:
    print(f"Good night, {name}")


print("Welcome to Your Personal ChatBot")
print("you can ask me basic question, Type 'bye' to exit from the bot")

# Chatbot Memory Creation [dictionary of responses]

responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every big of your project makes you a better developer",
    "happy": "That's awesome! Keep smiling, life is beautiful 😊",
    "sad": "I'm sorry you're feeling sad. Things will get better 💙 Stay strong.",
    "bye": "Bye! Talk to you later"
}

#Function to get response

def getResponseFromBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "As of now i am not able to answer that question. I am still in learning mode"

# Take user input

while True:
    user_input = input("Please ask your question : ")
    reply = getResponseFromBot(user_input)
    print("Bot Response :", reply)

    time.sleep(0.5) # 1 second delay after response

    if "bye" in user_input.lower():
        break