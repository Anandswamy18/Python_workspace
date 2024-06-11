import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None
    
    def start(self):
        self.start_time = time.time()
        print("Stopwatch started...")
    
    def stop(self):
        if self.start_time is None:
            print("Stopwatch hasn't been started yet!")
        else:
            self.end_time = time.time()
            elapsed_time = self.end_time - self.start_time
            print(f"Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds")


stopwatch = Stopwatch()


input("Press Enter to start the stopwatch...")
stopwatch.start()


input("Press Enter to stop the stopwatch...")
stopwatch.stop()
