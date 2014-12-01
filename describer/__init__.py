"""Describer
Esri Canada
https://github.com/EsriCanada

Describer uses the hasattr(object, name) built-in function to find all
the valid properties for a given describe object.  As the docs state:

<If you are uncertain of a particular property, you can use Python's hasattr() function to check.>

See the Describe (arcpy) object for a listing of all valid properties given valid element:

Describe (arcpy)
http://resources.arcgis.com/en/help/main/10.1/index.html#/Describe/018v00000066000000/

The list of all valid properties is contained in a .json file and each is checked against
the incoming element.  The property is retunred back to the user if it can be used to
successfully describe the object.

The included scraper dives into each of the properties links on the Describe landing page
and extracts the individual properties.  This is how they were initially grabbed from the
resource pages and how the full list can be updated with future changes.

For more information and to contribute see the GitHub repository
"""

__author__ = "Adam Marinelli"
__version__ = "1.0"

__all__ = ['Describer']

import arcpy
import json
import os

class Desc():
    """
    This class defines the basic interface to test for
    valid properties on the incoming object.
    """

    def __init__(self):
        # open the attributes file which contains the full list of all properties
        # for all objects.  Can be updated using auxillary script.
        self.property_list = json.loads(open(os.path.join(os.path.dirname(__file__), "properties_all.json"), "r").read())
        self.property_array = self.property_list['properties']
        self.valid_props = []
        self.desc_obj = {}

    def describe(self, desc):
        self.desc_obj = arcpy.Describe(desc)
        return

    def find_properties(self, desc):
        self.describe(desc)
        self.valid_props = []
        for prop in self.property_array:
            if hasattr(self.desc_obj, prop):
                self.valid_props.append(prop)
        return self.valid_props

    def pretty_properties(self, desc):
        self.find_properties(desc)
        for prop in self.valid_props:
            print "{0} : {1}".format(prop, getattr(self.desc_obj, prop))
