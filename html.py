#
#  Revised Oct 2016 to use the Garamond font.
#
#
def bottom(filePipe):
    filePipe.write("</body>\n")
    filePipe.write("</html>\n")
def topMonth5(outFile):
    outFile.write("""<!doctype html>
<html lang = "en">
<head>
    <meta charset = "utf-8"/>
    <link rel = "stylesheet" type = "text/css" href = "http://www.ncssm.edu/~morrison/CSS/threePage.css"/>
    <link rel = "stylesheet" type = "text/css" href = "http://www.ncssm.edu/~morrison/CSS/calendar.css"/>
    <link rel = "shortcut icon" href = "http://www.ncssm.edu/~morrison/CSS/rhino.ico"/>
<title>
""")
## Simple HTML5 page hed
def topPage5(outFile):
    outFile.write("""<!doctype html>
<html lang = "en">
<head>
    <meta charset = "UTF-8"/>
    <link rel = "stylesheet" type = "text/css" href = "http://www.ncssm.edu/~morrison/CSS/threePage.css"/>
    <link rel = "stylesheet" type = "text/css" href = "http://www.ncssm.edu/~morrison/CSS/pageContent.css"/>
    <link rel = "stylesheet" type = "text/css" href = "http://www.ncssm.edu/~morrison/boxes.css"/>
<title>
""")
## old XHTML pae head
def topIndex(outFile):
	outFile.write("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
<link rel=\"stylesheet\" type=\"text/css\" 
href =\"http://www.ncssm.edu/~morrison/CSS/indexStyle.css\" />
<title>""")
## Current Page head
def topMonthNEW(outFile):
    outFile.write("""    
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8"/> 
<link rel="stylesheet" type="text/css" 
href ="http://www.ncssm.edu/~morrison/CSS/pageContent.css" />
<link rel="stylesheet" type="text/css" 
href ="http://www.ncssm.edu/~morrison/CSS/boxes.css" />
<link rel="stylesheet" type="text/css" 
href ="http://www.ncssm.edu/~morrison/CSS/tableLayout.css" />
<link rel="stylesheet" type="text/css" 
href ="http://www.ncssm.edu/~morrison/CSS/calendar.css" />
<link rel="stylesheet" type="text/css" 
href ="http://www.ncssm.edu/~morrison/CSS/menus.css" />
<link href="https://fonts.googleapis.com/css?family=EB+Garamond" rel="stylesheet">
<link rel = "shortcut icon" href = "http://www.ncssm.edu/~morrison/CSS/rhino.ico"/>
<script type = "text/javascript" src = 
"http://www.ncssm.edu/~morrison/SCRIPTS/menus.js"></script>
<!--
Uncomment for JQuery
<script type = "text/javascript" src = "http://code.jquery.com/jquery-latest.min.js"></script>
-->
<!--
Uncomment for prettyprint
<script src="https://google-code-prettify.googlecode.com/svn/loader/run_prettify.js"></script>
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
-->
        <title>""")
