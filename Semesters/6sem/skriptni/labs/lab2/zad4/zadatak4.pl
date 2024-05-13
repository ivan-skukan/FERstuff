use Time::Piece;
$^W = 0;

while (defined(my $line = <>)) {
    chomp($line);
    #print "here1\n";
    if ($line =~ /([^;]*);([^;]*);([^;]*);([^ ]*)[ ]([^ ]*)[ ]([^ ]*)[ ][^;]*;([^ ]*)[ ]([^;]*)/) {
        $jmbag = $1;
        $lname = $2;
        $fname = $3;
        $termdate = $4;
        $termstart = $5;
        $termend = $6;
        $lockeddate = $7;
        $lockedtime = $8;
     
        ($starth, $startmin) = $termstart =~ /(\d{2}):(\d{2})/;
        ($lockh, $lockmin, $locks) = $lockedtime =~ /(\d{2}):(\d{2}):(\d{2})/;

        if ($termdate ne $lockeddate || ($lockh gt $starth && $lockmin gt $startmin) || ($lock eq $starth && $lockmin gt $startmin)) {
            print "$jmbag $lname $fname - PROBLEM: $termdate $termstart --> $lockeddate $lockedtime\n";
            #last;
        }
        #last;
    }

}  