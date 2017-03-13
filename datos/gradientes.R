library("entropy")
library("ggplot2")
library("ggthemes")
datos.CO<-read_csv("~/Proyectos/Otros/contaminaAnd/contaminAND/datos/contaminAND-gr-conjunto.csv", 
         col_types = cols(CO.congresos = col_number(), 
                          CO.norte = col_number()), na = "NA")
number_data.datos.CO<- nrow(datos.CO)
datos.gradiente.CO <- data.frame(congresos= numeric(0), norte= numeric(0), percert.congresos=numeric(0),percent.norte=numeric(0),original.congresos.ant=numeric(0),original.norte.ant=numeric(0),original.congresos=numeric(0),original.norte=numeric(0))

#for en datos.co para añadir a datos.gradiente.co
for(i in 2:number_data.datos.CO){ 
  data.Cong.ant<-datos.CO$CO.congresos[i-1];
  data.Nort.ant<-datos.CO$CO.norte[i-1];
  data.Cong<-datos.CO$CO.congresos[i];
  data.Nort<-datos.CO$CO.norte[i];
  if (! is.na(data.Cong.ant) && ! is.na(data.Nort.ant) && ! is.na(data.Cong) && ! is.na(data.Nort) ){

    diferencia.Cong<-data.Cong-data.Cong.ant;
    diferencia.Nort<-data.Nort-data.Nort.ant;
    
    diferencia.Cong.percent<-diferencia.Cong*100/data.Cong.ant;
    diferencia.Nort.percent<-diferencia.Nort*100/data.Nort.ant;
    nueva_fila<-c(diferencia.Cong,diferencia.Nort,diferencia.Cong.percent,diferencia.Nort.percent,data.Cong.ant,data.Nort.ant,data.Cong,data.Nort )
    datos.gradiente.CO[nrow(datos.gradiente.CO) + 1, ] <- nueva_fila;
    print(i)
  }

} 

#guardamos tabla 

write.csv(datos.gradiente.CO, file = "datos.gradiente.CO.csv")
ggplot(datos.gradiente.CO,aes(x=percent.norte,y=percert.congresos,color=abs(congresos),size=abs(norte)))+geom_point()+scale_colour_distiller(palette='Spectral')

