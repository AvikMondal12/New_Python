import random
subjects = [
  "Saharukh Khan",
  "Virat Kohli",
  "Nirmalaha Sitaraman",
  "A Mumbai Cat",
  "A Group of Monkey",
  "Prime Minister Modi",
  "A auto Driver from Delhi"
]
actions = [
  "launches",
  "cancels",
  "dances with",
  "eats",
  "declears war on",
  "orders",
  "celebrates"
]

places_or_things = [
  "at Red Fort",
  "in Mumbai Local Train",
  "a plate of samosa",
  "inside parlament",
  "during IPL match",
  "at Indaia Gate"
]

while True:
  subject = random.choice(subjects)
  action = random.choice(actions)
  place_or_thing = random.choice(places_or_things)
  
  
  headline = f" BREAKING NEWS : {subject} {action} {place_or_thing}"
  print("\n",headline)
  
  user_input = input("\n Do you want another headline YES/NO :").strip().lower()
  
  if user_input == "no":
    break
  
print("Thank you, Visit again ...")