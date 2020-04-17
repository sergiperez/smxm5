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
- -b per fer el ping de broadcast.

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

## arp

| Element | Valor |
| -------- | -------- |
| Sistema operatiu | GNU/Linux - Windows     |
| Definició | Serveix per consultar i gestionar la taula ARP del nostre equip.  |

### Explicació ordre

La taula arp ens permet treballar amb la taula ARP. La taula ARP és un registre que té l'ordinador per emmagatzemar l'equivalència entre IP (configuració lògica) i les MAC (configuració física) que usan per comunicar-se en les xarxes locals.
Ja que quan es comunica per xarxa, sempre ho fa localment i s'usa adreces MAC. Si ha de fer connexió a l'exterior, es comuncia localment per la MAC de la porta d'enllaç. Aquest és el comportament del protocol [ARP](https://ca.wikipedia.org/wiki/ARP).
![](https://i.imgur.com/VS16skB.png)


### Consultar la taula

Es fa amb l'ordre **arp** o posant el paràmetre **-a**

```bash=
profe@estany:~/smx1m5/smxm5/uf3/a01$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
_gateway                 ether   84:cf:bf:8b:9c:1c   C                     wlp0s20f3
profe@estany:~/smx1m5/smxm5/uf3/a01$ arp -a
_gateway (192.168.43.1) at 84:cf:bf:8b:9c:1c [ether] on wlp0s20f3

```
### Gestionar la taula

Hi ha els següents paràmetres:

- -s ip mac (afegeix una entrada estàtica a la taula ARP)
```bash=
profe@estany:~/smx1m5/smxm5/uf3/a01$ arp -s 192.167.0.1 84:cf:bf:8b:9c:11
SIOCSARP: L’operació no és permesa
profe@estany:~/smx1m5/smxm5/uf3/a01$ sudo arp -s 192.168.43.11 84:cf:bf:8b:9c:11
```

Fixeu-vos que la primera falla perquè la ip no és de la mateixa xarxa local.
```bash=
profe@estany:~/smx1m5/smxm5/uf3/a01$ ip addr show wlp0s20f3
3: wlp0s20f3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 30:24:32:b7:24:15 brd ff:ff:ff:ff:ff:ff
    inet 192.168.43.57/24 brd 192.168.43.255 scope global dynamic noprefixroute wlp0s20f3
       valid_lft 2405sec preferred_lft 2405sec
    inet6 fe80::2e31:e74f:fccd:288d/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```
- -d ip (elimina una entrada d'aquella ip a la taula ARP)
```bash=
profe@estany:~/smx1m5/smxm5/uf3/a01$ sudo arp -d 192.168.43.11
```

### Curiositat

Hi ha un mètode clàssic d'espionatge a xarxa que és el *[Man in the middle](https://ca.wikipedia.org/wiki/Intercepci%C3%B3)* hi ha un equip que es fa passar per la gateway (normalment el router), espia i després ho reenvia al router veritable. Una manera d'evitar-ho és afegint una entra estàtica a la taula ARP on es posa la ip de la porta d'enllaç (*gateway*) i la MAC d'aquesta. Ja que la falsa porta d'enllaç es posa la mateixa IP que el router però no pot posar-se la MAC:


Vegeu el següent video explicatiu:

[![asciicast](https://asciinema.org/a/pNk37nWXdTmKkDtA68hGRO6di.svg)](https://asciinema.org/a/pNk37nWXdTmKkDtA68hGRO6di)


## arping 

| Element | Valor |
| -------- | -------- |
| Sistema operatiu | GNU/Linux   |
| Definició | Permet descobrir la mac d'una ip xarxa. Permete detectar duplicats |

### Exemples 

Per conèixer la MAC quan li fem ping:
```bash=
profe@estany:~/smx1m5/smxm5/uf3/a01$ arping 192.168.43.1 -I wlp0s20f3
ARPING 192.168.43.1 from 192.168.43.57 wlp0s20f3
Unicast reply from 192.168.43.1 [84:CF:BF:8B:9C:1C]  5.100ms
```

El més habitual és l'ús d'aquesta ordre per detectar ip's duplicades. Vegeu en l'ordre següent com es descobreix si en una xarxa local hi ha IP's duplicades.

```bash=
arp -D -I eth0 192.168.99.147; echo $?
```

## nslookup 

| Element | Valor |
| -------- | -------- |
| Sistema operatiu | GNU/Linux - Windows   |
| Definició | Permet fer consultes DNS i així comprovar si ens funciona bé la resolució de noms|

### Ús

Es posa el nom de la comanda i seguit la URL que volem comprovar o bé només la comanda i podrem anar comprovant diferents URL. 

Per tant comprovem:
- que tenim bé el protocol TCP/IP
- que accedim a xarxes externes (per tant ben configurada la gateway)
- que tenim ben configurat el servidor de DNS

I també sabem la IP que correspon a una URL i quin servidor DNS usem.

```bash=
profe@estany:~/smx1m5/smxm5/uf3/a01$ nslookup www.google.com
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	www.google.com
Address: 216.58.201.164
Name:	www.google.com
Address: 2a00:1450:4003:802::2004
profe@estany:~/smx1m5/smxm5/uf3/a01$ nslookup
> www.google.com
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	www.google.com
Address: 216.58.201.164
Name:	www.google.com
Address: 2a00:1450:4003:802::2004
> www.elperiodico.cat
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
www.elperiodico.cat	canonical name = secure.grupozeta.es.edgekey.net.
secure.grupozeta.es.edgekey.net	canonical name = e12551.f.akamaiedge.net.
Name:	e12551.f.akamaiedge.net
Address: 104.83.44.94

```
En aquest cas veiem que elperiodico.cat té la ip 104.83.44.94 i el servidor DNS que usem és el prpi ordinador el 127.0.0.53.

## dig (permeten verificar si funciona el DNS i quin servidor usem)

| Element | Valor |
| -------- | -------- |
| Sistema operatiu | GNU/Linux |
| Definició | Permet fer consultar quina configuració té el servidor DNS que allotja un domini|

### Ús

Aquí podem veure quina definició té l'entrada DNS que respon per al domnini www.google.com .
```bash=
profe@estany:~$ dig www.google.com

; <<>> DiG 9.11.3-1ubuntu1.11-Ubuntu <<>> www.google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 61389
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;www.google.com.			IN	A

;; ANSWER SECTION:
www.google.com.		124	IN	A	216.58.211.36

;; Query time: 0 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Fri Apr 17 09:58:04 CEST 2020
;; MSG SIZE  rcvd: 59
```
En aquest cas veiem com està definit el registre en el DNS del domini www.google.com i veiem al final quin servidor he usat per fer la consulta, o sigui quin servidro DNS tinc (a partir de la línia ;; Query time: 0 msec). 

Per tant ens permet:
- saber quina IP té una URL.
- saber quina és la IP del meu servidor de DNS.

## host (permet saber la IP donat un nom)

| Element | Valor |
| -------- | -------- |
| Sistema operatiu | GNU/Linux   |
| Definició | Permet conèixer quina ip té un nom lògic (un domini)|

### Exemple ús

Es posa el domini (nom lògic d'una màquina) darrera la comanda i ens respon amb la seva ip v4 i v6.

```bash=
profe@estany:~/smx1m5/smxm5/uf3/a01$ host www.google.com
www.google.com has address 216.58.201.164
www.google.com has IPv6 address 2a00:1450:4003:809::2004
```
En aquest cas no ens indica quin server DNS fem servir.

Vegeu en aquest video les diverses ordres per comprovar DNS que tenim:
[![asciicast](https://asciinema.org/a/pNk37nWXdTmKkDtA68hGRO6di.svg)](https://asciinema.org/a/pNk37nWXdTmKkDtA68hGRO6di)


