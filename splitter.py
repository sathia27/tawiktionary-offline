#!/usr/bin/python

'''
The downloded wiktionary bz2 files are large in the order of MBs which would inhibit fast searching,
hence the files are split into smaller junks and indexed using the indexer.py.

This script would split the large .bz2 file into smaller .bz2 files.

Note: Make sure that page data isn't split between the smaller bits.
'''

#-------------------------------------------------------------------------
'''
Steps
-----
1. Set pages_per_file = 1000
2. Open the large .xml.bz2 file
3. parse the large file as such without decompression
4. Read each page block and into a file buffer until count is 1000
    or end of file
5. Write the buffer as a file
6. Repeat 4&5 until end of file

Pseudo code - for splitting
---------------------------
open input file
open output file 1
count = 0
for each line in file:
    write to output file
    count = count + 1
    if count > maxlines:
         close output file
         open next output file
         count = 0


'''
#-------------------------------------------------------------------------

import bz2

ppfile = 10
bzfile = bz2.BZ2File('wiki-files/tawiktionary-20110518-pages-articles.xml.bz2')
count = 0

for line in bzfile:
    o.write(line)
    if '</page>' in line:
        count += 1