#!/usr/bin/python
from sys import argv
import os
monthNames = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthNumbers = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
thisMonth = argv[1]
thisYear = argv[2]
theDays = argv[3:]
def mangle(yearOrDay):
    """prec: year is a positive integer
postc: returns the last two digits in string format for the year or day"""
    yearOrDay = yearOrDay % 100
    yearOrDay = str(yearOrDay)
    if(len(yearOrDay) == 1):
        yearOrDay = "0" + yearOrDay
    return yearOrDay
def generateDailyDirName(day, month, year):
    """prec day, month, year are integers
post: returns a string filename of the form ddmmmyy (ex: 26May57.php)"""
    dirName = mangle(day) + monthNames[month][:3] + mangle(year)
    return dirName
def fileNameList():
    out = []
    for d in theDays:
        dirName = generateDailyDirName(int(d), monthNumbers[thisMonth],
            int(thisYear))
        os.makedirs(dirName, mode=0o755)
        out.append(dirName + "/index.php")
    return out
bigAssList = fileNameList()
print(bigAssList)
def showNext(fileName):
    loc = bigAssList.index(fileName)
    return "" if loc == len(bigAssList) -1 else  bigAssList[loc + 1]
def showLast(fileName):
    loc = bigAssList.index(fileName)
    return "" if loc == 0 else  bigAssList[loc - 1]
def today(day, month, year):
    return "" + str(day) + " " + monthNames[month] + " " + str(year)
def buildAllDays():
    d = [int(k) for k in theDays]
    month = monthNumbers[thisMonth]
    year = int(thisYear)
    for eachDay in d:
        dfn = generateDailyDirName(eachDay, month, year) + "/index.php"
        outFile = open(dfn, "w")
        outFile.write("""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8"/> 
<link rel="stylesheet" type="text/css" 
href ="http://www.ncssm.edu/~morrison/CSS/pageContent.css"/>
<link rel="stylesheet" type="text/css" 
href ="http://www.ncssm.edu/~morrison/CSS/boxes.css"/>
<link rel="stylesheet" type="text/css" 
href ="http://www.ncssm.edu/~morrison/CSS/tableLayout.css"/>
<link rel="stylesheet" type="text/css" 
href ="http://www.ncssm.edu/~morrison/CSS/menus.css"/>
<link href="https://fonts.googleapis.com/css?family=EB+Garamond" rel="stylesheet"/>
<link rel = "shortcut icon" href = "http://www.ncssm.edu/~morrison/CSS/rhino.ico"/>

<!--
Uncomment for prettyprint
<script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js?lang=html&skin=sunburst"></script>
<style type = "text/css">
pre.prettyprint{
border: none !important;
}
</style>
<style type = "text/css">
pre.prettyprint{
border: none !important;
}
</style>
-->
<!--
Uncomment for mathJax
<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
-->
<!--
Uncomment for JQuery
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js"></script>
-->
<!--
Uncomment for do-nows
<script type = "text/javascript">
    var show = true;
    var hideDiv = function(divID)
    {
        jQuery("#" + divID).hide();
    }
    var showDiv = function(divID)
    {
        jQuery("#" + divID).show();
    }
    var change = function(divID)
    {
        if(!show)
            hideDiv(divID);
        else
            showDiv(divID);
        show = !show;
    }
    jQuery(document).ready(function()
    {
        hideDiv("doNow1");
    });
</script>
-->\n
        """)
        outFile.write("<title>"+ today(eachDay, month, year) + "</title>\n")
        outFile.write("""
</head>
<body>

<header>\n""")
        outFile.write("<h2>" + today(eachDay, month, year) + "</h2>")
        
        outFile.write("""
<?php include '/home/morrison/public_html/SCRIPTS/menus.php';
?>
</header>

<nav>
<?php
include '/home/morrison/public_html/SCRIPTS/navigation.php';
?>
</nav>

<main>
<br/>
<br/>
<br/>
<p>Notes go here!!</p>
</main>
<footer>\n
""")
        outFile.write("<ul>\n")
        outFile.write('<li><a href = "../' + showLast(dfn) + '">last class</a></li>\n')
        outFile.write('<li><a href = "../' + showNext(dfn) + '">next class</a></li>\n')
        outFile.write("""<li><a href = "../index.php"> Back to Calendar View</a></li>
</ul>
</footer>
</body>
</html>""")
buildAllDays()
