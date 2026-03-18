

import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        common_path = os.path.commonpath([working_dir_abs, target_file])
        valid_target_dir = common_path == working_dir_abs
        if not valid_target_dir:
            rtn = f'Error: Cannot execute "{file_path}" as it is outside '
            rtn += "the permitted working directory"
            return rtn

        
        if not os.path.isfile(target_file):
            rtn = 'Error: File not found or is not a regular file: '
            rtn +=f'"{file_path}" does not exist'
            return rtn

        if not file_path.endswith('.py'):
            rtn = f'Error: "{file_path}" is not a Python file'
            return rtn

        command = ["python", target_file]
        if args is not None:
            for arg in args:
                command.extend(arg)

        completed_process = subprocess.run(command, capture_output=True,
            cwd=working_directory,  text=True, timeout=30)

        rtn = ""
        rtn_code = completed_process.returncode
        if rtn_code != 0:
            rtn += f"Process exited with code {rtn_code}\n"

        rtn_stdout = completed_process.stdout
        rtn_stderr = completed_process.stderr

        if not rtn_stdout and not rtn_stderr:
            rtn += "No output produced\n"
        else:
            rtn += f"STDOUT: {rtn_stdout}\n"
            rtn += f"STDERR: {rtn_stderr}\n"
        
        return rtn

    except Exception as e:
        return f'Error: executing Python file: {e}'


