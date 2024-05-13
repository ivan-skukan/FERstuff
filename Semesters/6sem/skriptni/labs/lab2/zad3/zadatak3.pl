my %dates;

while (defined(my $line = <>)) {
    chomp($line);
    if ($line =~ /\[(\d{2}\/\w+\/\d{4}):(\d{2}):\d{2}:\d{2} /) {
        $dates{$1}{$2}++;
    }
}

for my $date (sort keys %dates) {
    print "Datum: $date\n";
    print "sat: broj pristupa\n";
    print "-----------------\n";
    for my $hour (sort keys %{$dates{$date}}) {
        #print "$date $hour:00 - $hour:59: $dates{$date}{$hour}\n";
        print "$hour: $dates{$date}{$hour}\n";
    }
    print "\n";
}
