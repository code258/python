f = open("temp.txt", 'r')
lines = f.readlines()
total_id = []
for line in lines:
    id, pwd = line.split(",")
    total_id.append(id)
f.close()
print(total_id)
f = open("temp.txt", 'a')
produce_id = input("Enter the your produce id : ")
produce_pwd = input("Enter the your produce pwd : ")
if produce_id not in total_id:
    f.write("\n" + produce_id)
    f.write("," + produce_pwd)

else:
    while produce_id in total_id:
        print("Your ID is duplicated.")
        produce_id = input("Enter the your produce id : ")
        produce_pwd = input("Enter the your produce pwd : ")

    if produce_id not in total_id:
        f.write("\n" + produce_id)
        f.write("," + produce_pwd)
