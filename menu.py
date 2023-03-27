import nuke
import exposeInFinder

node_classes = ["Read", "Write", "Camera1", "Camera2", "ReadGeo", "ReadGeo2", "WriteGeo"]

for node in node_classes:
    nuke.addOnUserCreate(exposeInFinder.add_expose_button, nodeClass=node)
    nuke.addKnobChanged(exposeInFinder.expose_in_finder, nodeClass=node)



