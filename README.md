# Meteorological-Data-Downloader

This program will download meteorological data from the meteo.gr website.

what it does so far:

    1. it downloads from a list of stations in a location
    2. it filters out headers and footers
    3. removes empty files
    4. removes dirty files (files with contents other than data)
    5. adds a header to the files
    6. merges all of the files within a a station

TODO:

    1. drop all days with all data missing besides the date
    2. for days with partially missing data just fill them with nan
    3. fix the merge() function in utilities because the merged file contains objects instead of float64

to run:

    
    1. type:python downloader.py

    2. type:python clean_up.py
    
    3. type:python format.py
    
    4. if you want to run them all together, type: python run.py
    
    you are done!!!
        

NOTE: 
tested on the following operating systems:

    1. Windows 7 machine (64 bit)
    2. mac 10.9.5

Recommended:  have anaconda python 3.5 installed

if not simply install:

    python 3.5
    pandas


