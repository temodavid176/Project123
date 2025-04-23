import os

def create_directory(directory_path):
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"Directory created: {directory_path}")
        else:
            print(f"Directory already exists at path: {directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_files(directory_path):
    files = []
    for root, dirs, files in os.walk(directory_path):
        files.extend([os.path.join(root, f) for f in files])
    return files

# Example usage
directory_path = "/path/to/your/directory"
create_directory(directory_path)
print(list_files(directory_path))
