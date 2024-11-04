import threading

def count_to_large_number():
    total = 0
    for i in range(10000000):
        total += i
    print(f"Total: {total}")

# Running two threads at once
t1 = threading.Thread(target=count_to_large_number)
t2 = threading.Thread(target=count_to_large_number)

t1.start()
t2.start()
t1.join()
t2.join()