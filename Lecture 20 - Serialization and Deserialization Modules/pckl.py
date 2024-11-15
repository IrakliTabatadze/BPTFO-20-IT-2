import pickle

hello_str = "Hello World!"

pckl_string = pickle.dumps(hello_str)
print(pckl_string)

with open('data.pkl', 'wb') as pkl_file:
    pickle.dump(hello_str, pkl_file)


data = pickle.loads(pckl_string)
print(data)

with open('data.pkl', 'rb') as pkl_file:
    print(pickle.load(pkl_file))


