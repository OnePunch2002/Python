import time

x = int(input("Enter time limit: "))
for seconds in range(x,0,-1):
    print(seconds)
    time.sleep(1)
print("Countdown ended")