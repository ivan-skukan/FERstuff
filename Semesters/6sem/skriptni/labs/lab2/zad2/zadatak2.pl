while (<STDIN>) {
    chomp;
    push @polje, $_;
}

$sum = 0;
$sum += $_ foreach @polje;
#print "Suma svih brojeva u polju je: $sum\n";
$len = @polje;
print "avg: ", $sum/$len, "\n";
