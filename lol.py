import pickle

print("Opening the model file...")
with open('regmodel.pkl', 'rb') as file:
    print("Loading the model...")
    model = pickle.load(file)
    print("Model loaded successfully")

# Further code to use the model
print(model)