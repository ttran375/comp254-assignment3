def compute_product(m, n):
    return 0 if n == 0 else m + compute_product(m, n - 1)


def main():
    m = 4
    n = 2
    result = compute_product(m, n)
    print(result)


if __name__ == "__main__":
    main()
