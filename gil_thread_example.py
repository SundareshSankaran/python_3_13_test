import time
start_time = time.time()


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


print("--- %s seconds ---" % (time.time() - start_time))


# Output from Python 3.13 - single threaded

# Total: 49999995000000
# Total: 49999995000000
# --- 0.6976718902587891 seconds ---

# Output from Python 3.13t - free threaded
# Total: 49999995000000
# Total: 49999995000000
# --- 0.4113438129425049 seconds ---

