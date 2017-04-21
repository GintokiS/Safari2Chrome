from plistlib import *

# read plist file and get URLs and titles
with open('./Bookmarks.plist', 'rb') as fp:
    plist = load(fp)

urlArray = plist['Children'][3]['Children']
marks = []

for dict in urlArray:
    marks.append((dict['URLString'], dict['URIDictionary']['title']))

# create Chrome bookmark html file
fileHeader = '''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
'''

rowHeader = '<DL><p>\n'
rowFooter = '</DL><p>'
bookmarkFolderLine = '<DT><H3 ADD_DATE="" LAST_MODIFIED="">Safari Web Bookmark</H3>\n'

f = open('chrome-bookmark.html', 'w')
f.write(fileHeader)
f.write(rowHeader)
f.write(bookmarkFolderLine)
f.write(rowHeader)

for target in marks:
    str = u'<DT><A HREF="' + target[0] + u'" ADD_DATE="" ICON="">' + target[1] + u'</A>' + '\n'
    f.write(str)

f.write(rowFooter)
f.write(rowFooter)
