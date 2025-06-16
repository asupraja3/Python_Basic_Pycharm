

import multiprocessing

def square(n):
    print(n * n)

if __name__ == "__main__": # This is necessary to avoid recursive spawning of subprocesses on Windows
    p1 = multiprocessing.Process(target=square, args=(5,)) # Create a process to run the square function with argument 5
    p1.start() # Start the process
    p1.join()# Wait for the process to finish

# This code creates a new process that runs the `square` function, which prints the square of the number passed to it.
# The `if __name__ == "__main__":` block is necessary to ensure that the code runs correctly on Windows,
# #     where the multiprocessing module requires this guard to prevent recursive spawning of subprocesses.
# The `p1.join()` method is used to wait for the process to finish before the main program continues.
# The `multiprocessing` module allows you to create and manage separate processes, which can run concurrently.
# This is useful for CPU-bound tasks where you want to take advantage of multiple CPU cores.
# The `multiprocessing` module is a powerful way to achieve parallelism in Python, especially for CPU-bound tasks.

# Differences between multithreading and multiprocessing:
# 1. **Execution Model**:
#    - **Multithreading**: Uses threads, which are lighter than processes and share the same memory space. Threads can run
#    concurrently but are limited by the Global Interpreter Lock (GIL) in CPython, which allows only one thread to execute Python
#    bytecode at a time.
#    - **Multiprocessing**: Uses separate processes, each with its own memory space. This allows true parallel execution on multiple
#    CPU cores, bypassing the GIL limitation.
# 2. **Memory Usage**:
#    - **Multithreading**: Threads share the same memory space, which can lead to lower memory usage but also requires careful management
#    of shared data to avoid
#    - **Multiprocessing**: Each process has its own memory space, which can lead to higher memory usage but avoids issues with shared state.
#    Communication between processes typically requires inter-process communication (IPC) mechanisms like pipes or queues.

# 3. **Performance**:
#    - **Multithreading**: Generally better for I/O-bound tasks (like network requests, file I/O) where threads can wait for I/O
#    operations to complete while allowing other threads to run.
#    - **Multiprocessing**: Better for CPU-bound tasks (like heavy computations) where processes can run in parallel on multiple CPU cores,
#    fully utilizing the available hardware.

#What is shareed state?
# Shared state refers to the ability of multiple threads or processes to access and modify the same data or resources.