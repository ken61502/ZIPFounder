ZIPFounder
==========
1. To run the server, you may need:
```
pip install pyshp
pip install scipy
pip install numpy
pip install matplotlib
pip install tornado
python server.py
```
2. Static directory is removed since its are too large.
Static directory includes the following files:
* tl_2014_us_zcta510.dbf
* tl_2014_us_zcta510.prj
* tl_2014_us_zcta510.shp
* tl_2014_us_zcta510.shp.ea.iso.xml
* tl_2014_us_zcta510.shp.iso.xml
* tl_2014_us_zcta510.shp.xml
* tl_2014_us_zcta510.shx

3. Please add the Google Map API Key to templates/zipmap.html
