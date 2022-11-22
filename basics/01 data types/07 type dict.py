
contacts = {
    "Ola" : "ola@example@com",
    "Daniel" : 30,
    "Ania" : "ania@example@com"
}

contacts["Rafal"] = "rafal@example.com"

print(contacts["Ola"])

print(contacts.keys())
print(contacts.values())

for key in contacts:
    print(key + " " + str(contacts[key]))