from node_network import node_network
from breadth_first_search import BFS

def create_network(config_file_path="./Configurations/network_configuration.csv"):
    nn = node_network()
    with open(config_file_path, "r") as config_file:
        fields = config_file.readline().split(",") # converstion_type, read_write_permission, file_type
        
        read_permission = []
        write_permission = []
        read_write_permission = []
        
        converstion_type =  ""
        
        for line in config_file:
            ct, rwp, ft = line.split(",")
            ft = ft.replace("\n", "")
            
            if converstion_type == "":
                converstion_type = ct
            
            if converstion_type != ct:
                # pass # apply current network, then reset and add curent
                # add file type node to network
                
                nn = update_node_network(nn, read_write_permission, read_permission, write_permission, converstion_type)
                
                # Do not do anything for the write ones as they wont connect to anything
                
                # Reset lists
                read_permission = []
                write_permission = []
                read_write_permission = []
                converstion_type = ct
            
            if rwp == "read_and_write":
                read_write_permission.append(ft)
            elif rwp == "readable_only":
                read_permission.append(ft)
            elif rwp == "writable_only":
                write_permission.append(ft)
            else:
                raise ValueError("Value " + rwp + " is unknown")
    nn = update_node_network(nn, read_write_permission, read_permission, write_permission, converstion_type)
    return nn

def update_node_network(nn: node_network, read_write_permission: list, read_permission: list, write_permission: list, converstion_type: str) -> node_network:
    for file_type in iter(read_write_permission + write_permission + read_permission):
        try:
            nn.add_file_type(file_type)
        except KeyError:
            pass
    # Create connections between read and write nodes
    for file_type_from in (x for x in read_write_permission):
        for file_type_to in (y for y in read_write_permission):
            if file_type_to == file_type_from:
                continue
            else:
                nn.add_file_connection_from_to(file_type_from, file_type_to, converstion_type)
    
    # Create connections between read nodes
    for file_type_from in (x for x in read_permission):
        for file_type_to in (y for y in read_write_permission + write_permission):
            nn.add_file_connection_from_to(file_type_from, file_type_to, converstion_type)
    
    return nn

if __name__ == "__main__":
    N = create_network()
    bfs = BFS(N)
    print(bfs.get_route("png", "jpeg 2000"))