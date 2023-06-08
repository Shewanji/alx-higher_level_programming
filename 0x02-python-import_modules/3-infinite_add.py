#!/usr/bin/python3

if __name__ == "__main__":
    """Add all command-line arguments."""
    import sys

    # Skip the first element (script name)
    arguments = sys.argv[1:]

    # Initialize total to 0
    total = 0

    # Iterate over each argument and add it to the total
    for arg in arguments:
        total += int(arg)

    # Print the result
    print(total)
