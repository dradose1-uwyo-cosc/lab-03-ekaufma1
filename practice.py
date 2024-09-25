names = ["Ellie", "Brady", "Addie", "Analiese", "Rueben"]
print(names)

#del
del names[0]
print(names)

#.remove
names.remove("Brady")
print(names)

names.append("Ally")
print(names)

#Addie is at my table
#Analiese is at my table
#Rueben is at my table
#Ally is at my table

for name in names:
    print(f"{name} is on my table")

names.reverse()
print(names)
