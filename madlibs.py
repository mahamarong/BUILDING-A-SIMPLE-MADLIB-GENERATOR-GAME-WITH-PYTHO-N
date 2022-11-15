#string concatenation (aka how to put string together)
# suppose we want to create a string that says "subscribe to _______"

# youtuber = "Marong" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber} ")

# adj = input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famous_person = input("Famous person: ")

# madlib = f"Computer programming gis so {adj}! It makes me so excited all the time because  \
# I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

# print(madlib)

# Mad Libs Generator
#----------------------------------------

#Loop back to this point once code finishes

#All the questions that the program asks the user
noun = input("Choose a noun: ")
noun2 = input("Choose a noun: ")
adjective = input("Choose an adjective (Describing word): ")
noun3 = input("Choose a  noun: ")
noun4 = input("Choose a  noun: ")
verb1 = input("Choose a verb: ")
verb2 = input("Choose a verb: ")
verb3 = input("Choose a verb: ")
            # place = input("Name a place: ")
            # adjective = input("Choose an adjective (Describing word): ")
            # noun3 = input("Choose a noun: ")
        #Displays the story based on the users input
print ("------------------------------------------")
print (f"It was {noun} day at school, and {noun2} was super {adjective} for lunch. \
 But when she went outside to eat, a {noun3} stole her {noun}! {noun2} chased the {noun3} all over school. \
She {verb1}, {verb2}, and {verb3} through the playground. \
Then she tripped on her {noun4} and the {noun3} escaped! Luckily, {noun2} ’s friends were willing to share their {noun} with her.")
print ("------------------------------------------")
