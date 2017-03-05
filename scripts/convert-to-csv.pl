#!/usr/bin/env perl

use strict;
use warnings;

use v5.20;

use File::Slurp::Tiny qw(read_file write_file);
use JSON;

my $file_name = shift || "contaminAND-gr-congresos.json";

my $file = read_file( $file_name );

my $datos = decode_json( $file );

say "date,NO2,CO,PART,O3,SO2";

for my $m (@$datos) {
  if ($m->{'date'} ne '' ) {
    say "$m->{'date'},$m->{'NO2'},$m->{'CO'},$m->{'PART'},$m->{'O3'},$m->{'SO2'}";
  }
}
