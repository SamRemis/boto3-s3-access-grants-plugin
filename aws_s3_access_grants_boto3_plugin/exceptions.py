#Why use this instead of the built in Value Error and
class IllegalArgumentException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


#Is there a built in exception here that may be appropriate? https://docs.python.org/3/library/exceptions.html
class UnsupportedOperationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
