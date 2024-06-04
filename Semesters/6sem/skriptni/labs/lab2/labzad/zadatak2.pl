my $filename = $ARGV[0];

open(my $fh, '<:encoding(UTF-8)', $filename);

my %count;

while (my $row = <$fh>) {
    #chomp $row;
    #print "$row\n";
    if ($row =~ /^From: .+<(.+@.+)>$/) {
        #print "$1\n";
        $count{$1}++;
    }
}

foreach my $email (sort { $count{$a} <=> $count{$b} } keys %count) {
    printf ("%40s %s (%d)\n", $email, '*' x $count{$email}, $count{$email});
}

close($fh);