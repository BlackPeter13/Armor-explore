<html>
<head>
<meta http-equiv="Content-Type" content="text/html; Charset=UTF-8">
<title>Explorer</title>
</head>
<body>
<a href="<?php echo $_SERVER ['PHP_SELF']; ?>">Explorer</a>
<form action="" method="GET">
<input type="TEXT" name="search" value="input height or block hash or tx hash" size="50" onfocus="this.value=''"/>
<input type="submit" value="go"/>
</form>
<hr>
<?php
//print_r($_GET); echo"<br>";
//if ((isset($_GET['str'])) && ($_GET['str']!=''))
if (empty($_GET)==false)
{
   reset($_GET);
   $param1=key($_GET);
   $param2=current($_GET);
//   echo current($_GET);
   $command = escapeshellcmd(dirname(__FILE__)."/rpc_request.py $param1 $param2");
//   $command = escapeshellcmd(dirname(__FILE__)."/rpc_request.py raw_block ".$_GET['str']."");
//   echo $command;
   $res = shell_exec($command);
   echo $res;
}
else
{
   $command = escapeshellcmd(dirname(__FILE__)."/rpc_request.py");
   $res = shell_exec($command);
   echo $res;
}


?>
</body>
</html>
