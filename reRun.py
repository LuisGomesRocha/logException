#!/usr/bin/python
from subprocess import Popen
import sys

filename = sys.argv[1]
while True:
    print("\nStarting " + filename)
    p = Popen("python " + filename, shell=True)
    p.wait()
    
#It uses python to open test.py as a new subprocess. 
# It does so in an infinite while loop, and whenever [name your sript].py
# fails, the while loop restarts test.py as a new subprocess.

#I’ll have to make the forever script executable by running 
# chmod +x forever. 
# Optionally forever script can be moved to some location 
# in the PATH variable, to make it available from anywhere.

#Next, I can start my program with:

# ./reRun [name your sript].py