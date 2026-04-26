import os
from datetime import datetime

print("Hello world from my devops app!")
def main():
    print("devops app running")
    print("Checking for .log files ...\n")
    count =0
    for filw in os.listdir('.'):
        if filw.endswith('.log'):
            count = count +1
            print(f"Found log file: {filw}")
    print(f"Total .log files found: {count}")
    print(f"Current date and time: {datetime.now()}")
    print("Environment:",os.getenv("ENVIRONMENT", "Not set"))

if __name__ == "__main__":
    main()
