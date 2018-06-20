"""This module runs the code in the code window."""

import sys
import traceback
from browser import document
import output
from test_code import test_code


# UI elements
textArea = document.getElementById("source-code-text")
executeButton = document.getElementById("execute-button")

executions = 0
def run_code(*args):
    """Run the code in the text field."""
    global executions
    try:
        executions += 1
        name = "run{}".format(executions)
        output.clear()
        code = textArea.value
        globals = {
            "__name__": name,
            "__file__": name + ".py",
        }
        exec(code, globals)
        test_code(globals)
    except:
        traceback.print_exc(file=sys.stderr)

executeButton.bind("click", run_code)

def capture_control_enter_and_run_code(event):
    """Run the code by pressing Control + Enter."""
#    print(event.charCode, event.ctrlKey)
    if event.charCode == 0 and event.ctrlKey:
        run_code()

# see https://www.brython.info/static_doc/en/keyboard_events.html
textArea.bind("keypress", capture_control_enter_and_run_code)
    


