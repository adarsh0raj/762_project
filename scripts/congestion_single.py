import random

lines = []
with open("../payments.csv", "r") as f:
    f.readline()
    lines = [x.rstrip("\n").split(",") for x in list(f.readlines())] 

payments = len(lines)
print("Payments: ", payments)
nodes = 2099
buf = 100

# vic_node = random.randint(0, nodes)
vic_node = 827

t = 500
n = int(payments/4)
for i in range(n):
    lines[i][1], lines[i][2] = str(507), str(vic_node)
    lines[i][4] = str(t)
    lines[i][3] = str(int(lines[i][3])*200)
    # t += 1
    
# t=10
# for i in range(n, 2*n):
#     lines[i][1], lines[i][2] = str(vic_node), str(0)
#     lines[i][4] = str(t)
#     t += 1

with open("../payments.csv", "w") as f:
    f.truncate()
    f.write("id,sender_id,receiver_id,amount,start_time\n")
    for line in lines:
        f.write(",".join(line) + "\n")
        
print("Victim Node Selected: ", vic_node)



