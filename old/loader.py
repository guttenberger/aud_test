"""Load the source code for error messages."""

a = None

class SourceLoader:
    """Loaders make the source code of a module available."""
    
    def __init__(self, code):
        """Create a new loader object with code."""
        self.code = code

    def get_source(self, *args):
        """Return the source code of the module."""
        global a
        a = args
        return self.code

class FileLoader:
    """Return the source code from the file name."""
    
    def __init__(self, path):
        """Create a new loader on a path."""
        self.path = path
    
    def get_source(self, *args):
        """Return the source of the module."""
        return open(self.path).read()

