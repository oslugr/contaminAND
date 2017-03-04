#!/usr/bin/env perl

use strict;
use warnings;
use v5.20;

use Mojo::DOM;
use LWP::Simple;
use File::Slurp::Tiny qw(write_file);
use Date::Calendar;
use Date::Calendar::Profiles qw( $Profiles );

use JSON;

my @provincias = qw(al ca ma gr se co hu ja);

my %provincias = map { $_ => 1 } @provincias;

my @meses = qw(ene feb mar abr may jun jul ago sep oct nov dic);

my $provincia = shift || "gr";

die "No existe esa provincia $provincia" if ! $provincias{$provincia};

my $calendar = Date::Calendar->new( $Profiles->{'ES-ES'} );
for my $y ( 1998..2016 ) {
    my $digits = $y % 100;
    my $this_year = $calendar->yea
    for (my $i = 0; $i <= $#meses; $i ++ ) {

	my $num_mes = sprintf( "%02d", $i+1);
	my $mes = $meses[$i];

	
	my $url = shift || 'http://www.juntadeandalucia.es/medioambiente/atmosfera/informes_siva/$mes$digits/n$provincia$digits$num_mes01.htm';


my $content = get( $url );

if    ( !$content )  {
  die "No puedo descargar $url";
}

my $dom = Mojo::DOM->new( $content );
my @tables = $dom->find('table')->each;

shift @tables; #Primera tabla con leyenda

my @datos;
while ( @tables ) {
  my $metadatos = shift @tables;
  my $datos = shift @tables;

  my @metadatos = ( $metadatos =~ /<b>.([A-Z][^<]+)/g);
  my $this_metadata;
  for my $k (qw(provincia municipio estacion direccion)) {
    $this_metadata->{$k} = shift @metadatos;
  }

  my @filas = $datos->find('tr')->each;

  shift @filas; #Cabecera
  my @medidas;
  for my $f (@filas) {
    my @columnas = $f->find('td')->map('text')->each;
    my $these_medidas;
    for my $c (qw(hora SO2 PART NO2 CO O3)) {
      $these_medidas->{$c} = shift @columnas;
    }
    push @medidas, $these_medidas;
  }
  pop(@medidas);
  push @datos, { meta => $this_metadata,
		 medidas => \@medidas };
}

my ($mesyear,$sitio,$dia) = ($url =~ m{/(\w+)/n(\w{2})\d{4}(\d{2})\.htm});

write_file( "contaminAND-$sitio-$mesyear-$dia.json", encode_json \@datos );


			     
