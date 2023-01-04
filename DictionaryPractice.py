entrance = {
  "descriptionText": "You see an old bridge leading to a crumbling gate. Beyond, you see a aging castle.",
  "occupants": [],
  "links": ["grandHall"]
}

grandHall = {
    "descriptionText": "You see a large open room.\n There is a staircase leading upstairs as well as down, and behind the stairs you see one door.",
    
    "occupants": [],
    "links": ["floodedRoom", "library", "tortureChamber"]
}

tortureChamber = {
  "descriptionText": "You walk into the torture chamber, inside you see a young man in chains, and a knight gaurding him. There is one blue door leading another way in the room",
  "occupants": ["knight", "son"],
  "links": ["floodedRoom", "grandHall"]
}

print(entrance["descriptionText"])

choiceValid = "no"

while(choiceValid == "no"):
    print("1. Move to the castle")

    choice = input()

    if(choice == "1"):
        print("You move to the castle")
        choiceValid = "yes"
    else:
        print("invalid choice, choose again")
          

