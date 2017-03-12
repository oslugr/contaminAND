library("entropy")
library("ggplot2")
library("ggthemes")

datos.dia.CO <- read.csv("contaminAND-gr-conjunto-date-CO.csv", fileEncoding="latin1")
datos.dia.CO$day <- as.factor(datos.dia.CO$day)
datos.dia.CO$CO.congresos <- as.numeric(datos.dia.CO$CO.congresos)
datos.dia.CO$CO.norte <- as.numeric(datos.dia.CO$CO.norte)
entropies.CO <-   as.data.frame(as.table(with(datos.dia.CO,tapply(CO.congresos,day,entropy))))
median.CO.con <- as.data.frame(as.table(with(datos.dia.CO,tapply(CO.congresos,day,median))))
median.CO.nor <- as.data.frame(as.table(with(datos.dia.CO,tapply(CO.norte,day,median))))
                                
                      
entropy.mean <- data.frame( day=as.Date(entropies.CO$Var1),
                           median.CO.con=median.CO.con$Freq,
                           median.CO.nor=median.CO.nor$Freq,
                           entropy = entropies.CO$Freq)
ggplot(entropy.mean,aes(x=median.CO.nor,y=median.CO.con,color=entropy))+geom_point()

