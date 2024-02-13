from pathlib import Path


def path(file_name):
    return str(Path(__file__).parent.parent.joinpath(f'homework_lecture_10/resources/{file_name}'))
