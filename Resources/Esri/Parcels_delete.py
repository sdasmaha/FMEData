# ---------------------------------------------------------------------------
# CityDataTruncateParcels.py
# This uses the new arcpy library for ArcGIS 10.0 and higher only. 
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import arcpy 
import sys, string, os

# Load required toolboxes...pick the ones from the appropriate Program Files directory
#arcpy.AddToolbox("C:/Program Files/ArcGIS/Desktop10.2/ArcToolbox/Toolboxes/Data Management Tools.tbx")
arcpy.AddToolbox("C:/Program Files (x86)/ArcGIS/Desktop10.2/ArcToolbox/Toolboxes/Data Management Tools.tbx")


# Local variables...
Geodb_parcels = "C:\\FME Training\\ESRI\\Resources\\VancouverCity.gdb\\Property\\Parcels"
Geodb_parcel_ids = "C:\\FMEData2014\\ESRI\\Resources\\VancouverCity.gdb\\Property\\Parcel_Ids"

# Process: Delete Rows...
arcpy.DeleteRows_management(Geodb_parcels)
arcpy.DeleteRows_management(Geodb_parcel_ids)
