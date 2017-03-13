#!/usr/bin/env perl

use strict;
use warnings;

use v5.20;

use File::Slurp::Tiny qw(read_file);

my $file_name = shift || "../datos/contaminAND-gr-conjunto.csv";

my @rows = split("\n",read_file($file_name));

die "No file" if !@rows;

shift @rows; # Headers

say "day,CO.congresos,CO.norte";
while (my $line = shift @rows) {
  my @data = split(",", $line );
  my ($day, $foo ) = split("T",$data[0]);
  say "$day, ",join(",",@data[1,2]);
}
