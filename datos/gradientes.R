library("entropy")
library("ggplot2")
library("ggthemes")
library("readr")
library("svglite")
datos.CO<-read_csv("contaminAND-gr-conjunto.csv", 
         col_types = cols(date= col_datetime(),CO.congresos = col_number(), 
                          CO.norte = col_number()), na = "NA")
number_data.datos.CO<- nrow(datos.CO)
datos.CO.filtros<-datos.CO[complete.cases(datos.CO),]
datos.CO.filtros$date <- NULL 
number_data.datos.CO.filtros<- nrow(datos.CO.filtros)
datos.CO.filtros2<- datos.CO.filtros[1:(number_data.datos.CO.filtros-1),]
datos.CO.filtros3<- datos.CO.filtros[-1,]
#datos.gradiente.CO <- data.frame(congresos= numeric(0), norte= numeric(0), percert.congresos=numeric(0),percent.norte=numeric(0),original.congresos.ant=numeric(0),original.norte.ant=numeric(0),original.congresos=numeric(0),original.norte=numeric(0))
datos.gradiente.CO<-data.frame(diff(as.matrix(datos.CO.sinna)),datos.CO.filtros2,datos.CO.filtros3)
datos.gradiente.CO$percent.congresos<-datos.gradiente.CO$CO.congresos*100/datos.gradiente.CO$CO.congresos.1;
datos.gradiente.CO$percent.norte<-datos.gradiente.CO$CO.norte*100/datos.gradiente.CO$CO.norte.1;


#guardamos tabla 

write.csv(datos.gradiente.CO, file = "datos.gradiente.CO.csv")
ggplot(datos.gradiente.CO,aes(x=percent.norte,y=percent.congresos,color=abs(CO.congresos),size=abs(CO.norte)))+geom_point()+scale_colour_distiller(palette='Spectral')

ggsave("gradientes.png")
ggsave("gradientes.svg")
