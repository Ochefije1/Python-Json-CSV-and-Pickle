import pickle

obj = {'Fruit', 89, 'Apple', 20}
with open('serializedObj', 'ab') as file:
    pickle.dump(obj, file)