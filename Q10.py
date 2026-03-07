import os
new1="Newfolder"
def new():
    os.mkdir(new1)
    cwd1=os.getcwd()
    print(cwd1)

new()
