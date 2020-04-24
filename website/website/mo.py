l = []
with open('carname.txt') as f:
    for user in f:
        l.append(user.strip())
with open('new_carname.txt', 'w') as f:
    for u in l:
        f.write("\"" + u + "\"" + ",\n")
