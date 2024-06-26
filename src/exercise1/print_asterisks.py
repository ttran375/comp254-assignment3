def print_asterisks(n, current=1):
    """
    Prints a pattern of asterisks using recursion.
    """
    return (
        # Base case: If the current line number exceeds n, terminate the recursion
        None
        if current > n
        else (
            # Print asterisks for the current line
            print("*" * current)
            # Recursive call to print the next line
            or print_asterisks(n, current + 1)
            # Print the current line again after the recursion
            or (current != n and print("*" * current))
        )
    )
