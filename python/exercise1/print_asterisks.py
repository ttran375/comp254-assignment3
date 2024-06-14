def print_asterisks(n, current=1):
    return (
        None
        if current > n
        else (
            print("*" * current)
            or print_asterisks(n, current + 1)
            or (current != n and print("*" * current))
        )
    )


def main():
    max_stars = int(input("Enter the number of asterisks of the maximum line: "))
    print_asterisks(max_stars)


if __name__ == "__main__":
    main()
