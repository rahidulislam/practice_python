import os

def list_files(path,extension=None):
    """ List all files in a directory specified by path
    Args:
        path - the root directory path
        extensions - a iterator of file extensions to include, pass None to get all files.
    Returns:
        A list of files specified by extensions
    """
    filepaths=[]
    for root,_,files in os.walk('/media/rahidulislam/Personal/Work/practice_python/practice_python'):
        for file in files:
            if extension is None:
                filepaths.append(os.path.join(root,file))
            else:
                for ext in extension:
                    if file.endswith(ext):
                        filepaths.append(os.path.join(root,file))
    return filepaths

if __name__ == "__main__":
    filepaths = list_files('/media/rahidulislam/Personal/Work/practice_python/practice_python',('.csv',))
    for file_path in filepaths:
        print(file_path)
        
