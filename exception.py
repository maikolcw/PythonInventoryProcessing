class InvalidDataError(Exception):
    """Represents an InvalidDataError"""
    def __init__(self, message):
        super().__init__("InvalidDataError -")
        self.message = message
