import random

subjects = [
    "Shahrukh Khan",
    "Virat Kohli", 
    "Nirmal Sitaraman", 
    "A Mumbai Cat", 
    "A Group of Monkeys", 
    "PM Modi", 
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances",
    "eats",
    "declares war",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"

    print("\n" + headline)
    print("\n Do you want another headline")

    user_choice = input("Enter 'yes' or 'no' : ").strip().lower()

    if user_choice == "no":
        break

print("\n Thanks for using fake news headline generator! have a fun day")