import re
from collections import defaultdict

def main():
    grammar = defaultdict(list)
    stored_grammar = defaultdict(list)

    while True:
        print("\n=== Recursive Descent Parser ===")
        print("1 - Enter Grammar Rules")
        print("2 - Check if Grammar is Simple")
        print("3 - Validate a Sequence")
        print("4 - Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            grammar.clear()
            print("Enter grammar rules (e.g., S -> aSb). Type 'done' when finished:")
            while True:
                rule = input("Rule: ").strip()
                if rule.lower() == "done":
                    break

                parts = [part.strip() for part in rule.split("->")]
                if len(parts) != 2:
                    print("Invalid rule format. Try again.")
                    continue

                non_terminal, production = parts
                grammar[non_terminal].append(production)

            # Store the entered grammar rules
            stored_grammar.clear()
            for key, value in grammar.items():
                stored_grammar[key] = value[:]

        elif choice == '2':
            if not stored_grammar:
                print("No grammar rules have been entered. Please enter grammar rules first.")
            elif is_simple_grammar(stored_grammar):
                print("The grammar is Simple.")
            else:
                print("The grammar is NOT Simple.")

        elif choice == '3':
            if not stored_grammar:
                print("No grammar rules have been entered. Please enter grammar rules first.")
                continue
            if not is_simple_grammar(stored_grammar):
                print("Grammar is not Simple. Please define a Simple Grammar first.")
                continue

            sequence = input("Enter the sequence to validate: ").strip()
            parse_tree = []
            if validate_sequence(stored_grammar, "S", sequence, parse_tree):
                print("The sequence is Accepted.")
                print("Parse Tree:")
                draw_parse_tree(parse_tree)
            else:
                print("The sequence is Rejected.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Try again.")

def is_simple_grammar(grammar):
    for non_terminal, productions in grammar.items():
        first_terminals = set()
        for production in productions:
            if not production or production[0].isupper():
                return False
            first_char = production[0]
            if first_char in first_terminals:
                return False
            first_terminals.add(first_char)
    return True

def validate_sequence(grammar, start_non_terminal, sequence, parse_tree):
    transition_table = build_transition_table(grammar)
    sequence += "$"
    stack = ["$", start_non_terminal]
    index = 0
    parse_tree.append((start_non_terminal, []))
    tree_stack = [parse_tree[-1][1]]

    while stack:
        top = stack.pop()
        current_symbol = sequence[index] if index < len(sequence) else "$"

        if top not in transition_table or current_symbol not in transition_table[top]:
            return False

        action = transition_table[top][current_symbol]

        if action == "Accept":
            return True
        elif action == "POP, ADVANCE":
            print(f"POP({current_symbol})")
            index += 1
        elif action.startswith("REP("):
            to_push = action[4:-1]
            print(f"REP({top} -> {to_push})")
            current_subtree = tree_stack.pop()
            for symbol in reversed(to_push):
                stack.append(symbol)
                new_node = (symbol, [])
                current_subtree.append(new_node)
                if not symbol.islower():
                    tree_stack.append(new_node[1])
        else:
            return False

    return False

def build_transition_table(grammar):
    table = defaultdict(lambda: defaultdict(lambda: "Reject"))

    for non_terminal, productions in grammar.items():
        for production in productions:
            first_terminal = production[0]
            table[non_terminal][first_terminal] = f"REP({production})"

    terminals = get_terminals(grammar)
    for terminal in terminals:
        table[terminal][terminal] = "POP, ADVANCE"

    table["$"]["$"] = "Accept"

    return table

def get_terminals(grammar):
    terminals = set()
    for productions in grammar.values():
        for production in productions:
            terminals.update(c for c in production if c.islower())
    return terminals

def draw_parse_tree(parse_tree, indent=0):
    for node, children in parse_tree:
        print("  " * indent + node)
        draw_parse_tree(children, indent + 1)

if __name__ == "__main__":
    main()