## Describer

Describer is an attempt to make the [Describe (arcpy)](http://resources.arcgis.com/en/help/main/10.1/index.html#/Describe/018v00000066000000/) function more user friendly by displaying all the valid properties you have access to based on the input data type.

For example, describing a geodatabase feature class means you have access to [several properties](http://resources.arcgis.com/en/help/main/10.1/index.html#/FeatureClass_properties/018v00000011000000/).  You can also use the properties available [GDB FeatureClass properties](http://resources.arcgis.com/en/help/main/10.1/index.html#/GDB_FeatureClass_properties/018v0000005t000000/) and so on.  This means you must navigate multiple resource pages to determine which properties are available for any given input.

Describer uses the hasattr(object, name) python built-in function to find all
the valid properties for a given describe object.  This trick is already hinted at in the ArcGIS documentation:

>If you try to access a property that a Describe object does not have, it will either throw an error or return an empty value (None, 0 or -1, or empty string). If you are uncertain of a particular property, you can use Python's **hasattr()** function to check.

### Example

```
import arcpy
import describer

desc = arcpy.Describe('Example.gdb')

D = describer.Desc()

properties = D.find_properties(desc)

```


### How it works

The list of all valid properties for every describable object is contained in a .json file.  Using the `hasattr()` function, each is checked against the incoming object (*pass or fail*).  The property is returned back to the user if it can be used to successfully describe the object.

Currently there are two functions to get the valid properties:

- The first will return just the property name
- The second will return the property name and evaluated result

The included scraper dives into each of the property links on the Describe landing page and extracts the individual properties for use in the Describer class.  This is how they were initially scraped from the resource pages and how the full list can be updated with future changes.  The `properties_all.json` file is used by the class to test with.

##### Dependencies

- ArcGIS for Desktop ([ArcPy](http://resources.arcgis.com/en/help/main/10.1/index.html#//000v000000v7000000))
- The scraper uses [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)

##### Issues

1. On the main [Describe (arcpy)](http://resources.arcgis.com/en/help/main/10.1/index.html#/Describe/018v00000066000000/) page, there is a disconnect between the main properties list and the list in the navigation pane.  You will notice a few folders in the nav that don't exist in the main list where the urls were scraped from.  Therefore, the current `properties_all.json` file does not know of properties in the *"Network Analyst Layer properties"* and *"Network Dataset properties"* folders.
