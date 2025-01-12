import json

data = {
    "title": "Shrek",
    "release_year": 2001,
    "genre": "Animation, Comedy, Family",
    "main_characters": ["Shrek", "Donkey", "Princess Fiona", "Lord Farquaad"],
    "theme": "Acceptance, Friendship, Overcoming Stereotypes"
}

# Specify the file path and name
file_name = "favourite.json" #with a typo ig

# Open the file in write mode and use json.dump() to write the data to the file
with open(file_name, 'w') as file:
   json.dump(data, file, indent=4)

print("Data has been written to", file_name)
