import arcpy
import describer

arcpy.env.workspace = r"C:\Users\AMarinelli\Documents\ArcGIS\Default.gdb"

desc = arcpy.Describe('Park_boundary_1')

D = describer.Desc()


# Will return list with all valid properties

properties = D.find_properties(desc)
for prop in properties:
    print(prop)


print("\n|----------------------|")
print("|----------------------|\n")


# Will print property and retrieved value

D.pretty_properties(desc)
