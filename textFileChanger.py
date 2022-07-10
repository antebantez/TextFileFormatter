#script to add " before and ",\n after every line in a txt-file
filepath = "change.txt"
with open(filepath, "r") as f:
  lines = f.read().splitlines()
with open(filepath, "w") as f:
  for line in lines:
    f.write('"' + line + '",\n')