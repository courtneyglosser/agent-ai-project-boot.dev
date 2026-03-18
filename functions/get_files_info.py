
import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        common_path = os.path.commonpath([working_dir_abs, target_dir])
        valid_target_dir = common_path == working_dir_abs
        if not valid_target_dir:
            rtn = f'Error: Cannot list "{directory}" as it is outside the'
            rtn += f'{rtn} return permitted working directory'
            return rtn

        if not os.path.isdir(target_dir):
            rtn = f'Error: "{directory}" is not a directory'
            return rtn

        if directory == ".":
            dir_name = "current"
        else:
            dir_name = f"'{directory}'"

        rtn = "Result for {dir_name} directory: \n"

        for i in os.listdir(target_dir):
            # print (f"Got item from listdir: {i}")
            filename = i
            i_test = os.path.join(working_dir_abs, directory, i)
            
            is_dir = os.path.isdir(i_test)
            size = os.path.getsize(i_test)
            # print (f" - {filename}: file_size={size}, is_dir={is_dir}")
            rtn = rtn + f" - {filename}: file_size={size}, is_dir={is_dir}\n"

        return rtn
    except Exception as e:
        return f"Error: unknown... {e}"
