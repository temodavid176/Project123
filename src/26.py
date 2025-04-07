import os
import shutil

def copy_files():
    source_dir = 'Project123'
    destination_dir = 'dist'

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    files_to_copy = os.listdir(source_dir)
    
    for file in files_to_copy:
        src_file_path = os.path.join(source_dir, file)
        dst_file_path = os.path.join(destination_dir, f"{file}")
        
        shutil.copy(src_file_path, dst_file_path)
