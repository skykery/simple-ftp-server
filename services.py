from pyftpdlib import servers
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler


class FTPServer:
    def __init__(self, user, password, port, path):
        self.user = user
        self.password = password
        self.address = ('0.0.0.0', port)
        self.handler = FTPHandler
        self.path = path or self.get_working_dir(None)
        self.set_credentials()
        self.server = servers.FTPServer(self.address, FTPHandler)

    @staticmethod
    def get_working_dir(path):
        if path:
            return path
        import pathlib
        path = pathlib.Path(__file__).parent.resolve()
        path = path / 'data'
        path.mkdir(exist_ok=True)
        return str(path)

    def set_credentials(self):
        authorizer = DummyAuthorizer()
        authorizer.add_user(self.user, self.password, self.path, perm="elradfmwMT")
        self.handler.authorizer = authorizer

    def start(self):
        self.server.serve_forever()

    def stop(self):
        self.server.close_all()

    @staticmethod
    def get_ip():
        import socket

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP


class FTPManager:
    @staticmethod
    def start(*args, **kwargs):
        FTPServer(*args, **kwargs).start()

    @staticmethod
    def get_ip():
        return FTPServer.get_ip()

    @staticmethod
    def get_path(path):
        return FTPServer.get_working_dir(path)
