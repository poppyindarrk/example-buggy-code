import os

def find_files(directory, extension):
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matches.append(file)  # Bug: Should append the full path
    return matches

print(find_files('/path/to/search', '.py'))
