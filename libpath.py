import sys
import os

# current search path for python in this virtual env
# print(str(sys.path))

# find out the current working dir; the package directory
# dir_path = os.path.dirname(os.path.realpath(__file__))
# print("current working dir: %s\n\n" % dir_path)

# add to the search path
'''
TODO:
Find out the path of the library you downloaded and extracted and adjust the variable lib_path 
'''
lib_path = r"C:\Users\mzahm.ZAHMAII\Documents\H-Nitec AI Application\Year 2\02_Service Robotics Application\SRA_Project\SRA_Lib\lib"
package_path = lib_path + "\python2.7\Lib\site-packages"

count = sum([p.count("pynaoqi-python2.7-") for p in sys.path])
if count == 0:
    sys.path.insert(0, lib_path)
    sys.path.insert(0, package_path)
else:
    print("libpath already in placed")
# new search path
# print(str(sys.path))
