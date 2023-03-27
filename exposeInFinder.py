import nuke
import os
import sys
import subprocess
# custom button:
def add_expose_button():
    node = nuke.thisNode()
    button_expose = nuke.PyScript_Knob("exposeInFinder", "expose in finder", "")
    tab_custom = nuke.Tab_Knob("custom", "custom")
    node.addKnob(tab_custom)
    node.addKnob(button_expose)


def expose_in_finder():
    node = nuke.thisNode()
    knob = nuke.thisKnob()

    if knob.name() == "exposeInFinder":
        path = os.path.dirname(node["file"].getValue())
        if os.path.isdir(path):
            open_folder(path)
        else:
            nuke.message("Can't expose in finder")

def open_folder(path):
    if sys.platform == 'win32':
        subprocess.check_call(["explorer", path])







