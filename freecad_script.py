import FreeCAD as App
import Part
import Draft

# Grundsätzliches Vorgehen:
# Schreibe eine Funktion für jede Aufgabe, die die benötigten Parameter entgegennimmt und das Ergebnis zurückgibt.
# printe das Ergebnis der Funktionen in der Konsole aus.

# Aufgabe1 : Erstelle eine Funktion, welches ein 3D-Modell aus einer STEP-Datei lädt, initialisere hierfür ein neues Dokument und füge das 3D-Modell hinzu.
# Verwende hierfür die App und Part-Module von FreeCAD.
def load_step_file(step_file_path):

    #Initialize the document
    doc = App.newDocument()
    doc.FileName = "example" + ".FCStd"

    #Read the step file
    # shape=Part.Shape()
    # shape.read(step_file_path)
    shape = Part.read(step_file_path)

    #Add the shape to the document
    doc.addObject("Part::Feature", "Object3D")
    doc.Object3D.Shape = shape

    return doc


# Aufgabe 2 : Erstelle eine Funktion, die die Ausdehnung des 3D-Modells in X-, Y- und Z-Richtung zurückgibt. Benutze hierfür dein Part Objekt aus Aufgabe 1.
def get_extents(doc):

    boundingBox=doc.Object3D.Shape.BoundBox
    extents = [boundingBox.XLength, boundingBox.YLength, boundingBox.ZLength]

    return extents

# Fleissaufgabe: Erstelle eine Funktion, die das 3D-Modell in eine 2D-Ansicht kollabiert. Benutze hierfür das Draft-Modul von FreeCAD.
def collapse_to_2D(doc):

    shape_2d = Draft.make_shape2dview(doc.Object3D, App.Vector(0, 0, 1))
    doc.recompute()
    objs = [doc.getObject('Shape2DView')]

    return objs


step_file_path = "/home/site/wwwroot/data/example.STEP"
doc = load_step_file(step_file_path)
extents = get_extents(doc)
objs = collapse_to_2D(doc)

print(extents, objs, doc.Object3D)


