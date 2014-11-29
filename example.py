import describer

desc = r"C:\Users\AMarinelli\Documents\ArcGIS\Default.gdb\Park_boundary_1"

D = describer.Desc()



# Usage-1
# Will return list with all valid properties

properties = D.find_properties(desc)

for prop in properties:
    print(prop)


print("\n|----------------------|\n")



# Usage-2
# Will print property and returned value

D.pretty_properties(desc)
