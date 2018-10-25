import sys
import re
import os


for line in sys.stdin:

    try :
        file = os.environ['mapreduce_map_input_file']
        prefix, file = file.split("u-")
    except :
        file = "unknown"
        
    author = file

    line = re.sub('[^a-z ]', ' ', line.lower())

    for word in line.split() :
        print(author+","+word+","+str(1))