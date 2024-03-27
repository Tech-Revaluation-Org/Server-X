from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Define anonymous access
authorizer = DummyAuthorizer()
authorizer.add_anonymous("/")

# Create FTP handler and server
handler = FTPHandler
handler.authorizer = authorizer

# Server address and port
server = FTPServer(("0.0.0.0", 21), handler)

# Start  FTP server
server.serve_forever()
