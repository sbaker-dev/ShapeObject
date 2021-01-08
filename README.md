![logo]
# shapeObject
Create an objected from a shapefile with shapely compatible geometry

The [Pyshp][pyshp] library allows for a pure python approach to reading in Esri Shapefile formatted files. This Project
uses Pyshp to import these files, but then configures the objects to be [Shapely][shapely] style objects. 

## Getting Started 
shapeObject is available via Pypi so you can pip install by the following command

```shell script
python -m pip install shapeObject
```

## Usage
After installing shapeObject all you need to do is provide a path to Esri's .shp file and your good to go! Keep in mind
that Esri .shp files tend to have lots of supporting files and these should be in the same directory as Pyshp will look
within the directory of the .shp file for these supporting files.

```python
from shapeObject.ShapeObject import ShapeObject

file = ShapeObject(r"/path/to/your/shapefile/file.shp")

```
Now you have an objected that has loaded your shapefile which is filled with shapely objects! If you want a more 
detailed set of information you use the example jupyter notebook within the Examples directory along with some example
shapefiles that have been provided for you, or your own if you have them.

[pyshp]: https://pypi.org/project/pyshp/1.2.10/
[shapely]: https://pypi.org/project/Shapely/
[logo]: images/logo3.png


