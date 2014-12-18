import describer

desc = r"C:\Users\AMarinelli\Documents\ArcGIS\Default.gdb\Park_boundary_1"

D = describer.Desc()



# Usage 1
# Will return python list with all valid properties

properties = D.find_properties(desc)

print properties

for prop in properties:
    print(prop)



# Usage 2
# Will print all available properties and their returned value(s)

D.pretty_properties(desc)
