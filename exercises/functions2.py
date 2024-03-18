import os


def getListofRawFiles(dir_path):
    """
    ## Original function that we have seen in the slides
    """
    dirs = [x[0] for x in os.walk(dir_path)]
    raw_files = []
    for mypath in dirs:
        all_raw_files = [fileName for fileName in os.listdir(mypath) if fileName.endswith(".raw")]
        for raw_file in all_raw_files:
            raw_files.append(os.path.join(mypath, raw_file))
    return raw_files

'''
My Solution below
'''
def get_raw_file_names_in_dir(dir_path: str) -> list:
    return [fileName for fileName in os.listdir(dir_path) if fileName.endswith(".raw")]

def get_raw_file_paths(dir_path: str) -> list:
    return [os.path.join(dir_path, fileName) for fileName in get_raw_file_names_in_dir(dir_path)]

def getListofRawFiles(dir_path: list) -> list:
    dir_list = [x[0] for x in os.walk(dir_path)]
    raw_files = []
    for dir_path in dir_list:
        raw_files += get_raw_file_paths(dir_path)
    return raw_files