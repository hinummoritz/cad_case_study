import FreeCAD as App
import Part
import Draft
import Points
#For local testing


def load_step_file(step_file_path):

    #Initialize the document
    doc = App.newDocument()
    doc.FileName = "example" + ".FCStd"

    #Read the step file
    shape=Part.Shape()
    shape.read(step_file_path)

    #Add the shape to the document
    doc.addObject("Part::Feature", "Object3D")
    doc.Object3D.Shape = shape

    return doc


def get_extents(doc):

    boundingBox=doc.Object3D.Shape.BoundBox
    extents = [boundingBox.XLength, boundingBox.YLength, boundingBox.ZLength]

    return extents

    
def collapse_to_2D(doc):

    shape_2d = Draft.make_shape2dview(doc.Object3D, App.Vector(0, 0, 1))
    doc.recompute()
    objs = [doc.getObject('Shape2DView')]

    return objs


step_file_path = "/home/site/wwwroot/data/example.STEP"
doc = load_step_file(step_file_path)
extents = get_extents(doc)

print(extents)


