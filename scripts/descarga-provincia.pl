#!/usr/bin/env perl

use strict;
use warnings;
use v5.20;

use Mojo::DOM;
use LWP::Simple;
use File::Slurp::Tiny qw(write_file);
use JSON;
use DateTime;


my @provincias = qw(al ca ma gr se co hu ja);

my %provincias = map { $_ => 1 } @provincias;

my @meses = qw(ene feb mar abr may jun jul ago sep oct nov dic);

my $provincia = shift || "gr";

my $current = DateTime->new(
    day   => 1,
    month => 1,
    year  => 2017,
);

my $stop = DateTime->new(
    day   => 3,
    month => 3,
    year  => 2017,
);

my @datos;

while ( $current < $stop ) {
  my $year = substr $current->strftime('%Y'), 2, 4;
  my $mes = $current->strftime('%m');
  my $dia = $current->strftime('%d');
  my $date =  $year.$mes.$dia;
  #printf "Descargando informacion de ngr%s\n", $date;
  
  my $url = "http://www.juntadeandalucia.es/medioambiente/atmosfera/informes_siva/$meses[$mes-1]$year/n$provincia$date.htm";
  
  my $content = get( $url );
  
  if    ( $content )  {
    my $dom = Mojo::DOM->new( $content );
    my @tables = $dom->find('table')->each;
    
    shift @tables; #Primera tabla con leyenda
    
    my $fecha = "$current";
    
    while ( @tables ) {
      my $metadatos = shift @tables;
      my $datos = shift @tables;
      
      my @metadatos = ( $metadatos =~ /<b>.([A-Z][^<]+)/g);
      my $this_metadata = { date => $fecha };
      for my $k (qw(provincia municipio estacion direccion)) {
	$this_metadata->{$k} = shift @metadatos;
      }
      
      my @filas = $datos->find('tr')->each;
      
      shift @filas; #Cabecera
      pop @filas;
      for my $f (@filas) {
	my @columnas = $f->find('td')->map('text')->each;
	my %these_medidas = %{$this_metadata};
	my $fecha_hora = shift @columnas;
	my ($hora) = ($fecha_hora =~ /(\d+:\d+)/);
	$these_medidas{'date'} =~ s/00:00/$hora/;
	for my $c (qw(SO2 PART NO2 CO O3)) {
	  $these_medidas{$c} = shift @columnas;
	}
	push @datos, \%these_medidas;
      }
    }
  }
  
  $current = $current->add(days => 1) ;
}


write_file( "contaminAND-$provincia.json", encode_json \@datos );


			     
