# VTP Vlan Trunking protocol

## Index
1. [Definició](https://github.com/sergiperez/smxm5/blob/master/vtp.md#definici%C3%B3)
2. [Glossari](https://github.com/sergiperez/smxm5/blob/master/vtp.md#glossari)
3. [Configuracions](https://github.com/sergiperez/smxm5/blob/master/vtp.md#configuracions)
4. [Passes](https://github.com/sergiperez/smxm5/blob/master/vtp.md#pases-per-realitzar-una-configuraci%C3%B3-de-vlan)
5. [Exemple i configuracions](https://github.com/sergiperez/smxm5/blob/master/vtp.md#exemple-i-comprovacions)


## Definició
Protocol que ens estalvia definir les vlan a tots els switchs.
Les VLAN es defineixen només en un switch (servidor) i la resta de switchs el poden usar (client).

## Glossari
1. **Domini:** nom lògic que identifica tots els switchs d'una mateixa xarxa. Per exemple tots els alumnes sou del domini BB, us agrupa i teniu mateixos professors i horari.
2. **Server:** switch on es defineix les vlan que usarà tota la xarxa.
3. **Client:** switch que usarà les vlan definides pel server en un domini. No pot definir vlan.
4. **Transparent:** switch que usa les vlan definides pel server, però pot definir de pròpies o renombrar les que li arriben.

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
10.- Assignar els enllaços troncals
Normalment els ports que serveixen per usar switchs.
```
Switch(config)#interface FastEthernet 0/2
Switch(config-if)#switchport mode trunk
```




