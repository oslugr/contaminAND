#!/usr/bin/env perl

use strict;
use warnings;
use v5.20;

use Mojo::DOM;
use LWP::Simple;
use File::Slurp::Tiny qw(write_file);
use JSON;
use DateTime;

my $start = DateTime->new(
    day   => 1,
    month => 2,
    year  => 2017,
);

my $stop = DateTime->new(
    day   => 18,
    month => 2,
    year  => 2017,
);

my %sMes = (
    '01' => "ene",
    '02' => "feb",
    '03' => "mar",
    '04' => "abr",
    '05' => "may",
    '06' => "jun",
    '07' => "jul",
    '08' => "ago",
    '09' => "sep",
    '10' => "oct",
    '11' => "nov",
    '12' => "dic",
);

while ( $start->add(days => 1) < $stop ) {
    my $year = substr $start->strftime('%Y'), 2, 4;
    my $mes = $start->strftime('%m');
    my $dia = $start->strftime('%d');
    my $date =  $year.$mes.$dia;
    #printf "Descargando informacion de ngr%s\n", $date;

    my $path = 'http://www.juntadeandalucia.es/medioambiente/atmosfera/informes_siva/'.$sMes{$mes}.$year.'/ngr'.$date.'.htm';
    printf "URL: %s\n",$path;

}

my $url = shift || 'http://www.juntadeandalucia.es/medioambiente/atmosfera/informes_siva/feb17/ngr170201.htm';

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


			     
