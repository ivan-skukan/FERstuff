#use locale;
use utf8;
use open ':encoding(UTF-8)', ':std';

my $prefix_length = pop @ARGV;
my %prefixes;

while (defined(my $line = <>)) {
    $line =~ s/[[:punct:]]/ /g; # Remove punctuation
    my @words = split /\s+/, $line; # Split the line into words

    for my $word (@words) {
        $word = lc $word; # Convert the word to lowercase
        if (length $word < $prefix_length) { next; } 
        my $prefix = substr $word, 0, $prefix_length; 

        if (exists $prefixes{$prefix}) {
            $prefixes{$prefix}++; # Increment the count
        } else {
            $prefixes{$prefix} = 1; # Initialize the count
        }
    }
}

# Sort the keys of %prefixes and print each prefix and its count
for my $prefix (sort keys %prefixes) {
    print "$prefix: $prefixes{$prefix}\n";
}