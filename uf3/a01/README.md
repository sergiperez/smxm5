# Comandes de verificació de connectivitat

## Index
1. [ip](#ip)
2. [ifconfig](#ifconfig)
3. [ipconfig](#ipconfig)
4. [ping](#ping)
5. [arp](#arp)
6. [arping](#arping)
7. [nslookup](#nslookup)
8. [dig](#dig)
9. [host](#host)

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

