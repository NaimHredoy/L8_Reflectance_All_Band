# MD SHAH NAIM HREDOY
# hridhowlader@gmail.com

# Import system modules

import arcpy
import math
from arcpy import env

# set environment
# Here you have to set your own directory

env.workspace="H:/STUDY/Document/Papers/RS02/aaaaaaa"
env.overwriteOutput=True
from arcpy.sa import *

# Checking out spatial extension 

arcpy.CheckOutExtension("Spatial")

# Setting up variables

image = arcpy.Raster("H:/STUDY/Document/Papers/RS02/aaaaaaa/LC08_L1TP_138043_20160411_20170326_01_T1_B1.TIF")
mp=0.00002
ap= -0.100000

# calculation

refl_init1= mp * image
refl_init2= refl_init1+ap
solar_elevation= math.sin(62.39412056*(math.pi/180))    #in this case the value of sun elevation varies in different satellite images.
                                                        #so, you have to check it from the metadata file (.MTL) and update it
                                                        #bsin() function will return the value in degree. if you want it in radian then erase - (math.pi/180)
reflectance= refl_init2/solar_elevation

#saving the output

reflectance.save ("H:/STUDY/Document/Papers/RS02/aaaaaaa/ref1.tif")
