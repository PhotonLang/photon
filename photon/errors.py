class PhotonError(Exception):
    """Base Exception raised by the language"""

class ManipulationError(PhotonError):
    """Error raised when there is a manipulation error"""

class ConfigError(PhotonError):
    """Error raised when there is a config error"""
    def __init__(self, msg: str):
        self.msg = msg
    
    def __str__(self):
        return self.msg



class RunError(PhotonError):
    """Error Raised when Photon fails to run the given query"""
    def __init__(self, msg: str):
        self.msg = msg
    
    def __str__(self):
        return self.msg