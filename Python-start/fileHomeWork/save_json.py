import json
from music_serialize import my_favourite_group


with open('group.json', 'w') as f:
    json.dump(my_favourite_group, f)

with open('group.json', 'r') as f:
    print(json.load(f))