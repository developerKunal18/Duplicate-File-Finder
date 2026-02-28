import os

folder_path = input("Enter folder path: ")

files = {}
duplicates = []

for file in os.listdir(folder_path):
    full_path = os.path.join(folder_path, file)

    if os.path.isfile(full_path):
        size = os.path.getsize(full_path)

        if size in files:
            duplicates.append((file, files[size]))
        else:
            files[size] = file

if duplicates:
    print("\nDuplicate files found:")
    for file1, file2 in duplicates:
        print(f"{file1} and {file2}")
else:
    print("No duplicate files found.")
