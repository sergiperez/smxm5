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

Vegeu més explicació a [https://www.tecmint.com/ifconfig-command-examples/](https://www.tecmint.com/ifconfig-command-examples/)

## ipconfig

| Element | Valor |
| -------- | -------- |
| Sistema operatiu | Windows     |
| Definició | Serveix per comprovar i renovar l'adreça ip d'una targeta de xarxa d'un ordinador     |

### Consultar la configuració TCP/IP

Per visualitzar la configuració bàsica de totes les interfícies:

```bash=
ipconfig 
```

Per visualitzar tota la configuració de totes les interfícies:
```bash=
ipconfig /all
```

Per comprovar la informació DNS (les traduccions per nom lògic a IP) de la nostra interfície:
```bash=
ipconfig /displaydns Adaptador
```

S'ha d'especificar quina interfície li correspon. És el nom posat a l'adaptador.

### Renovar configuracions TCP/IP

Per renovar la configuració TCP/IP que assigna un servidor DHCP:
```bash=
ipconfig /renew Adaptador
```
S'ha d'especificar quina interfície li correspon. És el nom posat a l'adaptador.

Per renovar la configuració DNS (les traduccions per nom lògic a IP) rebuda pel servidor DHCP:
```bash=
ipconfig /registerdns Adaptador
```
S'ha d'especificar quina interfície li correspon. És el nom posat a l'adaptador.


Per eliminar les peticions DNS (les traduccions per nom lògic a IP) que s'han fet durant la sessió:
```bash=
ipconfig /flushdns Adaptador
```
S'ha d'especificar quina interfície li correspon. És el nom posat a l'adaptador.

Més informació a [https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig)

## ping

| Element | Valor |
| -------- | -------- |
| Sistema operatiu | GNU/Linux - Windows     |
| Definició | Serveix per comprovar la connectivitat d'un equip enviant missatges a altres dispositius     |

## Exemple ordre

EL ping envia un paquet de dades per la xarxa a un altre dispositiu. Així ens permet saber si la nostra configuració TCP/IP és correcte i al del destí. Utilitza el protocol [ICMP](https://ca.wikipedia.org/wiki/Internet_Control_Message_Protocol).

L'ordre és:

```bash=
ping ipDestí
ping nomLogic
```

El destí pot ser una ip (8.8.8.8) o un nom lògic (excemple www.insjoandaustria.org)

## Paràmetres més interessants

- -t (només per a Windows) eternament i s'acaba  prement **ctr+c**. En GNU/Linux per defecte és etern.
- -c número de solicituts . Per enviar un nombre concret de missatges.
- -I interfície que s'usa. Si tenim wifi i cablejat decidir per quina enviem el missatge.
- -i interval (*delay*) entre peticions expressat en segons.
- -s mida del paquet (bytes). Per defecte són 64 bytes i el màxim són 65507 bytes. Ens permetrà conèixer millor el rendiment d'una xarxa en situacions d'estress amb volum de dades alt.

Hi ha un explicació sobre com saturar una xarxa amb pings fent el [Ping de la mort](https://es.wikipedia.org/wiki/Ping_de_la_muerte) però la majoria de servidors ja ho tenen previst, i per *Firewall* ho controlen o fins i tot hi ha servidors que no permeten rebre ping.  Vegeu en el video demostració que el servidor DNS de Google el 8.8.8.8 no permet rebre pings amb paquet de dades gran.

## Principals usos

El ping és de les comandes més usades per comprovar la bona instal·lació i configuració d'una xarxa. Principalment per:

- per saber si la targeta xarxa interna funciona (es fa ping a la pròpia targeta de xarxa, IP de la xarxa 127.0.0.0 /8)
- per saber si la targeta de xarxa té ben configurat el protocol TCP/Ip (ping sobre la pròpia IP que té la tarja)
- per saber si hi ha connectivitat en la xarxa local.
- per saber si hi ha connectivitat a xarxes externes i de fet saber si la gateway està ben configurada.
- per saber si es resolen bé els noms. Comprovant la configuració DNS (realitzant un ping per nom i no ip)

Vegeu el següent video explicatiu:

[![asciicast](https://asciinema.org/a/LUwQjircOYfzvjVC4JUYaeamg.svg)](https://asciinema.org/a/LUwQjircOYfzvjVC4JUYaeamg)

## arp mostra la taula ARP del vostre host
-d ip (elimina l'entrada d'aquella ip a la taula ARP)
-s ip mac (afegeix una entrada a la taula ARP)
-a ip (mostra l'entrada a la taula ARP que correspon a la IP)
Comentar manera de detectar Man in the middle

mostra tràfic arp o icmp:
tcpdump -ennqti eth0 \( arp or icmp \)

detecta adreces IP duplicades:
## arping -D -I eth0 192.168.99.147; echo $?

arping permet trobar ip duplicades.
## nslookup 
## dig (permeten verificar si funciona el DNS i quin servidor usem)
## host (permet saber la IP donat un nom)


