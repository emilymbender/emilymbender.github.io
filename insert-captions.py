# Script for inserting captions into individual pages for new years cards.
# Inputs:
#
# A text file with the captions, one per line.
# A Pages/ directory with the html files, same number as the captions.
#
# The script assumes that Pages-new/ exists and will populate it with updated
# html files.

import sys
import re

captionfile = open(sys.argv[1],"r")
captions = captionfile.readlines()

p = 1

for caption in captions:
    page = str(p)

    pagefile = open(sys.argv[2]+"/"+page+".html","r")
    newpage = open("Pages-new/"+page+".html","w")

    keepnextline = True
    
    for line in pagefile.readlines():
        if keepnextline:
            newpage.write(line)
        else:
            newpage.write(caption)
            keepnextline = True

        if re.search("src=\"../Images",line):
            keepnextline = False


    p += 1

    pagefile.close()
    newpage.close()
    
