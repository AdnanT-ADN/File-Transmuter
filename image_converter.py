from file_converter import file_converter

class image_converter(file_converter):
    
    def __init__(self):
        super().__init__()
    
    def convert_file(self, target_file_path: str, destination_file_path: str) -> None:
        target_file_path, destination_file_path = self._format_path(target_file_path, destination_file_path)
        if self._check_file_exist(target_file_path):
            target_file_type, desired_file_type = self._get_file_types_from_paths(target_file_path, destination_file_path)
            
        else:
            raise FileNotFoundError("Path " + target_file_path + " is not a file")
        