import pandas as pd
from bokeh.io import curdoc,output_file,show
from bokeh.models.widgets import Panel,Tabs
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource


def a_datetimeformat(row):
    return pd.to_datetime(row['FECHA-HORA'].replace('-',' ').replace('/','-'),dayfirst = True)
    




DF = pd.read_csv('Contaminacion_Congresos_febrero.csv',index_col = 'Unnamed: 0')
DF['FECHA-HORA']= DF.apply(a_datetimeformat,axis=1)
print(DF)
################################
##Visualizacion

source_SO2  = ColumnDataSource(DF)
source_PART = ColumnDataSource(DF)
source_NO2  = ColumnDataSource(DF)
source_CO   = ColumnDataSource(DF)
source_O3   = ColumnDataSource(DF)

main_plot = figure(plot_width = 1600,plot_height = 600,x_axis_type='datetime',
                   title = 'Calidad del aire Granada: Palacio de Congresos. FEB 2017')

main_plot.line (x = 'FECHA-HORA',y = 'NO2', source = source_NO2,color = 'blue',legend = 'NO2_')
main_plot.line (x = 'FECHA-HORA',y = 'SO2', source = source_SO2,color = 'red', legend = 'SO2_')
##main_plot.line (x = 'FECHA-HORA',y = 'CO', source = source_CO,color = 'green')
main_plot.line (x = 'FECHA-HORA',y = 'PART', source = source_PART,color = 'orange', legend = 'PART_')
main_plot.line (x = 'FECHA-HORA',y = 'O3', source = source_O3,color = 'brown', legend = 'O3_')


tab_general = Panel(child = main_plot, title = 'Plataforma de analisis de contaminacion')
tabs = Tabs(tabs=[ tab_general])
##curdoc().add_root(tabs)
show(tabs)
output_file('Palacio_Congresos_Feb.html')
