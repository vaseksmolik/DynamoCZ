# This script was created as a part of package DynamoCZ
# More at http://en.vaseksmolik.cz
#
# INPUT : IN[0] = room or space
# OUTPUT : OUT = elements of boundary segments (e.g. Wall)

import sys
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument;

DYNroom = IN[0]
room = DYNroom.InternalElement
opt = SpatialElementBoundaryOptions()
bounds = room.GetBoundarySegments(opt)
elements = []
for innerlist in bounds :
	for bound in innerlist :
		elements.append(doc.GetElement(bound.ElementId))

OUT = elements
