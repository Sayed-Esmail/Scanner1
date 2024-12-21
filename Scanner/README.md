# C++ Code Scanner

This Python script scans and classifies different components in C++ code. It identifies single-line comments, multi-line comments, keywords, character constants, string literals, identifiers, operators, numeric constants, and special characters. The script then outputs these classified components along with their positions in the source code.

## Features

- **Single-line Comments**: Identifies comments starting with `//`.
- **Multi-line Comments**: Identifies comments enclosed in `/* */`.
- **Keywords**: Recognizes C++ keywords such as `if`, `for`, `while`, `class`, etc.
- **Character Constants**: Identifies character constants (e.g., `'a'`, `'1'`).
- **String Literals**: Identifies string literals (e.g., `"Hello World"`).
- **Identifiers**: Identifies valid identifiers in the code.
- **Operators**: Identifies operators like `+`, `-`, `*`, `&&`, etc.
- **Numeric Constants**: Identifies integer and floating-point numbers.
- **Special Characters**: Identifies special characters like `{`, `}`, `()`, etc.

## Requirements

- Python 3.x
- Regular expressions (`re` module) for pattern matching

## How It Works

1. The script processes C++ code from an input file.
2. It uses regular expressions to classify different components such as comments, keywords, literals, operators, and more.
3. The components are then outputted in the same order they appear in the code, along with their type and position.
4. The result is written to an output file.

## Usage Instructions

### Step 1: Modify the File Paths

Before running the script, make sure to change the paths for the input file and output file.

In the script, you will find the following lines:

#### input_file = r"E:\Fourth Year\Scanner of C++\input.txt".
#### output_file = r"E:\Fourth Year\Scanner of C++\output.txt".

- **input_file**: The path to the C++ source code file you want to scan.
- **output_file**: The path where you want the results to be saved.
Modify these paths to match the location of your input file and where you want the output to be saved.

### Step 2: Running the Script
1. Ensure Python 3.x is installed on your machine.
2. Place the Python script and the input C++ file in your project directory or any directory of your choice.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the Python script.
5. Run the script using the following command:
