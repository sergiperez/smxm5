# Comandes de verificació de connectivitat

## Index
1. [ip](https://hackmd.io/AxKvK1WDQ3GUd58_rkAocg#ip)
2. [ifconfig](https://hackmd.io/AxKvK1WDQ3GUd58_rkAocg#ifconfig)
3. [ipconfig](https://hackmd.io/AxKvK1WDQ3GUd58_rkAocg#ipconfig)
4. [ping](https://hackmd.io/AxKvK1WDQ3GUd58_rkAocg#ping)
5. [arp](https://hackmd.io/AxKvK1WDQ3GUd58_rkAocg#arp)
6. [arping](https://hackmd.io/AxKvK1WDQ3GUd58_rkAocg#arping)
7. [nslookup](https://hackmd.io/AxKvK1WDQ3GUd58_rkAocg#nslookup)
8. [dig](https://hackmd.io/AxKvK1WDQ3GUd58_rkAocg#dig)
9. [host](https://hackmd.io/AxKvK1WDQ3GUd58_rkAocg#host)

## ip

| Element | Valor |
| -------- | -------- |
| Sistema operatiu | GNU/Linux     |
| Definició | Serveix per comprovar, canviar i des/habilitar l'adreça ip d'una targeta de xarxa d'un ordinador     |


### Comprovació de connexió

Per comprovar quina adreça de xarxa ho podem fer amb les següents comandes:  

```bash=
profe@estany:~$ ip a
profe@estany:~$ ip addr
profe@estany:~$ ip addr show
profe@estany:~$ ip addr show enp7s0
```

Les tres primeres ens mostra la configuració TCP/IP de totes les interfícies de xarxa del nostre ordinador. 
La darrera ordre ens mostra només la configuració de la interfície amb nom enp7s0.

Normalment els noms de les interfícies cablejades comencen per e (d'ethernet) i en el cas de les sense fil per w.

Vegeu el seu ús:

[![asciicast](https://asciinema.org/a/c9vfz2V0671vuJNqi9uJ5patW.svg)](https://asciinema.org/a/c9vfz2V0671vuJNqi9uJ5patW)

### Canviar adreça ip

Per afegir una adreça ip a una interfície es fa:

```bash=
profe@estany:~$ sudo ip addr add 192.168.0.11/24 dev enp7s0
``` 
En aquest cas afegim l'adreça 192.168.0.11/24 a la interfície cablejada enp7s0.

Si volem eliminar una adreça ip d'un itnerfícies es fa amb la següent ordre:
```bash=
profe@estany:~$ sudo ip addr add 192.168.0.11/24 dev enp7s0
``` 

**S'ha de fer amb permisos de sudo**

Vegeu el seu ús:

[![asciicast](https://asciinema.org/a/bvkgXlzAnYzSkVjvnJtAUEBYU.svg)](https://asciinema.org/a/bvkgXlzAnYzSkVjvnJtAUEBYU)


### Habilitar / deshabilitar la targeta de xarxa

Per deshabilitar (desconnectar) una interfície es fa:

```bash=
profe@estany:~$ sudo ip link set enp7s0 down
``` 
Per tornar-la a connectar es fa:

```bash=
profe@estany:~$ sudo ip link set enp7s0 down
``` 
**S'ha de fer amb permisos de sudo**

Vegeu el seu ús:

[![asciicast](https://asciinema.org/a/B9TWt6D31Q1kS2jcnIW9cTuN4.svg)](https://asciinema.org/a/B9TWt6D31Q1kS2jcnIW9cTuN4)

Vegeu més explicació a [https://www.tecmint.com/ip-command-examples/] (https://www.tecmint.com/ip-command-examples/)

## ifconfig

| Element | Valor |
| -------- | -------- |
| Sistema operatiu | GNU/Linux     |
| Definició | Serveix per comprovar, canviar i des/habilitar l'adreça ip d'una targeta de xarxa d'un ordinador. ** En versions noves de GNU/Linux en desús**    |


### Comprovació de connexió

Per comprovar quina adreça de xarxa ho podem fer amb les següents comandes:  

```bash=
profe@estany:~$ ifconfig
profe@estany:~$ ifconfig -a
profe@estany:~$ ifconfig enp7s0
```

Les dues primeres ens mostra la configuració TCP/IP de totes les interfícies de xarxa del nostre ordinador. 
La darrera ordre ens mostra només la configuració de la interfície amb nom enp7s0.

Normalment els noms de les interfícies cablejades comencen per e (d'ethernet) i en el cas de les sense fil per w.

Vegeu el seu ús:

[![asciicast](https://asciinema.org/a/3xb7sagE7Eoz01tsiReTsFcYJ.svg)](https://asciinema.org/a/3xb7sagE7Eoz01tsiReTsFcYJ)

### Canviar adreça ip

Per afegir una adreça ip a una interfície es fa:

```bash=
profe@estany:~$ sudo ifconfig enp7s0:1 192.168.0.11 netmask 255.255.255.0 broadcast 192.168.0.255
``` 
En aquest cas afegim l'adreça 192.168.0.11/24 a la interfície cablejada enp7s0:1. En aquest cas per fer servir una pseudointerfície que permet que ifconfig doni més d'una IP a la mateixa targeta de xarxa.

**S'ha de fer amb permisos de sudo**

Vegeu el seu ús:

[![asciicast](https://asciinema.org/a/okozQch0Kj8YXLChWenfj66Qr.svg)](https://asciinema.org/a/okozQch0Kj8YXLChWenfj66Qr)


### Habilitar / deshabilitar la targeta de xarxa

Per deshabilitar (desconnectar) una interfície es fa:

```bash=
profe@estany:~$ sudo ifconfig enp7s0:1 down
``` 
Per tornar-la a connectar es fa:

```bash=
profe@estany:~$ sudo ifconfig enp7s0:1 up
``` 
**S'ha de fer amb permisos de sudo**

Vegeu el seu ús:

[![asciicast](https://asciinema.org/a/K7a9wW8HwfAypuT8ZSt0LllFS.svg)](https://asciinema.org/a/K7a9wW8HwfAypuT8ZSt0LllFS)

Vegeu més explicació a [https://www.tecmint.com/ifconfig-command-examples/] (https://www.tecmint.com/ifconfig-command-examples/)


