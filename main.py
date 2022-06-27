from datetime import datetime

hora_fin_jornada = datetime.now().strftime('%Y-%m-%d') + ' 19:00:00' # Fecha de ese día + hora a la que finaliza la jornada

hora_final = datetime.strptime(hora_fin_jornada, '%Y-%m-%d %H:%M:%S') # De String a formato fecha para poder operar

hora_actual = datetime.now() #Fecha y hora en tiempo real

diferencia = hora_final - hora_actual

if (hora_actual > hora_final): # Si la hora actual es posterior a las 19:00
    print("Tu jornada laboral ha finalizado")
else:
    hora_salida = diferencia.seconds // 3600 # Horas que quedan hasta las 19:00
    minutos_salida = (diferencia.seconds % 3600 ) // 60 # Minutos que quedan hasta las 19:00
    segundos_salida = (diferencia.seconds % 3600 ) % 60 # Segundos que quedan hasta las 19:00
    print("Quedan", hora_salida, "horas", minutos_salida, "minutos y", segundos_salida, "segundos para finalizar la jornada laboral.")