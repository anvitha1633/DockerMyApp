import os

files=os.listdir('.')

print("Checking for .log files ...\n")
count =0
for filw in files:
	if filw.endswith('.log'):
		count = count +1
		print(f"Found log file: {filw}")
print(f"Total .log files found: {count}")