import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

print(dataFrameAsistencia['estado'].unique)
print(dataFrameAsistencia['estrato'].unique)
print(dataFrameAsistencia['medio_transporte'].unique)

#Filtros y condiciones para transformar datos

#1. Reportar todos los estudiantes que asistieron
estudintesQueAsistieron=dataFrameAsistencia.query('estado=="asistio"')
print(estudintesQueAsistieron)
#2. Reportar todos los estudiantes que no asistieron
#3. Reportar todos los estudiantes que llegaron tarde(Justificado)
#4. Reportar todos los estudiantes de estrato 1
estudiantesEstratoUno=dataFrameAsistencia.query('estrato==1')
print (estudiantesEstratoUno)
#5. Reportar todos los estudiantes de estratos altos
#6. Reportar todos los estudiantes que llegan en metro
estudiantesQueUsanMetro=dataFrameAsistencia.query('medio_transporte=="metro"')
print(estudiantesQueUsanMetro)
#7. Reportar todos los estudiantes que llegan en bicicleta
#8. Reportar todos los estudiantes que no caminan para llegar a la universidad
estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_trasporte!="a pie"')
print(estudiantesQueNoCaminan)
#9. Reportar todos los registros de asisitencia del mes de Junio
#10. Reportar los estudiantes que faltaron y usan bus para llegar a la universidad
EstudiantesQueFaltanUsanBus=dataFrameAsistencia.query('medio_transporte=="bus and estado=="inasistencia"')
print(EstudiantesQueFaltanUsanBus)
#11. Reportar los estudiantes que usan bus y son de estratos altos
#12. Reportar los estudiantes que usan bus y son de estratos bajos
#13. Reportar los estudiantes que llegan tarde y son de estrato 3, 4, 5 o 6
#14. Reportar los estudiantes que usan transportes ecologicos
#15. Reportar los estudiantes que faltan y usan carro para transportarse
#16. Reportar los estudiantes que asisten son estratos altos y caminan 
#17. Reportar los estudiantes que son estratos bajos y justifican su inasistencia
#18. Reportar los estudiantes que son estratos altos y justifican su inasistencia
#19. Reportar los estudiantes que usan carro y justifican su inasistencia
#20. Reportar los estudiantes que faltan y usan metro y son estratos medios

#Agrupaciones y conteos sobre los datos

#1. necesito contar cada registro de asistencia por cada estado
conteoDeRegistrosPorEstado=dataFrameAsistencia.groupby ('estado').size()
print(conteoDeRegistrosPorEstado)
#2. numero de registro por estrato
conteoDeRegistrosPorEstrato=dataFrameAsistencia.groupby ('estrato').size()
print(conteoDeRegistrosPorEstrato)
#3. cantidad de estudiantes por medio de transporte
#4. cantidad de registro por grupo
#5. necesito un cruce entre estado y medio de transporte
cruceEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()
print(cruceEstadoMedioTransporte)
#6. promedio de estrato por estado de asistencia
promedioEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].mean()
#7. estrato promedio por medio de transporte

#8. maximo estrato por estado de asistencia
#9. minimo estrato por estado de asistencia
#10. conteo de asistencia por grupo y por estado
#11. transporte usado por cada grupo
#12. cuantos grupos distintos registraron asistencia por fecha
#13. necesito promedio de estrato por fecha
#14. numero de tipo de estado por transporte
#15. neceito el primer registro de cada grupo