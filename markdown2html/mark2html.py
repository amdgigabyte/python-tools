#coding=utf-8
import sys
import markdown2

def processmkd(filename):
    theHead = ''
    thehtml = markdown2.markdown_path(filename)
    theTitle = unicode(filename,"utf-8")
    fileHandle = open(filename+'.html', "w")
    theHead = '<!DOCTYPE html>'
    theHead += '<html><head><meta charset="utf-8"/><title>' + theTitle + '</title><link href="demo.css" type="text/css" rel="stylesheet"/></head><body>'
    theHead += thehtml
    theHead += '</body></html>\n'
    theHTML =  theHead.encode('utf-8')
    fileHandle.write(theHTML)
    fileHandle.close()

cmdargs = sys.argv[1:]
if len(cmdargs) > 0:
    for k in cmdargs:
        processmkd(k)
