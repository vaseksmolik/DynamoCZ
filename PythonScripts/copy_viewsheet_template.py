import sys
import clr
clr.AddReference('ProtoGeometry')
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.DesignScript.Geometry import *

#######################################
##### SCRIPT MADE BY VACLAV SMOLIK ####
#######################################
# WWW.BIMTWIN.CZ | WWW.VASEKSMOLIK.CZ #
#######################################
####### PLEASE DO NOT REMOVE ##########
####### THIS TEXT FROM SCRIPT #########
#######################################

uidoc = DocumentManager.Instance.CurrentUIDocument
doc = DocumentManager.Instance.CurrentUIDocument.Document;
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

activeviews = uidoc.ActiveView

# Input
template_scheduleView = UnwrapElement(IN[0])
name = IN[1]
activeview_R = IN[2]

if activeview_R:
	activeviews = UnwrapElement(activeview_R)

# transaction
TransactionManager.Instance.EnsureInTransaction(doc)
i = 0
for activeview in activeviews:
	if not isinstance(activeview,Autodesk.Revit.DB.ViewSheet):
		raise Exception('Input view is not viewsheet, but '+str(activeview)+ '. Please define another view or activate viewsheet.')
	
	template_definition = template_scheduleView.Definition
	
	
	target_scheduleView = ViewSchedule.CreateSchedule(doc,template_definition.CategoryId)
	target_definition = target_scheduleView.Definition
	target_grid = ScheduleSheetInstance.Create(doc,activeview.Id,target_scheduleView.Id,XYZ.Zero)
	
	target_scheduleView.HeaderTextTypeId = template_scheduleView.HeaderTextTypeId
	target_scheduleView.TitleTextTypeId = template_scheduleView.TitleTextTypeId
	target_scheduleView.BodyTextTypeId = template_scheduleView.BodyTextTypeId
	
	for field_id in template_definition.GetFieldOrder():
		field = template_definition.GetField(field_id)
		
		if field.IsHidden:
			continue
			
		for new_schedulable_field in target_definition.GetSchedulableFields():
			if field.GetSchedulableField() == new_schedulable_field:			
				new_field = target_definition.AddField(new_schedulable_field)	
				new_field.GridColumnWidth = field.GridColumnWidth	
				new_field.ColumnHeading = field.ColumnHeading

	if isinstance(name,list):
		currentname=name[i]
	else:
		currentname=name
	
	target_scheduleView.Name = activeview.SheetNumber + " - "+ currentname
	i = i+1
	
TransactionManager.Instance.TransactionTaskDone()
OUT = True
