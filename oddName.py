""" Hayden """
name = str(input("inster name"))
while len(name) == 0:
    name=input("insert name")
for i in range(0, len(name), 2):
    print(name[i])