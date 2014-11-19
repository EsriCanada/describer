import arcpy
import describer

arcpy.env.workspace = r"C:\Users\AMarinelli\Documents\ArcGIS\Default.gdb"

desc = arcpy.Describe('Park_boundary_1')

D = describer.Desc()


# Will return list with all valid properties because a second
# parameter is not supplied (default is False).

properties = D.find_properties(desc)
for prop in properties:
    print(prop)


print("\n|----------------------|")
print("|----------------------|\n")


# Will return dictionary with property as the key and the evaluated property
# attribute for the desc object. Uses second parameter of True.

properties = D.find_properties(desc, True)
for prop, value in sorted(properties.items()):
    print(str(prop), ":", str(value))
