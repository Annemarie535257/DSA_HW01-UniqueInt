import os
import time
import psutil  # Importing psutil for memory measurement

class UniqueInt:
    @staticmethod
    def processFile(input_file_path, output_file_path):
        # Read input file and extract unique integers
        unique_integers = UniqueInt.readUniqueIntegers(input_file_path)
        
        # Sort unique integers using custom sort function
        unique_integers = UniqueInt.custom_sort(unique_integers)
        
        # Write unique integers to output file
        with open(output_file_path, 'w') as output_file:
            for integer in unique_integers:
                output_file.write(str(integer) + "\n")

        print("Unique integers written to output file:", output_file_path)

    @staticmethod
    def readUniqueIntegers(file_path):
        unique_integers = []
        with open(file_path, 'r') as file:
            for line in file:
                # Process each line according to the criteria
                integer = UniqueInt.process_line(line)
                if integer is not None and not UniqueInt.contains(unique_integers, integer):
                    unique_integers.append(integer)
        return unique_integers

    @staticmethod
    def process_line(line):
        # Custom stripping leading and trailing whitespace (including tabs and spaces)
        stripped_line = UniqueInt.custom_strip(line)

        # Skip empty lines
        if not stripped_line:
            return None
        
        # Split the line by whitespace
        parts = UniqueInt.custom_split(stripped_line)

        # Skip lines with more than one part or non-integer input
        if len(parts) != 1:
            return None
        
        # Try to convert the part to an integer
        if UniqueInt.is_integer(parts[0]):
            return int(parts[0])
        else:
            return None

    @staticmethod
    def custom_strip(s):
        result = ""
        i = 0
        while i < len(s) and (s[i] == ' ' or s[i] == '\t'):
            i += 1
        j = len(s) - 1
        while j >= 0 and (s[j] == ' ' or s[j] == '\t'):
            j -= 1
        for k in range(i, j + 1):
            result += s[k]
        return result

    @staticmethod
    def custom_split(s):
        parts = []
        part = ""
        for char in s:
            if char == ' ' or char == '\t':
                if part:
                    parts.append(part)
                    part = ""
            else:
                part += char
        if part:
            parts.append(part)
        return parts

    @staticmethod
    def is_integer(s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()

    @staticmethod
    def contains(arr, value):
        for item in arr:
            if item == value:
                return True
        return False

    @staticmethod
    def custom_sort(arr):
        # Implementing a simple bubble sort for demonstration
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

def measure_performance():
    # Prompt user to enter input file path
    input_file_path = input("Enter the input file path: ")

    # Define output file path
    output_file_path = input("Enter the output file path: ")

    # Record start time and memory usage
    start_time = measure_time()
    start_memory = measure_memory()

    # Process the input file
    UniqueInt.processFile(input_file_path, output_file_path)

    # Record end time and memory usage
    end_time = measure_time()
    end_memory = measure_memory()

    # Calculate runtime and memory usage
    runtime = (end_time - start_time) * 1000  # convert to milliseconds
    memory_used = end_memory - start_memory

    print("Runtime:", runtime, "milliseconds")
    print("Memory used:", memory_used, "bytes")

def measure_time():
    return time.time()

def measure_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

if __name__ == "__main__":
    measure_performance()
