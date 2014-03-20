use Lingua::EN::Numbers qw(num2en num2en_ordinal);

#build the string
$total;
for($count = 1; $count <= 1000; $count++){
	$words = num2en($count);
	#remove whitespaces and hyphen
	$words =~ s/[\s\-]//g;
	$total += length($words);
}
print "$total \n";
