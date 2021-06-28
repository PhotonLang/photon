from io import BytesIO

class Open:
    """
    Represents a generic Open statement. Can be subclassed later to represent advanced Open statements
    """
    def __init__(self, io: BytesIO, identifier: str):
        self.io = io
        self.identifier = identifier
    

