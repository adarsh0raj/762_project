import random

print("id,sender_id,receiver_id,amount,start_time")
id = 0

# Generate random payments (Nodes: 0 to 99)
# Adversary Node: 0

# Generate Adversary to Victim Node payments
# vic_node = random.randint(0, 99)
vic_node = 1
for i in range(0, 5000):
    time = random.randint(0, 100)
    print(id, 0, vic_node, random.randint(1, 100), time, sep=',')
    print(id+1, vic_node, 0, random.randint(1, 100), time+1, sep=',')
    id += 2
    time += 1
    
# Generate random payments (Nodes: 0 to 99)
for i in range(0, 2000):
    print(id, random.randint(0,99), random.randint(0,99), random.randint(1, 100), random.randint(0, 100), sep=',')
    id += 1
    time += 1
