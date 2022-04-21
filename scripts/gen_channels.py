import random

print("id,edge1_id,edge2_id,node1_id,node2_id,capacity")
id = 0
capacity = 50000

# Adversary Node: 0

# Generate Adversary to Victim Node payments
# vic_node = random.randint(0, 99)
vic_node = 1

print(0,0,1,0,1,50000000,sep=',')
for i in range(0, 500):
    
    print(id, 0, vic_node, random.randint(1, 100), time, sep=',')
    print(id+1, vic_node, 0, random.randint(1, 100), time, sep=',')
    id += 2
    time += 1
    
# Generate random payments (Nodes: 0 to 99)
for i in range(0, 200):
    print(id, random.randint(0,99), random.randint(0,99), random.randint(1, 100), time, sep=',')
    id += 1
    time += 1
