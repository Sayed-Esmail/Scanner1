# Recursive Descent Parser

This Python script implements a **Recursive Descent Parser** with support for user-defined grammars. The parser validates input sequences against the defined grammar, checks if the grammar is **Simple**, and generates a parse tree for valid sequences.

## Features

1. **Enter Grammar Rules**: Define the grammar using rules like `S -> aSb`.  
2. **Check if Grammar is Simple**: Verify if the grammar follows Simple Grammar rules:
   - Productions start with a terminal.
   - No two productions of the same non-terminal start with the same terminal.
3. **Validate a Sequence**: Check if a sequence is valid under the grammar and generate a parse tree.
4. **Exit**: Exit the program.

---

## How It Works

### Grammar Rules Format
- Input grammar rules in the format: `NonTerminal -> Production`.  
- Example: `S -> aSb` or `A -> b`.  
- Enter `done` when finished entering rules.

### Simple Grammar Rules
A grammar is considered **Simple** if:  
1. All productions for a non-terminal start with a terminal.  
2. No two productions for the same non-terminal start with the same terminal.  
3. **Empty String Rule**: Non-terminals cannot produce the empty string (`ε`).  


### Validating a Sequence
- The sequence is validated against the user-defined grammar if it is Simple.
- If valid, a parse tree is generated.

---

## Program Workflow

1. **Menu Options**
   - Choose an option from the menu:
     - Enter Grammar Rules.
     - Check if Grammar is Simple.
     - Validate a Sequence.
     - Exit.
2. **Validation**
   - If validating a sequence, the program builds a **Transition Table** from the grammar and processes the sequence using a stack-based approach.
3. **Parse Tree**
   - If the sequence is valid, a parse tree is displayed.

---

## Code Explanation

### Main Functions

- `main()`: The entry point for the program. Manages menu options and user inputs.
- `is_simple_grammar(grammar)`: Checks if the entered grammar is Simple.
- `validate_sequence(grammar, start_non_terminal, sequence, parse_tree)`: Validates a sequence using a stack and transition table.
- `build_transition_table(grammar)`: Constructs a transition table for the grammar.
- `draw_parse_tree(parse_tree)`: Displays the parse tree.

### Data Structures

- **`grammar`**: A dictionary storing grammar rules, where keys are non-terminals and values are lists of productions.
- **`transition_table`**: A dictionary defining transitions based on the grammar.

---

## Example Usage

### 1. Enter Grammar Rules

Enter grammar rules (e.g., S -> aSb). Type 'done' when finished:
Rule: S -> aSb
Rule: S -> c
Rule: done
