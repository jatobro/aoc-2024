lines = list()

with open("./input.txt") as f:
  for line in f:
    lines.append(line.rstrip())
    
    
for line in lines:
  print(line)