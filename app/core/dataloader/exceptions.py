class NotConnectedError(Exception):
    """Exception raised when the database is not connected.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
