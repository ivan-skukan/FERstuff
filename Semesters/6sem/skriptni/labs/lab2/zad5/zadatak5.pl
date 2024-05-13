my @factors;
my %map;
my @values;

while (defined(my $line = <>)) {
    #print "$line\n";
    if ($line eq "\n" || $line eq '' || $line =~ /^#/) {
        #print "first if\n";
        next;
    }

    if ($line =~ /^([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);(.*)$/ and scalar @factors == 0) {
        push @factors, $1, $2, $3, $4, $5, $6, $7;
        #print "second if\n";
        next;
    }

    if ($line =~ /^([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);([^;]*);(.*)$/) {
        #print "third if\n";
        my $jmbag= $1;
        my $lname = $2;
        my $fname = $3;
        my $f1 = $4;
        my $f2 = $5;
        my $f3 = $6;
        my $f4 = $7;
        my $f5 = $8;
        my $f6 = $9;
        my $f7 = $10;

        my $sum = $factors[0] * $f1 + $factors[1] * $f2 + $factors[2] * $f3 + $factors[3] * $f4 + $factors[4] * $f5 + $factors[5] * $f6 + $factors[6] * $f7;
        #print "$sum";
        $map{"$lname, $fname ($jmbag)"} = $sum;
        push @values, $sum;
    }
    #print "end of while\n";
}

for my $key (sort { $map{$b} <=> $map{$a} } keys %map) {
    print "$key: $map{$key}\n";
}