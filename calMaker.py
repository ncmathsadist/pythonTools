#!/usr/bin/python
#    This program is relased using the Gnu Pulblic License.
#    Author: John M. Morrison
#    I make no warranties or representations about this program.
#    Here are the usages.  
#
#    $ calMaker.py month year
#    $ calMaker.py month year <List of integers 0-4>
#
#    The first usage creates a weekday calendar for the month
#    and year passed it in a PHP file named index.php.
#    Each numerical day has a link to 
#    an HTML file.  To make this useful, you should make files
#    with names of the form ddmmmyy, where dd is the date
#    (precede with a 0 if the dd < 9), mmmm, i the first three
#    letters of the month name, e.g. September is Sep and yy
#    is the last two digits of the year.  Place these in the same
#    directory as the index page produced by this program.
#    Use the program month.py to create shell HTML files in that directory.

#    Place this program in a file named
#    calMaker.py.  This program creates a weekday calendar
#    with links to the HTML files described above.  If you have
#    a class that does not meet certain days, you may pass
#    them as a space-separated list of integers.  For example
#    # calMaker.py August 2009 4
#    creates a calendar for a class not meeting on Friday.  No
#    links are created for friday, but the table cells bear
#    class = "Xday"; you can place a class in a CSS file to
#    make these cells a different color.

#    Revised 6 Aug 2010.
#
import calendar
import sys
import html
def monthNum(month):
	d = {"January":1, "February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
	return d[month]
def fileName(year, month, day):
	day = str(day) if day > 9 else "0" + str(day)
	month = month[:3]
	year = year % 100
	year = str(year) if year > 9 else "0" + str(year)
	return  "" + day + month + year + "/index.php"
##begin main routine
month = sys.argv[1]
year = sys.argv[2]
xdayList = []
if(len(sys.argv) > 3):
	xdayList = map(int, sys.argv[3:])
outFile = open("index.php", "w")

html.topMonthNEW(outFile)
outFile.write(month + " " + year + "</title>")
outFile.write("</head>\n<body>\n")
outFile.write('<header>\n')
outFile.write("<h1>" +month + " " + year  + "</h1>")   ##HERE

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

""")
outFile.write("""
<table class = "calendar">
<tr>
    <th>Monday</th>
    <th>Tuesday</th>
    <th>Wednesday</th>
    <th>Thursday</th>
    <th>Friday</th>
</tr>\n""")
start, daysInMonth = calendar.monthrange(int(year), monthNum(month))
if( 0 < start < 5 ):
	outFile.write("<tr>\n" + "\t<td></td>\n"*start)
for k in range(start, daysInMonth + start):
	if k%7 == 0:
		outFile.write("<tr>\n")
	if k%7 < 5:
		tdbegin = "<td class = \"Xday\">" if k%7 in xdayList else "<td>"#put simple td if not xday
		dateSymbol = str(1 + k - start) if k%7 in xdayList else ("<a href = \"" + fileName(int(year), month, 1 + k - start) + "\">" + str(1 + k - start)  + "</a>")

		outFile.write(tdbegin + dateSymbol +  "</td>\n")
	if k%7 == 4:
		outFile.write("</tr>\n")
end = (calendar.weekday(int(year), monthNum(month), daysInMonth))%7
if end < 5:
	outFile.write("<td></td>\n"*(4 - end) + "</tr>\n")
outFile.write("</table>\n")
outFile.write('<p class = "display"><a href = "../index.php">Back to Course Page</a></p>\n')
outFile.write("</main>")
outFile.write("</body>\n")
outFile.write("</html>\n")
outFile.close()
