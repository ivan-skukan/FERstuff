#! /bin/sh
#
# Dodajte ili modificirajte pravila na oznacenim mjestima ili po potrebi (i želji) na 
# nekom drugom odgovarajucem mjestu (pazite: pravila se obrađuju slijedno!)
#
IPT=/sbin/iptables

$IPT -P INPUT DROP
$IPT -P OUTPUT DROP
$IPT -P FORWARD DROP

$IPT -F INPUT
$IPT -F OUTPUT
$IPT -F FORWARD

$IPT -A INPUT   -m state --state ESTABLISHED,RELATED -j ACCEPT
$IPT -A OUTPUT  -m state --state ESTABLISHED,RELATED -j ACCEPT
$IPT -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

#
# za potrebe testiranja dozvoljen je ICMP (ping i sve ostalo)
#
$IPT -A INPUT   -p icmp -j ACCEPT
$IPT -A FORWARD -p icmp -j ACCEPT
$IPT -A OUTPUT  -p icmp -j ACCEPT

#
# Primjer "anti spoofing" pravila na sucelju eth0
#
#$IPT -A INPUT   -i eth0 -s 127.0.0.0/8  -j DROP
#$IPT -A FORWARD -i eth0 -s 127.0.0.0/8  -j DROP
#$IPT -A INPUT   -i eth0 -s 203.0.113.0/24  -j DROP
#$IPT -A FORWARD -i eth0 -s 203.0.113.0/24  -j DROP
#$IPT -A INPUT   -i eth0 -s 10.0.0.0/24  -j DROP
#$IPT -A FORWARD -i eth0 -s 10.0.0.0/24  -j DROP
#$IPT -A INPUT   -i eth0 -s 192.168.1.2  -j DROP
#$IPT -A FORWARD -i eth0 -s 192.168.1.2  -j DROP

#
# Web poslužitelju (tcp/80 i tcp/443) pokrenutom na www se može 
# pristupiti s bilo koje adrese (iz Interneta i iz lokalne mreže), ...
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -d 203.0.113.100 -p tcp --dport 443 -j ACCEPT
$IPT -A FORWARD -d 203.0.113.100 -p tcp --dport 80 -j ACCEPT
$IPT -A FORWARD -d 203.0.113.200 -p tcp --dport 53 -j ACCEPT
$IPT -A FORWARD -d 203.0.113.200 -p udp --dport 53 -j ACCEPT
#
# DNS poslužitelju (udp/53 i tcp/53) pokrenutom na www se može 
# pristupiti s bilo koje adrese (iz Interneta i iz lokalne mreže), ...
#
# <--- Dodajte pravila (ako je potrebno)
##napisano gore
#
# ... a SSH poslužitelju na www samo s racunala admin iz lokalne mreže "Private"
# 
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -s 10.0.0.20 -d 203.0.113.100 -p tcp --dport 22 -j ACCEPT
#
# ... kao i SSH poslužitelju na dns (samo s racunala admin iz lokalne mreže "Private")
# 
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -s 10.0.0.20 -d 203.0.113.200 -p tcp --dport 22 -j ACCEPT

# 
# S www je dozvoljen pristup poslužitelju database (Private) na TCP portu 10000 te pristup 
# DNS poslužiteljima u Internetu (UDP i TCP port 53).
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -s 203.0.113.100 -d 10.0.0.100 -p tcp --dport 10000 -j ACCEPT
$IPT -A FORWARD -o eth0 -s 203.0.113.100 -p udp --dport 53 -j ACCEPT
$IPT -A FORWARD -o eth0 -s 203.0.113.100 -p tcp --dport 53 -j ACCEPT
#
# ... S www je zabranjen pristup svim ostalim adresama i poslužiteljima.
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -s 203.0.113.100 -j DROP
#
# 
#S dns je dozvoljen DNS poslužiteljima u Internetu (UDP/TCP 53), sve ostalo je zabranjeno
#
#<----
$IPT -A FORWARD -o eth0 -s 203.0.113.200 -p tcp --dport 53 -j ACCEPT
$IPT -A FORWARD -o eth0 -s 203.0.113.200 -p udp --dport 53 -j ACCEPT

$IPT -A FORWARD -s 203.0.113.200 -j DROP

# Pristup svim ostalim adresama i poslužiteljima u DMZ je zabranjen.
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -o eth2 -j DROP #-i????
#

#====PRIVATE======

# Pristup SSH poslužitelju na cvoru database, koji se nalazi u lokalnoj mreži "Private", 
# dozvoljen je samo racunalima iz mreže "Private".
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -i eth1 -s 10.0.0.0/24 -d 10.0.0.100 -p tcp --dport 22 -j ACCEPT 
#
# Web poslužitelju na cvoru database, koji sluša na TCP portu 10000, može se pristupiti
# iskljucivo s racunala www koje se nalazi u DMZ (i s racunala iz mreže "Private").
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -s 203.0.113.100 -d 10.0.0.100 -p tcp --dport 10000 -j ACCEPT
$IPT -A FORWARD -i eth1 -o eth1 -s 10.0.0.0/24 -d 10.0.0.100 -p tcp --dport 10000 -j ACCEPT #iskreno sumnjam da je ovo potrebno, ali ne steti
#
# S racunala database je zabranjen pristup svim uslugama u Internetu i u DMZ.
#
# <--- Na odgovarajuce mjesto dodajte pravila (ako je potrebno)
$IPT -A FORWARD -i eth1 -s 10.0.0.100 -j DROP

# Zabranjen je pristup svim ostalim uslugama na poslužitelju database (iz Interneta i iz DMZ)
#
# <--- Na odgovarajuce mjesto dodajte pravila (ako je potrebno)
$IPT -A FORWARD -d 10.0.0.100 -j DROP
#
# S racunala iz lokalne mreže "Private" (osim s database) se može pristupati svim racunalima 
# u Internetu ali samo korištenjem protokola HTTP (tcp/80 i tcp/443) i DNS (udp/53 i tcp/53).
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD ! -s 10.0.0.100 -i eth1 -o eth0 -p tcp --dport 80 -j ACCEPT
$IPT -A FORWARD ! -s 10.0.0.100 -i eth1 -o eth0 -p tcp --dport 53 -j ACCEPT
$IPT -A FORWARD ! -s 10.0.0.100 -i eth1 -o eth0 -p udp --dport 53 -j ACCEPT
#
# Pristup iz vanjske mreže u lokalnu Private mrežu je zabranjen.
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A FORWARD -i eth0 -o eth1 -j DROP

#=======FW=======
#
# Na FW je pokrenut SSH poslužitelj kojem se može pristupiti samo iz lokalne mreže "Private"
# i to samo sa cvora admin.
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A INPUT -i eth1 -s 10.0.0.20 -p tcp --dport 22 -j ACCEPT
#
# Pristup svim ostalim uslugama (portovima) na cvoru FW je zabranjen.
#
# <--- Dodajte pravila (ako je potrebno)
$IPT -A INPUT -j DROP

#idk=======
