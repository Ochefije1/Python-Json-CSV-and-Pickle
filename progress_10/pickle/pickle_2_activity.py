import pickle


pythonObj = {'name':'Milo', 'price':1200, 'quantiyy':10}
# with open('serializedObj', 'rb') as file:
#     obj = pickle.load(file)
#     print(obj)


serialized_obj = pickle.dumps(pythonObj)
print(serialized_obj)

python = pickle.loads(serialized_obj)
print(python)