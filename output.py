# change the stdout and stderr
import sys
from browser import document
from loader import FileLoader
__loader__ = FileLoader(__file__)

outputElement = document.getElementById("output")

class OutputToHTML:
    """A file interface for Output."""
    
    def __init__(self, cls):
        """Create an output object with a css class for styling."""
        self.cls = cls
        
    def write(self, string):
        """Write a new string to the output."""
        element = document.createElement("pre")
        element.classList.add(self.cls)
        element.innerText = string
        outputElement.appendChild(element)
    
    def flush(self):
        """Does nothing.
        
        Fixes:
        - AttributeError: '_WritelnDecorator' object has no attribute 'flush'
          see https://pythonhosted.org/gchecky/unittest-pysrc.html#_WritelnDecorator.__getattr__
        """

def capture():
    """Capture the output."""
    sys.stdout = stdout = OutputToHTML("stdout")
    sys.stderr = stderr = OutputToHTML("stderr")
    return stdout, stderr

def clear():
    """Remove all previous output."""
    outputElement.innerHTML = ""

