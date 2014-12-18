## Describer

Describer is an attempt to make the [Describe (arcpy)](http://resources.arcgis.com/en/help/main/10.1/index.html#/Describe/018v00000066000000/) function more user friendly by displaying all the valid properties you have access to based on the input data type.

For example, describing a geodatabase feature class means you have access to [several properties](http://resources.arcgis.com/en/help/main/10.1/index.html#/FeatureClass_properties/018v00000011000000/).  You can also use the properties available [GDB FeatureClass properties](http://resources.arcgis.com/en/help/main/10.1/index.html#/GDB_FeatureClass_properties/018v0000005t000000/) and so on.  This means you must navigate multiple resource pages to determine which properties are available for any given input.

Describer uses the hasattr(object, name) python built-in function to find all
the valid properties for a given describe object.  This trick is already hinted at in the ArcGIS documentation:

>If you try to access a property that a Describe object does not have, it will either throw an error or return an empty value (None, 0 or -1, or empty string). If you are uncertain of a particular property, you can use Python's **hasattr()** function to check.

Describer also does the *describing* for you so there is no need to use arcpy to describe the input before feeding it into the class.

### Example

```python
import describer

desc = '\\Example.gdb'

D = describer.Desc()

properties = D.find_properties(desc)
```
Returns:
```python
[u'baseName', u'catalogPath', u'children', u'childrenExpanded', u'dataElementType', u'dataType', u'extension', u'file', u'fullPropsRetrieved', u'metadataRetrieved', u'name', u'path', u'children', u'catalogPath', u'connectionProperties', u'connectionString', u'currentRelease', u'domains', u'release', u'workspaceFactoryProgID', u'workspaceType']
```

### Getting Started

- [Download](https://github.com/EsriCanada/describer/archive/master.zip) or fork this repository
- Place the *describer* module folder relative to your working script
- At the top of your script `import describer`
- Instantiate the class and call either of the two available functions


### How it works

The list of all valid properties for every describable object is contained in a .json file.  Using the `hasattr()` function, each is checked against the incoming object (*pass or fail*).  The property is returned back to the user if it can be used to successfully describe the object.

Currently there are two functions to get the valid properties:

- The first will return the valid property names as a python list
- The second will return the property name and evaluated result as a formatted string

##### Dependencies

- ArcGIS for Desktop ([ArcPy](http://resources.arcgis.com/en/help/main/10.1/index.html#//000v000000v7000000))
- Tested with [Python 2.7.5](https://www.python.org/download/releases/2.7.5/)


##### Issues

1. On the main [Describe (arcpy)](http://resources.arcgis.com/en/help/main/10.1/index.html#/Describe/018v00000066000000/) page, there is a disconnect between the main properties list and the list in the navigation pane.  You will notice a few folders in the nav that don't exist in the main list where the urls were scraped from.  Therefore, the current `properties_all.json` file does not know of properties in the *"Network Analyst Layer properties"* and *"Network Dataset properties"* folders.

##### Properties Scraper

The included scraper dives into each of the property links on the Describe landing page and extracts the individual properties for use in the Describer class.  This is how they were initially scraped from the resource pages and how the full list can be updated with future changes.  The `properties_all.json` file is used by the class to test against.

*Dependency*

- The scraper uses [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
