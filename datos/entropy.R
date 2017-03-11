library("entropy")
library("ggplot2")
library("ggthemes")
library(data.table)

datos.dia.CO <- read.csv("contaminAND-gr-congresos-CO.csv", fileEncoding="latin1")
datos.dia.CO$day <- as.factor(datos.dia.CO$day)
datos.dia.CO$CO <- as.number(datos.dia.CO$CO)
entropies.CO <- as.data.frame(as.table( with(datos.dia.CO,tapply(CO,day,entropy))))
mean.CO <- as.data.frame(as.table(with(datos.dia.CO,tapply(CO,day,mean))))
entropy.mean <- data.frame( day=as.date(entropies.CO$Var1),
                           mean.CO=mean.CO$Freq,
                           entropy = entropies.CO$Freq)ç
ggplot(entropy.mean,aes(x=day,y=mean.CO))+geom_point()
ggplot(entropy.mean,aes(x=day,y=entropy))+geom_point()
ggplot(entropy.mean,aes(x=mean.CO,y=entropy))+geom_point()
