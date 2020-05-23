# Shape_object
<img src="images/logo_50%.png" alt="Logo">
<h3 align="center">Shape_Object</h3>
<p align="center">Create an objected from a shapefile with shapely compatible geometry</p>
<p align="center">All of the source code can be found at the <a href="https://github.com/sbaker-dev/Shape_object">Shape_object github repository</a></p>


<!--Table OF CONTENTS -->
## Table of Contents
* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Basic Example](#basic-example)
* [Contributions](#contributions)
* [License](#license)


<!--ABOUT THE PROJECT -->
## About The Project
The [Pyshp](https://pypi.org/project/pyshp/1.2.10/) library allows for a pure python approach to reading in Esri 
Shapefile formatted files. This Project uses Pyshp to import these files, but then configures the objects to be 
[Shapely](https://pypi.org/project/Shapely/) style objects. 

This should make it quicker to start new projects involving shapefiles and reduce duplicating code.

<!-- GETTING STARTED -->    
## Getting Started 
Shape_object is avaliable via Pypi so you can pip install by the following command

```shell script
python -m pip install Shape_object
```

<!-- USAGE -->
## Usage
After installing Shape_object all you need to do is provide a path to Esri's .shp file and your good to go! Keep in mind
that Esri .shp files tend to have lots of supporting files and these should be in the same directory as Pyshp will look
within the directory of the .shp file for these supporting files.

```python
from Shape_object.core import ShapeObject

shape_object = ShapeObject(r"/path/to/your/shapefile/file.shp")

```
Now you have an objected that has loaded your shapefile which is filled with shapely objects. This means that it is very
easy to use shapely inbuilt functions as the IntelliSence from Shapely exists for all the objects within shape_obj.

![shapely_sense]

<!-- BASIC EXAMPLE -->
## Basic Example

All the features are held within a ShapeObject. It computes all the underlying geometry for a given shapefile once 
called so it is best to do this at the top of your file and set it equal to variable that then holds the underling 
ShapeObject class. Below is a simple example that prints the record held in the shapefile and the area of each polygon#


```python
from Shape_object.core import ShapeObject

shape_object = ShapeObject(r"/path/to/your/shapefile/file.shp")

for poly, rec in zip(shape_object.polygon_geometry, shape_object.polygon_records):
    print(rec)
    print(poly.area)
```


<!-- CONTRIBUTIONS -->
## Contributions
Contributions are always welcome, if you want to make a contribution simply make a pull request based on your fork of
the project

<!-- License -->
## License
Distributed under the MIT License. See `LICENSE` for more information.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[logo]: images/logo.png
[shapely_sense]: images/intelisense.png


