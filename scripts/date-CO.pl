#!/usr/bin/env perl

use strict;
use warnings;

use v5.20;

use File::Slurp::Tiny qw(read_file);

my $file_name = shift || "contaminAND-gr-congresos.csv";

my @rows = split("\n",read_file($file_name));

die "No file" if !@rows;

shift @rows; # Headers

say "day,CO";
while (my $line = shift @rows) {
  my @data = split(",", $line );
  my ($day, $foo ) = split("T",$data[0]);
  say "$day,$data[2]" if $data[2];
}
