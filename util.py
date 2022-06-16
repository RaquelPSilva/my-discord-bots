from datetime import datetime, timedelta

def proxima_data(dia_semana, fuso):
  dia_semana_atual = datetime.now().weekday()
  proxima = datetime.now(fuso)
  if dia_semana_atual > dia_semana:
    delta_procurado = 7 - dia_semana_atual + dia_semana
  else:
    delta_procurado = dia_semana - dia_semana_atual
  proxima = proxima + timedelta(days = delta_procurado)
  return proxima