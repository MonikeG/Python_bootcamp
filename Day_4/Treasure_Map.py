# 🚨 Don't change the code below 👇



row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# if position == "11":
#     row1[0] = "X"
# if position == "12":
#     row1[1] = "X"
# if position == "13":
#     row1[2] = "X"
# if position == "21":
#     row2[0] = "X"
# if position == "22":
#     row2[1] = "X"
# if position == "23":
#     row2[2] = "X"
# if position == "31":
#     row3[0] = "X"
# if position == "32":
#     row3[1] = "X"
# if position == "33":
#     row3[2] = "X"    
#print(row1)

vertical = int(position[])
horizontal = int(position[])

map [vertical - 1][horizontal - 1] = 'X'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


