from xmlrpc.client import ServerProxy

if __name__ == '__main__':
    # initialize server
    server = ServerProxy("http://127.0.0.1:8888")

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    # invoke server
    server_output = server.sum(x,y)

    print(f'The sum of {x} and {y} is {server_output}')