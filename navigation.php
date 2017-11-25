<?php
function showRegularFiles($path)
{
    $fileList = array();
    if($handle = opendir($path)) 
    {
        while (false !== ($file = readdir($handle))) 
        {
            if (!is_dir($file) && $file != 'index.php' 
                && $file != 'navigation.php' && $file[0] != '.') 
            {
               // echo '<a href = "'.$file.'">'."$file"."</a><br/>\n";
                array_push($fileList, $file);
            }
        }
        closedir($handle);
    }
    sort($fileList);
    foreach($fileList as $k)
    {
        echo '<li><a href = "'.$k.'">'."$k"."</a></li>\n";
    }
    unset($k);
}

function showDirectories($path)
{
    $dirList = array();
    if($handle = opendir($path)) 
    { 
        while (false !== ($file = readdir($handle))) 
        {
            if (is_dir($file) && $file != "." && $file != "..")
            {
               // echo '<a href = "'.$file.'">'."$file"."</a><br/>\n";
                array_push($dirList, $file);
            }
        }
        closedir($handle);
    }
    sort($dirList);
    foreach($dirList as $k)
    {
        echo '<li><a href = "'.$path."/".$k.'">'."$k"."</a></li>\n";
    }
    unset($k);
}
?>

<br/>
<br/>
<br/>
<h2>Navigation</h2>

<hr />
<h3>Directories</h3>

<?php
echo '<ul>';
echo '<li><a href = "..">Parent Directory</a></li>';
showDirectories(".");
echo '</ul>';
echo '<hr/>';
echo '<h3>Files</h3>';
echo '<ul>';
showRegularFiles(".");
echo '</ul>';
echo '<hr />';
echo '<h3>Other Places</h3>';
echo '<ul>';
echo '<li><a href = "http://www.ncssm.edu/~morrison/currentClasses">Current Courses Main Page</a></li>';
echo '<li><a href = "http://www.ncssm.edu/~morrison">Morrison\'s Main Page</a></li>';
echo '</ul>';
?>


