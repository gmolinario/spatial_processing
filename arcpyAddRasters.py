###########################################################
###########################################################
# This script simply adds rasters into 1. 

# Giuseppe Molinario 

# Import  modules
import arcpy
from arcpy import env
from arcpy.sa import *
import os

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

# Set environment 
# root folder
rootFolder= r"Z:\Giuseppe\PhD\GFC\GFC_2000_2016\Mosaic\DRC\Only_2015_reclass"

# Insert path to raster to snap to 
tempEnvironment0 = arcpy.env.snapRaster
arcpy.env.snapRaster = r"C:\Data_Molinario\Temp\LFT_local\16th_run\2014\Master\DRC_2014_final.tif"

env.workspace=r"Z:\Giuseppe\PhD\GFC\GFC_2000_2016\Mosaic\DRC\Only_2015_reclass"
outRas=Raster("DRC_2014_final.tif")+Raster("Hansen_GFC2016_lossyear_Mosaic_DRC_sin_v3_2015_60m.tif")

outName="DRC_2015_to_reclass.tif"
print env.workspace
print rootFolder+"\\"+outName
outRas.save(rootFolder+"\\"+outName)

