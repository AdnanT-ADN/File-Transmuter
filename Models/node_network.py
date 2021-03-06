import array
class node_network:
    __slots__ = ["_file_types"]
    class _Node:
        __slots__ = ["_connected_file_types", "_converstion_types"]
        
        def __init__(self):
            self._connected_file_types = []
            self._converstion_types = []
        
        def add_file_connection(self, file_type: str, converstion_type: str):
            if file_type not in self._connected_file_types:
                self._connected_file_types.append(file_type)
                if converstion_type not in self._converstion_types:
                    self._converstion_types.append(converstion_type)
        
        @property
        def connected_file_types(self):
            """ Returns generator of all connected file type names"""
            return (x for x in self._connected_file_types)
        
        @property
        def converstion_types(self) -> list:
            return self._converstion_types
    
    def __init__(self):
        self._file_types = {}
    
    def add_file_type(self, file_type: str) -> None:
        if file_type in self._file_types:
            raise KeyError("File type already exists in the network")
        else:
            self._file_types[file_type] = self._Node()
    
    def get_nodes_connected_to(self, file_type: str):
        """ Returns generator of all connected file types for a specific node """
        if file_type not in self._file_types:
            raise KeyError("File type does not exist in the network")
        else:
            return self._file_types[file_type].connected_file_types
    
    def get_file_types_in_network(self):
        """ Returns generator """
        return (x for x in self._file_types)
    
    def add_file_connection_from_to(self, file_type_from: str, file_type_to: str, converstion_type: str) -> None:
        file_types_supported, non_supported_file_types = self.check_file_types_in_network(file_type_from, file_type_to)
        if file_types_supported:
            self._file_types[file_type_from].add_file_connection(file_type_to, converstion_type)
        else:
            raise KeyError("Not supported File Types: " + ', '.join(non_supported_file_types))
    
    def check_file_types_in_network(self, *file_types: str) -> (bool, list):
        is_present = True
        non_present_file_types = []
        for file_type in file_types:
            if file_type not in self._file_types:
                is_present = False
                non_present_file_types.append(file_type)
        return is_present, non_present_file_types
    
    def get_converstion_types(self, file_type: str) -> list:
        file_types_supported, non_supported_file_types = self.check_file_types_in_network(file_type)
        if file_types_supported:
            return self._file_types[file_type].converstion_types
        else:
            raise KeyError("Not supported File Types: " + ', '.join(non_supported_file_types))