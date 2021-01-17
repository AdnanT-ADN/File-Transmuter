from queue import Queue
from node_network import node_network

class BFS:
    
    def __init__(self, network: node_network):
        self._queue = Queue()
        self._network = network
        self._bfs_table = {}
    
    def _init_bfs_table(self) -> None:
        for file_type in self._network.get_file_types_in_network():
            self._bfs_table[file_type] = {
                "node_visited": False,
                # "distance_travled": 0,
                "from_node": ""
            }
    
    def get_route(self, init_point: str, destination_point: str):
        route = []
        self._rest_variables()
        init_point, destination_point = init_point.upper(), destination_point.upper()
        file_types_supported, non_supported_file_types = self._network.check_file_types_in_network(init_point, destination_point)
        if file_types_supported:
            # Set start point
            self._queue.put(init_point)
            self._bfs_table[init_point] = {
                "node_visited": True,
                # "distance_traveled": 0,
                "from_node": init_point
            }
            
            # Find Paths
            queued_items = [init_point]
            while not self._bfs_table[destination_point]["node_visited"] and not self._queue.empty():
                # Set current file type
                current_file_type = self._queue.get()
                current_node = self._network.get_nodes_connected_to(current_file_type)
                # Set nodes visited and distance
                for file_type in self._network.get_nodes_connected_to(current_file_type):
                    if not self._bfs_table[file_type]["node_visited"]:
                        self._bfs_table[file_type] = {
                            "node_visited": True,
                            # "distance_traveled": 
                            "from_node": current_file_type
                        }
                    if file_type not in queued_items:
                        self._queue.put(file_type)
                        queued_items.append(file_type)
            # Return connected path as a list
            if self._bfs_table[destination_point]["from_node"] != "":
                # There is a route
                route = [destination_point]
                current_file_type = destination_point
                while current_file_type != init_point:
                    route.append(self._bfs_table[current_file_type]["from_node"])
                    current_file_type = self._bfs_table[current_file_type]["from_node"]
            
            # Format Route
            formatted_route = []
            i = 0
            route.reverse()
            while i < len(route):
                if i + 1 < len(route):
                    file_type_1 = route[i]
                    file_type_2 = route[i + 1]
                    common_format = list(set(self._network.get_converstion_types(file_type_1)).intersection(set(self._network.get_converstion_types(file_type_2))))[0]
                    formatted_route.append((file_type_1, file_type_2, common_format))
                i += 1
            route = formatted_route
        else:
            raise KeyError("Not supported File Types: " + ', '.join(non_supported_file_types))
        
        return route
    
    def _rest_variables(self) -> None:
        self._queue = Queue()
        self._bfs_table = {}
        self._init_bfs_table()

if __name__ == "__main__":
    nn = node_network()
    
    # nn.add_file_type("1")
    # nn.add_file_type("2")
    # nn.add_file_type("3")
    # nn.add_file_type("4")
    # nn.add_file_type("5")
    # nn.add_file_type("6")
    # nn.add_file_type("7")
    
    # nn.add_file_connection_from_to("1", "3")
    # nn.add_file_connection_from_to("1", "2")
    
    # nn.add_file_connection_from_to("2", "1")
    # nn.add_file_connection_from_to("2", "3")
    # nn.add_file_connection_from_to("2", "4")
    
    # nn.add_file_connection_from_to("3", "1")
    # nn.add_file_connection_from_to("3", "2")
    # nn.add_file_connection_from_to("3", "5")
    
    # nn.add_file_connection_from_to("4", "2")
    
    # nn.add_file_connection_from_to("5", "3")
    # nn.add_file_connection_from_to("5", "6")
    # nn.add_file_connection_from_to("5", "7")
    
    # nn.add_file_connection_from_to("6", "5")
    # nn.add_file_connection_from_to("6", "7")
    
    # nn.add_file_connection_from_to("7", "5")
    # nn.add_file_connection_from_to("7", "6")
    
    # b = BFS(nn)
    # print(b.get_route("3", "7"))
    
    nn.add_file_type("png")
    nn.add_file_type("jpg")
    nn.add_file_type("ico")
    nn.add_file_type("gif")
    nn.add_file_type("pdf")
    nn.add_file_type("word")
    nn.add_file_type("A1")
    nn.add_file_type("A2")
    nn.add_file_type("A3")
    nn.add_file_type("B1")
    nn.add_file_type("B2")
    nn.add_file_type("B3")
    
    nn.add_file_connection_from_to("png", "jpg", "image")
    nn.add_file_connection_from_to("png", "ico", "image")
    nn.add_file_connection_from_to("png", "gif", "image")
    nn.add_file_connection_from_to("png", "pdf", "image")
    
    nn.add_file_connection_from_to("jpg", "png", "image")
    nn.add_file_connection_from_to("jpg", "ico", "image")
    nn.add_file_connection_from_to("jpg", "gif", "image")
    nn.add_file_connection_from_to("jpg", "pdf", "image")
    
    nn.add_file_connection_from_to("ico", "jpg", "image")
    nn.add_file_connection_from_to("ico", "png", "image")
    nn.add_file_connection_from_to("ico", "gif", "image")
    nn.add_file_connection_from_to("ico", "pdf", "image")
    
    nn.add_file_connection_from_to("gif", "jpg", "image")
    nn.add_file_connection_from_to("gif", "ico", "image")
    nn.add_file_connection_from_to("gif", "png", "image")
    nn.add_file_connection_from_to("gif", "pdf", "image")
    
    nn.add_file_connection_from_to("pdf", "jpg", "image")
    nn.add_file_connection_from_to("pdf", "ico", "image")
    nn.add_file_connection_from_to("pdf", "gif", "image")
    nn.add_file_connection_from_to("pdf", "png", "image")
    nn.add_file_connection_from_to("pdf", "word", "document")
    
    nn.add_file_connection_from_to("word", "pdf", "document")
    nn.add_file_connection_from_to("word", "A2", "document")
    nn.add_file_connection_from_to("word", "A3", "document")
    
    nn.add_file_connection_from_to("A1", "A2", "document")
    
    nn.add_file_connection_from_to("A2", "A1", "document")
    nn.add_file_connection_from_to("A2", "word", "document")
    nn.add_file_connection_from_to("A2", "A3", "document")
    nn.add_file_connection_from_to("A2", "B1", "b-type")
    
    nn.add_file_connection_from_to("A3", "word", "document")
    nn.add_file_connection_from_to("A3", "A2", "document")
    
    nn.add_file_connection_from_to("B1", "A2", "document")
    nn.add_file_connection_from_to("B1", "B2", "b-type")
    
    nn.add_file_connection_from_to("B2", "B1", "b-type")
    nn.add_file_connection_from_to("B2", "B3", "b-type")
    
    nn.add_file_connection_from_to("B3", "B2", "b-type")
    
    b = BFS(nn)
    # print(b.get_route("jpg", "B2"))
    # print(b.get_route("jpg", "A1"))
    
    
    
    