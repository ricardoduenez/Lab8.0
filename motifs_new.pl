# This script will find the motifs in a DNA sequence
# While executing this script it asks for the file name of the DNA sequence. If the sequence file is not available in the same directory of this script, enter the name of the file along with the path.  eg.In windows: c:\dnafile.txt, In Linux: /home/user/sequence/dnafile.txt
print "\n\n\t\#################### motifs in  DNA SEQUENCE #################### \n\n";
print "This script find the motifs in a DNA sequence\n\n";
print "ENTER THE FILENAME OF THE DNA SEQUENCE:= ";
$dnafilename = <STDIN>;
chomp $dnafilename;
unless ( open(dnafilename, $dnafilename) ) {
print "Cannot open file
\"$dnafilename\"\n\n";
exit;
}
@protein = <dnafilename>;
close dnafilename;
$protein = join( '', @protein);
$protein =~ s/\s//g;
do {
print "ENTER A MOTIF {Sequence} TO SEARCH FOR :=
";
$motif = <STDIN>;
chomp $motif;
if ( $protein =~ /$motif/ ) {
print "Found it!\n\n";
exit;
} else {
print "Not found.\n\n";
exit;
}
} until ( $motif =~ /^\s*$/ );