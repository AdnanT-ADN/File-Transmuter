import os.path as pathlib

class file_converter:
    
    def __init__(self):
        self._writable_file_types = []
        self._readable_file_types = []
    
    def _check_file_exist(self, *file_paths: str) -> bool:
        """ Returns True if a file exists else False """
        files_exist = True
        for file_path in file_paths:
            if not pathlib.isfile(file_path):
                files_exist = False
        return files_exist
    
    def _format_path(self, *paths: str) -> str:
        x = []
        for path in paths:
            a = path.replace("\\", "/")
            a = a.replace("//", "/")
            x.append(a)
        return tuple(x)
    
    def _get_file_types_from_paths(self, *paths: str) -> str:
        return tuple([path.split(".")[-1] for path in paths])