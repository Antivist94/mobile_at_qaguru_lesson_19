from pathlib import Path


def abs_path_from_project(file_name):
    return str(Path(__file__).parent.joinpath(f'files/{file_name}'))
