import time
from DecoratorPattern import stopwatch


def perform_operation():
    print("The operation has started...")
    time.sleep(.5)
    print("The operation has completed.")


perform_operation_decorated = stopwatch.elapsed_time(perform_operation)
elapsed_time = perform_operation_decorated()  # invoke the function
print("Elapsed time: {}".format(elapsed_time))
