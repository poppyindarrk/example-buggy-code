import threading

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        current = self.count
        self.count = current + 1

def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = Counter()
threads = [threading.Thread(target=worker, args=(counter,)) for _ in range(2)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Final count: {counter.count}")
