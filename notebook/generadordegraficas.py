import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataFrameAsistencia = pd.read_csv('./data/asistencia_estudiantes_completo.csv')

#GRAFICANDO 
#GRAFICA DE BARRAS
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF69B4']
plt.figure(figsize=(8, 5))
sns.countplot(data=dataFrameAsistencia, x='estado', palette=colors)
plt.title('Cantidad de registros por estado de asistencia')
plt.xlabel('Estado de asistencia')
plt.ylabel('Cantidad de registros')
plt.tight_layout()
plt.show()

#GRAFICA DE TORTAS
#MOSTRAR PROPORCIONES ENTRE DOS COLUMNAS DEL PDF (proporcion de estudiantes x MEDIO DE TRANSPORTE)

conteoMedioTransporte = dataFrameAsistencia['medio_transporte'].value_counts()

plt.figure(figsize=(5, 5))
plt.pie(
    conteoMedioTransporte, 
    labels=conteoMedioTransporte.index, 
    autopct='%1.1f%%',
    colors=sns.color_palette("Blues")     
)
plt.title('Proporción de estudiantes por medio de transporte')
plt.tight_layout()
plt.show()

#GRAFICA DE baras agrupadas
#SE APLICA CUANDO HICE CRUCE EN EL DATAFRAME

conteoMedioTransporteEstado = dataFrameAsistencia.groupby([ 'estado','medio_transporte']).size().unstack(fill_value=0)

conteoMedioTransporteEstado.plot(kind='bar',
                                 figsize=(10,6), 
                                 color=colors)

plt.title('Registros por estado de asistencia y medio de transporte')
plt.xlabel('Estado de asistencia')
plt.ylabel('Cantidad de registros')
plt.legend(title='Medio de transporte')
plt.tight_layout()
plt.show()