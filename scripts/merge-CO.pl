#!/usr/bin/env perl

use strict;
use warnings;
use Carp;
use DateTime; 
use DateTime::Format::ISO8601;
use DateTime::Format::Strptime;

use v5.20;

use File::Slurp::Tiny qw(read_file);

my $file_name = shift || "../datos/contaminAND-gr-congresos.csv";
my $another_file_name = shift || "../datos/contaminAND-gr-norte.csv";

my ($start_1, $end_1, $hash_1) = hash_CO( $file_name );
my ($start_2, $end_2, $hash_2) = hash_CO( $another_file_name );

say "date,CO.congresos,CO.norte";
my $start = ($start_1 > $start_2)?$start_1:$start_2;
my $end = ($end_1 < $end_2)?$end_1:$end_2;

for (my $d = $start; $d <= $end; $d = $d->add(minutes => 10)) {
  if ( $hash_1->{$d} &&  $hash_2->{$d} ) {
    say "$d, $hash_1->{$d}, $hash_2->{$d}";
  }
}


    
sub hash_CO {
    my $file_name = shift;
    
    my @rows = split("\n",read_file($file_name));
    
    croak "No file" if !@rows;
    
    shift @rows; # Headers
    
    my %CO;
    my $start_date = (split(",", $rows[0]))[0];
    my $end_date = (split(",", $rows[$#rows]))[0];
    while (my $line = shift @rows) {
	my @data = split(",", $line );
	$CO{$data[0]} = $data[2];
      
    };
    return DateTime::Format::ISO8601->parse_datetime($start_date),
      DateTime::Format::ISO8601->parse_datetime($end_date),
      \%CO;
    
}
    
