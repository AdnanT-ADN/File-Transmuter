class node_network:
    
    class _Node:
        
        def __init__(self):
            self._connected_file_types = []
        
        def add_file_connection(self, file_type: str):
            if file_type not in self._connected_file_types:
                self._connected_file_types.append(file_type)
        
        @property
        def connected_file_types(self):
            """ Returns generator of all connected file type names"""
            return (x for x in self._connected_file_types)
    
    def __init__(self):
        self._file_types = {}
    
    def add_file_type(self, file_type: str) -> None:
        if file_type in self._file_types.keys():
            raise Exception("File type already exists in the network")
        else:
            self._file_types[file_type] = self._Node()
    
    def get_nodes_connected_to(self, file_type: str):
        """ Returns generator of all connected file types for a specific node """
        if file_type not in self._file_types.keys():
            raise KeyError("File type does not exist in the network")
        else:
            return self._file_types[file_type].connected_file_types
    
    def get_file_types_in_network(self):
        """ Returns generator """
        return (x for x in self._file_types.keys())
    
    def add_file_connection_from_to(self, file_type_from: str, file_type_to: str) -> None:
        # TODO check file type from and to are in the network
        self._file_types[file_type_from].add_file_connection(file_type_to)