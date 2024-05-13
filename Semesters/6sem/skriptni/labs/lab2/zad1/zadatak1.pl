print "Upiši znakovni niz: ";
$znakovni_niz = <STDIN>;
print "Upiši broj ponavljanja: ";
$broj_ponavljanja = <STDIN>;

chomp($broj_ponavljanja);

print $znakovni_niz x $broj_ponavljanja;
