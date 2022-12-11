from xmlrpc.server import SimpleXMLRPCServer

def respon_string(str):
    return "Here is your string: %s"%str

def sum_of_two(x,y):
    return x + y

if __name__ == '__main__':
    # initialize the server at localhost and port 8888
    server = SimpleXMLRPCServer(('0.0.0.0',8888))
    # register function
    server.register_function(respon_string, "get_string")
    
    # register another function
    server.register_function(sum_of_two, "sum")

    print("Listening for Client")

    # keep waiting for calls
    server.serve_forever()