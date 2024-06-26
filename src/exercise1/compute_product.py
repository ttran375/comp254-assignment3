def compute_product(m, n):
    """
    Computes the product of two positive integers using only addition and recursion.
    """
    return (
        # Base case: If n is 0, the product is 0
        0 if n == 0

        # Recursive case: Add m to the product of m and (n-1)
        else m + compute_product(m, n - 1)
    )
