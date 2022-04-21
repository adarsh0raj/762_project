lines = []
with open("../payments.csv", "r") as f:
    f.readline()
    lines = [x.rstrip("\n").split(",") for x in list(f.readlines())] 
print(lines[0])