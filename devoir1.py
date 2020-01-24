url = "https://montrealcampus.ca?p=30145"
BASE = (url[:28])
# print (BASE + ID)
ID = []
for x in range(20000,30151):
    ID.append(BASE + str(x))
print (ID)
print (len(ID))

