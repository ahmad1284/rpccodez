from xmlrpc.server import SimpleXMLRPCServer

# Define your function
def sum_of_two(x,y):
    return x + y

if __name__ == '__main__':
    # initialize the server at localhost and port 8888
    server = SimpleXMLRPCServer(('localhost',8888))
    
    # register another function
    server.register_function(sum_of_two, "sum")

    print("Listening for Client")

    # keep waiting for calls
    server.serve_forever()