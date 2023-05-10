import pickle

# persistence is the practice of saving data in a database


# pickle has 2 majpor method             for saving and fpor serializing

# dump serializes and saves the file in your local machine, and this file cannot be altered by a third part
# dumps serializes, but doesnt't save locally in your machine, and returns a string

# pickle is better to use unlike txt files, because it is impossible to it's content to be altered, especially by intruders.
# you cannot modify serialized data, except it is converted back to a python object, whether it is dumps or dumps.


python_obj = {'name':'Milo', 'price':1200}

with open('seriallizedObj', 'ab') as file:
    pickle.dump(python_obj, file) 