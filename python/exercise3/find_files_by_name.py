import os


def find_files_by_name(path, filename):
    results = []

    if not os.path.exists(path):
        return results

    if os.path.isfile(path):
        if os.path.basename(path) == filename:
            results.append(path)
        return results

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)

        if os.path.isdir(full_path):
            results.extend(find_files_by_name(full_path, filename))

        elif os.path.isfile(full_path) and entry == filename:
            results.append(full_path)

    return results


if __name__ == "__main__":
    path = "."  # Replace with an actual path on your filesystem
    filename = "__init__.py"  # Replace with an actual filename you want to search for

    results = find_files_by_name(path, filename)
    if results:
        print(f"Entries found with filename '{filename}':")
        for entry in results:
            print(entry)
    else:
        print(f"No entries found with filename '{filename}'.")
