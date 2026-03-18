
import os


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        common_path = os.path.commonpath([working_dir_abs, target_file])
        valid_target_dir = common_path == working_dir_abs
        if not valid_target_dir:
            rtn = f'Error: Cannot read "{file_path}" as it is outside '
            rtn += "the permitted working directory"
            return rtn

        if os.path.isdir(target_file):
            rtn = f'Error: Cannot write to "{file_path}" as it is a directory.'
            return rtn

        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, 'w') as f:
            content = f.write(content)
    except Exception as e:
        return f'Error: "{e}"'

    rtn = f'Successfully wrote to "{file_path}" ({content} characters'
    rtn += ' written)'
    return rtn
