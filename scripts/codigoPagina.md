##Web Medio Ambiente Junta de Andalucía    

Informes diarios (Desde el 1 de enero de 1998) 
  
http://www.juntadeandalucia.es/medioambiente/site/portalweb/menuitem.7e1cf46ddf59bb227a9ebe205510e1ca/?vgnextoid=7e612e07c3dc4010VgnVCM1000000624e50aRCRD&vgnextchannel=948a445a0b5f4310VgnVCM2000000624e50aRCRD&lr=lang_es  


'''
 <div class="apartado"><SCRIPT LANGUAGE="JavaScript">

var IE4, ObjetoFormularioDia, ObjetoFormularioMes;
var uerreele = "http://www.juntadeandalucia.es/medioambiente/atmosfera/informes_siva/";
var fecha_hoy, fecha_minima;

var array_meses = new Array ();

function tipo_mes (nombre, dias)
{
	this.nombre = nombre;
	this.dias = dias;
}


function crea_array_meses ()
{
   
	array_meses [0] = new tipo_mes ("ene", 31);
	array_meses [1] = new tipo_mes ("feb", 28);
	array_meses [2] = new tipo_mes ("mar", 31); 
	array_meses [3] = new tipo_mes ("abr", 30); 
	array_meses [4] = new tipo_mes ("may", 31);
	array_meses [5] = new tipo_mes ("jun", 30); 
	array_meses [6] = new tipo_mes ("jul", 31); 
	array_meses [7] = new tipo_mes ("ago", 31); 
	array_meses [8] = new tipo_mes ("sep", 30); 
	array_meses [9] = new tipo_mes ("oct", 31);
	array_meses [10] = new tipo_mes ("nov", 30); 
	array_meses [11] = new tipo_mes ("dic", 31);
}


function arranque ()
{
	var version = parseInt (navigator.appVersion);
	var nombre = navigator.appName;
	
	IE4 = (version>=4 && nombre=="Microsoft Internet Explorer") ? 1 : 0;
	//ObjetoFormularioDia = (IE4) ? 'form_dia' : 'document.form_dia';
	ObjetoFormularioDia = 'document.form_dia';
	crea_array_meses ();
	fecha_hoy=new Date();
	ayer_milis=fecha_hoy.getTime()-(1000*60*60*24); //le quito un dia a hoy
	fecha_ayer=new Date(ayer_milis);
	
	anyo=''+fecha_ayer.getYear(); //puede venir con 4 digitos
	anyo=anyo.substring(anyo.length-2);
	eval (ObjetoFormularioDia + '.DIA.value = fecha_ayer.getDate ()');
	eval (ObjetoFormularioDia + '.MES.value = fecha_ayer.getMonth () + 1');
	eval (ObjetoFormularioDia + '.ANO.value = anyo');
	 
	fecha_minima = new Date (1998, 0, 1);
}


   
function comprueba_valor (valor, minimo, maximo)
{
		return ((valor < minimo || valor > maximo)  ? false : true);
}


function obtenerValorSeleccionado (ObjetoFormulario, nombreLista)
{
   lista = eval (ObjetoFormulario + '.' + nombreLista);
      	   
   if (IE4)
   {
   		 return (lista.options.value);
   	}     	   	
   	else
   	{
   		 indice_seleccionado = lista.selectedIndex;
   	     return (lista.options [indice_seleccionado].value);
   	}     
}  



function obtenerValorPulsado (nombreRadio)
{
	radio = eval (ObjetoFormularioDia + '.' + nombreRadio)
	encontrado=false;
  	for (i = 0; i < radio.length && !encontrado; i++)
  	{ 
		if (radio [i].checked)
		{
			encotrado = true;
			valor = radio [i].value;
		}
	}
	return valor;
}

 

function proceso_dia ()
{
	 var text_ano = eval (ObjetoFormularioDia + '.ANO');
	 var text_mes = eval (ObjetoFormularioDia + '.MES');
	 var text_dia = eval (ObjetoFormularioDia + '.DIA');
	 
	 num_ano = text_ano.value;
	 num_mes = text_mes.value;
	 num_dia = text_dia.value;	  	  	   	 	  
	  
         if (num_ano.length < 2) num_ano = "0" + num_ano;

	 ano_aux = (num_ano < 50) ? "20" + num_ano : "19" + num_ano;
	  
	 var fecha_usuario = new Date (ano_aux, num_mes - 1, num_dia); 
  	
    // if (num_ano % 4 == 0)
	if ((num_ano%4==0&&!num_ano%100==0)||num_ano%400==0)
        array_meses [1].dias = 29;
		
     if (comprueba_valor (num_mes, 1, 12) && comprueba_valor (num_dia, 1, array_meses [num_mes-1].dias))
     { 
	 	d=fecha_hoy;
		//le quito los milisegundos
		fecha_hoy=new Date((d.getMonth()+1)+"/"+d.getDate()+"/"+d.getFullYear());
 		//alert(fecha_usuario+" - "+fecha_hoy);
       //if (fecha_usuario <= fecha_hoy && fecha_usuario > fecha_minima)    	
        if (fecha_usuario < fecha_hoy && fecha_usuario >= fecha_minima)    	
        {
            nombre_mes = array_meses [num_mes - 1].nombre;
 
            provincia = obtenerValorSeleccionado (ObjetoFormularioDia,"PROVINCIA");
            tipo = obtenerValorPulsado ("TIPO");     
  
            directorio = nombre_mes + num_ano + "/";

            if (num_dia.length < 2) num_dia = "0" + num_dia;
            if (num_mes.length < 2) num_mes = "0" + num_mes;	
            if (num_ano.length < 2) num_ano = "0" + num_ano;
 	
			//informes completos desde 1/11/2004							
			fecha_control=new Date("11/01/2004");
			ext=(fecha_usuario<fecha_control)? ".txt" : ".htm";
            //nombre_fichero = tipo + provincia + num_ano + num_mes + num_dia + ".txt";
            nombre_fichero = tipo + provincia + num_ano + num_mes + num_dia + ext;
   
            location.href = uerreele + directorio + nombre_fichero;
         }
         else
            alert ("Lo sentimos. No disponemos de esos datos");
	}
	else
	   alert ("Fecha incorrecta");	
}


function proceso_mes ()
{
	 var num_ano = obtenerValorSeleccionado (ObjetoFormularioMes, "M_ANO");	 
	 var num_mes = obtenerValorSeleccionado (ObjetoFormularioMes, "M_MES");
	 
         directorio = "meses" + num_ano + "/";
  	 
	 nombre_fichero = "IMA" + num_ano + num_mes + ".DOC";	

         location.href = uerreele + directorio + nombre_fichero;
}
</SCRIPT>
'''

