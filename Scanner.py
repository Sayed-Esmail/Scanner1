import re

# Define regex patterns for different C++ components
patterns = {
    "Single-line comment": r"//.*?$",  # Match single-line comments
    "Multi-line comment": r"/\*[\s\S]*?\*/",  # Match multi-line comments
    "Keywords": r"\b(auto|break|string|case|char|const|endl|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|namespace|operator|register|return|short|signed|sizeof|static|struct|switch|template|typedef|union|unsigned|void|volatile|while|bool|catch|class|const_cast|delete|dynamic_cast|explicit|export|friend|inline|mutable|new|private|protected|public|reinterpret_cast|static_cast|template|this|throw|try|typeid|typename|using|virtual|wchar_t|cout|cin|endl|cerr|clog|iostream|include|std|main)\b",
    "Character constants": r"'([^'\\]*(\\.[^'\\]*)*)'",  # Match character literals including escaped characters
    "String literals": r'"([^"\\]*(\\.[^"\\]*)*)"',  # Match string literals including escaped characters
    "Identifiers": r"\b[a-zA-Z_]\w*\b",  # Identifiers should follow keywords and constants
    "Operators": r"[+\-*/%=&|^!<>~?:]+",  # Common operators in C++
    "Numeric constants": r"\b\d+(\.\d+)?\b",  # Match integers and floating-point numbers
    "Special characters": r"[{}()\[\],.;]",  # Common special characters in C++
}

# Function to classify components in C++ code
def classify_cpp_components(code):
    token_list = []
    
    # Process each pattern with priority given to comments, keywords, and constants
    for key in ["Single-line comment", "Multi-line comment", "Keywords", "Character constants", "String literals", "Numeric constants", "Operators", "Special characters", "Identifiers"]:
        pattern = patterns[key]
        matches = list(re.finditer(pattern, code, re.MULTILINE))
        
        # Extract each match with its position in code
        for match in matches:
            value = match.group()
            start_position = match.start()
            if key == "Identifiers" and any(value == token[0] for token in token_list if token[1] == "Keywords"):
                continue  # Skip identifiers that match keywords
            token_list.append((value, key, start_position))
            code = code[:match.start()] + " " * (match.end() - match.start()) + code[match.end():]  # Replace with spaces
    
    # Sort tokens by their position in ascending order
    token_list.sort(key=lambda x: x[2])  # Sort by the start position
    
    # Format tokens with type for output
    formatted_tokens = [f"{value} [{token_type}]" for value, token_type, _ in token_list]
    
    return formatted_tokens

# Read from input file and write to output file
def scan_cpp_file(input_file, output_file):
    # Read the C++ code from the input file
    with open(input_file, 'r') as file:
        cpp_code = file.read()
    
    # Classify components
    classified_tokens = classify_cpp_components(cpp_code)
    
    # Write the results to the output file in ascending order
    with open(output_file, 'w') as file:
        for token in classified_tokens:
            file.write(f"{token}\n")  # Write each token with its type

# Specify the input and output files
input_file = r"E:\Fourth Year\Scanner of C++\input.txt"
output_file = r"E:\Fourth Year\Scanner of C++\output.txt"
# Run the scanner
scan_cpp_file(input_file, output_file)

print(f"Classification completed. Check '{output_file}' for results.")
