import pickle
import json

with open('group.pickle', 'rb') as f:
    print(pickle.load(f))

with open('group.json', 'r') as f:
    print(json.load(f))