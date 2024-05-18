### Description of the Code

The provided Python script is designed to read an input file containing integers, extract unique integers from the file, sort them, and write the sorted unique integers to an output file. Additionally, the script measures the runtime and memory usage during its execution. Below is a detailed description of the various components and functions within the code:

#### 1. **Class: `UniqueInt`**
The `UniqueInt` class contains several static methods to handle the processing of the input file and manage the unique integer extraction, sorting, and writing to the output file.

##### **`processFile` Method**
- **Input**: Paths for the input file and output file.
- **Function**:
  - Reads unique integers from the input file.
  - Sorts the unique integers using a custom sorting method.
  - Writes the sorted unique integers to the specified output file.
  - Prints a confirmation message with the output file path.

##### **`readUniqueIntegers` Method**
- **Input**: Path to the input file.
- **Output**: List of unique integers.
- **Function**:
  - Reads the input file line by line.
  - Processes each line to extract integers.
  - Checks if the integer is unique and adds it to the list if it is.

##### **`process_line` Method**
- **Input**: A line from the input file.
- **Output**: An integer or `None`.
- **Function**:
  - Strips leading and trailing whitespace from the line.
  - Splits the line by whitespace.
  - Checks if the line contains exactly one integer part.
  - Converts the valid integer part to an integer and returns it.

##### **`custom_strip` Method**
- **Input**: A string.
- **Output**: Stripped string.
- **Function**:
  - Manually removes leading and trailing whitespace (spaces and tabs).

##### **`custom_split` Method**
- **Input**: A string.
- **Output**: List of parts split by whitespace.
- **Function**:
  - Splits the string by spaces and tabs into a list of parts.

##### **`is_integer` Method**
- **Input**: A string.
- **Output**: Boolean indicating if the string is an integer.
- **Function**:
  - Checks if the string represents a valid integer.

##### **`contains` Method**
- **Input**: A list and a value.
- **Output**: Boolean indicating if the list contains the value.
- **Function**:
  - Checks if the value exists in the list.

##### **`custom_sort` Method**
- **Input**: A list of integers.
- **Output**: Sorted list of integers.
- **Function**:
  - Implements a simple bubble sort algorithm to sort the list of integers.

#### 2. **Function: `measure_performance`**
- **Function**:
  - Prompts the user to input the file paths for the input and output files.
  - Measures the start time and memory usage before processing the file.
  - Calls the `processFile` method to process the file.
  - Measures the end time and memory usage after processing the file.
  - Calculates and prints the runtime and memory used during processing.

#### 3. **Function: `measure_time`**
- **Output**: Current time in seconds since the epoch.
- **Function**:
  - Returns the current time using `time.time()`.

#### 4. **Function: `measure_memory`**
- **Output**: Memory usage in bytes.
- **Function**:
  - Uses the `psutil` library to get the current process's memory usage.
  - Returns the Resident Set Size (RSS) memory usage, which is the portion of memory occupied by the process held in RAM.

#### 5. **Main Execution Block**
- **Function**:
  - Executes the `measure_performance` function if the script is run as the main module.

### Key Points:
- **Custom Methods**: The script includes custom implementations for string stripping, splitting, and sorting to avoid using built-in Python functions directly, likely for educational purposes.
- **Memory Measurement**: Utilizes the `psutil` library to measure the memory usage of the process, providing a realistic insight into the script's memory consumption.
- **Performance Measurement**: Measures both the runtime and memory usage to evaluate the efficiency of the script.

This script is useful for understanding file processing, custom string manipulation, sorting algorithms, and performance measurement in Python.
