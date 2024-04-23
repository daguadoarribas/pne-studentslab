import json

with open('people-e1.json') as f:
    data = json.load(f)

print("Total number of people:", len(data))
for person in data:
    print("\nFirstname:", person["Firstname"])
    print("Lastname:", person["Lastname"])
    print("Age:", person["age"])
    print("Phone Numbers:")
    for number in person["phoneNumber"]:
        print("  Type:", number["type"])
        print("  Number:", number["number"])
