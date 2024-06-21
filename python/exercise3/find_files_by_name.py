import os


def find_files_by_name(directory_path, target_filename):
    found_files = []

    if not os.path.exists(directory_path):
        return found_files

    if os.path.isfile(directory_path):
        if os.path.basename(directory_path) == target_filename:
            found_files.append(directory_path)
        return found_files

    for item in os.listdir(directory_path):
        full_item_path = os.path.join(directory_path, item)

        if os.path.isdir(full_item_path):
            found_files.extend(find_files_by_name(full_item_path, target_filename))

        elif os.path.isfile(full_item_path) and item == target_filename:
            found_files.append(full_item_path)

    return found_files


def main():
    DIRECTORY_PATH = "."
    TARGET_FILENAME = "__init__.py"

    search_results = find_files_by_name(DIRECTORY_PATH, TARGET_FILENAME)
    if search_results:
        print(f"Entries found with filename '{TARGET_FILENAME}':")
        for file_path in search_results:
            print(file_path)
    else:
        print(f"No entries found with filename '{TARGET_FILENAME}'.")


if __name__ == "__main__":
    main()
