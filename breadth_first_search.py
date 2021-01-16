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
        else:
            raise KeyError("Not supported File Types: " + ', '.join(non_supported_file_types))
        
        return route[::-1]
    
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
    
    nn.add_file_connection_from_to("png", "jpg")
    nn.add_file_connection_from_to("png", "ico")
    nn.add_file_connection_from_to("png", "gif")
    nn.add_file_connection_from_to("png", "pdf")
    
    nn.add_file_connection_from_to("jpg", "png")
    nn.add_file_connection_from_to("jpg", "ico")
    nn.add_file_connection_from_to("jpg", "gif")
    nn.add_file_connection_from_to("jpg", "pdf")
    
    nn.add_file_connection_from_to("ico", "jpg")
    nn.add_file_connection_from_to("ico", "png")
    nn.add_file_connection_from_to("ico", "gif")
    nn.add_file_connection_from_to("ico", "pdf")
    
    nn.add_file_connection_from_to("gif", "jpg")
    nn.add_file_connection_from_to("gif", "ico")
    nn.add_file_connection_from_to("gif", "png")
    nn.add_file_connection_from_to("gif", "pdf")
    
    nn.add_file_connection_from_to("pdf", "jpg")
    nn.add_file_connection_from_to("pdf", "ico")
    nn.add_file_connection_from_to("pdf", "gif")
    nn.add_file_connection_from_to("pdf", "png")
    nn.add_file_connection_from_to("pdf", "word")
    
    nn.add_file_connection_from_to("word", "pdf")
    nn.add_file_connection_from_to("word", "A2")
    nn.add_file_connection_from_to("word", "A3")
    
    nn.add_file_connection_from_to("A1", "A2")
    
    nn.add_file_connection_from_to("A2", "A1")
    nn.add_file_connection_from_to("A2", "word")
    nn.add_file_connection_from_to("A2", "A3")
    nn.add_file_connection_from_to("A2", "B1")
    
    nn.add_file_connection_from_to("A3", "word")
    nn.add_file_connection_from_to("A3", "A2")
    
    nn.add_file_connection_from_to("B1", "A2")
    nn.add_file_connection_from_to("B1", "B2")
    
    nn.add_file_connection_from_to("B2", "B1")
    nn.add_file_connection_from_to("B2", "B3")
    
    nn.add_file_connection_from_to("B3", "B2")
    
    b = BFS(nn)
    print(b.get_route("jpg", "B2"))
    
    
    
    