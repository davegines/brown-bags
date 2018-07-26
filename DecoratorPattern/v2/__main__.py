import time
from DecoratorPattern.stopwatch import elapsed_time


@elapsed_time
def perform_operation():
    print("The operation has started...")
    time.sleep(.5)
    print("The operation has completed.")


elapsed_time = perform_operation()  # invoke the function
print("Elapsed time {}: ".format(elapsed_time))
