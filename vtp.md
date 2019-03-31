# VTP Vlan Trunking protocol

## Introducció
- Realització del següent repte:

![Introducció a VTP](https://github.com/sergiperez/smxm5/blob/master/Captura%20de%20pantalla%20de%202019-03-28%2009-28-29.png)

- Què us ha costat més? 

## Definició
Protocol que ens estalvia definir les vlan a tots els nodes.
Es defineixen en un node (servidor) i la resta de nodes el poden usar (client).

## Glossari
1. **Domini:** nom lògic que identifica tots els nodes d¡una mateixa xarxa. Per exemple tots els alumnes sou del domini BB, us agrupa i teniu mateixos professors i horari.
2. **Server:** node on es defineix les vlan que usarà tota la xarxa.
3. **Client:** node que usarà les vlan definides pel server en un domini. No pot definir vlan.
4. **Transparent:** node que usa les vlan definides pel server, però pot definir de pròpies o renombrar les que li arriben.

## Configuracions
Totes les configuracions s'han de fer des de comandes. El CLI.

Configuració node switch com a server
```
switch>enable
switch#conf t
switch(config)#vtp mode server
switch(config)#vtp domain jda
```
Configuració node switch com a client

```
switch>enable
switch#conf t
switch(config)#vtp mode client
switch(config)#vtp domain jda
```Configuració node switch com a tranasparent
```
## Pases per realitzar una configuració de VLAN

1.- Fer topologia
2.- Posar IP
3.- Posar mode trunk a les intefícies que connecten 
switchs
4.- Triar el switch server.
5.- Definir les VLAN al server. Des de CLI o visual.
```
Switch>enable
Switch#
Switch#vlan database
Switch(vlan)#vlan 112 name servers
VLAN 112 added:
    Name: servers
```    
6.- Definir el switch com a server
```
Switch(config)#vtp mode server
Device mode already VTP SERVER.
```
7.- Definir el domini
```
Switch(config)#vtp domain jda
Changing VTP domain name from null to jda
```
8.- Anar a la resta de switch i definir-los com a clients.
```
Switch(config)#vtp mode client
Setting device to VTP CLIENT mode.
Switch(config)#vtp domain jda
Changing VTP domain name from null to jda
```
9.- Assignar les VLAN als ports
```
Switch(config)#interface FastEthernet 0/1
Switch(config-if)#switchport access vlan 11
```

## Exemple i comprovacions



