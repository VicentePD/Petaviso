
def alerta_avisos():
  from datetime import date,timedelta
  hj = date.today()
  qtd = 0
  msg=""
  diferenca = timedelta(days=365)
  rows = db((db.avisos.id_pet == db.pets.id ) &  (db.avisos.status == True)   &  (db.avisos.dt_fim_controle >= hj ) & (db.pets.id_usr == auth.user.id )).select()
  for row in rows:
    diferenca_temp = row('avisos.dt_fim_controle')-hj
    if diferenca_temp < diferenca:
       diferenca = diferenca_temp
    qtd = qtd+1
  if diferenca.days == 0 and qtd >=1 :
      msg = "Existem Alertas Vencendo hoje!"
  else :
      if diferenca.days > 1 and qtd >=1:
        msg = "Existem Alertas Vencendo em %s dias!" %diferenca.days
      else:
        msg = "" 

  return msg   
