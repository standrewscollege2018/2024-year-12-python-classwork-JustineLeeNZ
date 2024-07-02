#set up list of lists
client_list = [["John", "Smith",16],["Bob","Roberts",18],["Billy","Roberts",14]]

# ugly print of whole of client_list for debug only
print("Ugly printing whole of client_list")
print(client_list)

# ugly print of sublist for debug only
print("\nUgly printing second sublist")
print(client_list[1])

# display a specific item in sublist e.g. firstname
print("\nPrinting first name of first client")
print(f"Dear {client_list[0][0]}")

# add a whole new sublist
client_list.append(["Jane", "Smith", 20])
# ugly print for debug
print("\nUgly printing updated client list after append()  (+ Jane Smith)")
print(client_list)

# add a new sublist using variables
# add values to variables, could also use input() to get values from user
f_name = "Sam"
l_name = "Edwards"
age = 16
# add new sublist to end of existing client_list
client_list.append([f_name,l_name,age])
# ugly print for debug
print("\nUgly printing updated client list after append()  (+ Sam Edwards)")
print(client_list)


# nice printing of the whole list
# use for loop because know how many times needs to run using len() of list
# use i as index of current sublist
print("\n Nicely printing each sublist using for loop")
for i in range(0,len(client_list)):
    print(f"Name: {client_list[i][0]} {client_list[i][1]} Age: {client_list[i][2]} ")


# delete a sublist
del(client_list[1])
# ugly print for debug
print("\nUgly printing updated client list after del()  (- Bob Roberts)")
print(client_list)

#update item in sublist
client_list[3][2] = 20
print("\nUgly printing updated client list (changed age of Sam Edwards to 20)")
print(client_list)








