import random

print("id,channel_id,counter_edge_id,from_node_id,to_node_id,balance,fee_base,fee_proportional,min_htlc,timelock")
id = 0
# Adversary Node: 0
vic_node = 1
node1 = 0
node2 = 1

for i in range(0, 100):
    print(id, )
for i in range(0, 500):
    
    print(id, 0, vic_node, random.randint(1, 100), time, sep=',')
    print(id+1, vic_node, 0, random.randint(1, 100), time, sep=',')
    id += 2
    
# Generate random payments (Nodes: 0 to 99)
for i in range(0, 200):
    print(id, random.randint(0,99), random.randint(0,99), random.randint(1, 100), time, sep=',')
    id += 1
