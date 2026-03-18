
import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        common_path = os.path.commonpath([working_dir_abs, target_file])
        valid_target_dir = common_path == working_dir_abs
        if not valid_target_dir:
            rtn = f'Error: Cannot read "{file_path}" as it is outside '
            rtn += "the permitted working directory"
            return rtn

        
        if not os.path.isfile(target_file):
            rtn = 'Error: File not found or is not a regular file: '
            rtn +=f'"{file_path}"'
            return rtn

        with open(target_file, 'r') as f:
            content = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f'Error: "{e}"'

    return content

