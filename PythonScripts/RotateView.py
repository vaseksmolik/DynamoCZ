import clr 
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import ToDSType (bool) extension method 
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

from System.Collections.Generic import *

# Import RevitAPI 
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import ReferencePointArray

view = UnwrapElement(IN[0])
vector = IN[1].ToRevitType()


doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application


TransactionManager.Instance.EnsureInTransaction(doc)
#apply lineweight override to elements in an input list
view.OrientTo(vector)
# "End" the transaction
TransactionManager.Instance.TransactionTaskDone()
uiapp.ActiveUIDocument.RefreshActiveView()

OUT = doc.ActiveView
