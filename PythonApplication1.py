import os

print("hello, devops world")

files=os.listdir('.')
print("Files in this directory:")
for file in files:
    print(file)

def greet(name):
    print(f"Hello, {name}!Welcome to Devops.")

greet("Alice")

def times(name):
    print(name * 5)

times("Anvitha")

def loopingexample(name):
    for i in range(5):
        print(f"Hello {name}")

loopingexample("Anvitha")

name1 = input("Enter your name: ")
for i in range(3):
    print(f"Hello {name1}, welcome to the world of Devops!")