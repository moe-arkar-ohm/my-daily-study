import threading

# Global variable (The "Kitchen")
counter = 0

def increase():
    global counter
    for _ in range(1000000):
        # This looks like one step, but the CPU sees 3 steps:
        # 1. Read counter
        # 2. Add 1
        # 3. Write counter
        counter += 1

# 1. Create two threads (People in the house)
t1 = threading.Thread(target=increase)
t2 = threading.Thread(target=increase)

# 2. Start them at the same time
print("Starting threads...")
t1.start()
t2.start()

# 3. Wait for them to finish
t1.join()
t2.join()

print(f"Expected Value: 2000000")
print(f"Actual Value:   {counter}")
