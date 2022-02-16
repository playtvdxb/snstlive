<h1><?php
$command = escapeshellcmd('python test.py');
$output = shell_exec($command);
echo "ARIVARASAN SUN TV";
?>
<h1>
<iframe src="<?=$output?>"width="100%" height="100%"></iframe>

