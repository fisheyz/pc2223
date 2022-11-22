#  Python program to illustrate the use
# of fast Input / Output
import io
import os
import time

# Function to take normal input


def normal_io():

    # Stores the start time
    start = time.perf_counter()

    # Take Input
    for i in range(10):
        s = input()

    # Stores the end time
    end = time.perf_counter()

    # Print the time taken
    print("\nTime taken in Normal I / O:",
          end - start)

# Function for Fast Input


def fast_io():

    start = time.perf_counter()
    input = io.BytesIO(os.read(0,
                               os.fstat(0).st_size)).readline
    for i in range(4000):
        print(input().decode())

    end = time.perf_counter()

    # Print the time taken
    print("\nTime taken in Fast I / O:",
          end - start)


# Driver Code
if __name__ == "__main__":

    # Function Call
    # normal_io()

    fast_io()
