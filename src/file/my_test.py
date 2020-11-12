import re

str = re.split(r'(?:\s+)', open("27-A_demo.txt", "r").read().strip())

print(str)

