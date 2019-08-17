import pickle
from music_serialize import my_favourite_group


with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)

with open('group.pickle', 'rb') as f:
    print(pickle.load(f))