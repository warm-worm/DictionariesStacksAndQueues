import json

voting_file = 'voting.json'

# Read the contents of the json file
try:
    with open(voting_file, 'r') as file:
        voting = json.load(file)
except FileNotFoundError:
    voting = {}

# Vote for a person
person_name = input('Name of the person you are voting for: ')
if person_name in voting: #vote count
    voting[person_name] += 1
else:
    voting[person_name] = 1

# Save voting data to json file
with open(voting_file, 'w') as file:
    json.dump(voting, file)

print(f'Voted for {person_name}.')