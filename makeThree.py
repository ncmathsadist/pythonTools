#!/usr/bin/python
from sys import argv
root = argv[1]
outFile = open(root + ".html", "w")
outFile.write("<!doctype html>\n")
outFile.write("<!--Author: Morrison-->\n")
outFile.write("""
<html>
<head>
<title>%s</title>
<link rel="stylesheet" href="%s.css"/>
<script type="text/javascript" src="%s.js">
</script>
</head>
<body>
</body>
</html>""" %(root, root, root))
outFile.close()
outFile = open(root + ".css", "w")
outFile.write("""/*Author: Morrison*/
h1, h2, .display
{
    text-align:center;
}
canvas
{
    border:solid 1px black;
}
""")
outFile.close()
outFile = open(root + ".js", "w")
outFile.write("/*Author: Morrison*/\n")
outFile.close();
