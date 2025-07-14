import random as rd

action_list = [
    "hit a six",
    "took a diving catch",
    "scored a century",
    "celebrated with a fist pump",
    "bowled a perfect yorker",
    "gave an inspiring speech",
    "signed an autograph",
    "ran between wickets",
    "practiced in the nets",
    "waved at the crowd"
]

places_list = [
    "in Wankhede Stadium",
    "at Eden Gardens",
    "in Lord's Cricket Ground",
    "in a training camp",
    "during a post-match conference",
    "at an IPL event",
    "on a cricket field in Dubai",
    "at a charity match",
    "in their hometown",
    "on a rainy day match in Bengaluru"
]


while True:
  user_input = input("Give an Indian cricketer name:- ")
  if user_input == "exit":
    break
  else:
    random_action = rd.choice(action_list)
    random_place = rd.choice(places_list)

    print(f"{user_input} {random_action} {random_place}")