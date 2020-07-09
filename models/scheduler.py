
from gluon.scheduler import Scheduler


def envia_aviso():
  # Recuperar avisos para enviar e-mail
  print("inicioooooo")
  from datetime import date, timedelta
  hj = date.today()
  rows = db((db.avisos.id_pet == db.pets.id) &
            (db.avisos.status == True)).select()
  for row in rows:
    # Calcular a data relativa para envio do aviso.
    dt_inicio_aviso = row('avisos.dt_fim_controle') - \
                          timedelta(days=row('avisos.qtd_dias_primeiro_aviso'))
    print('Data Termino %s  Data Inicio %s' %  (row('avisos.dt_fim_controle'), dt_inicio_aviso )  )

    if  row('avisos.dt_fim_controle') >= hj and dt_inicio_aviso <= hj:
      donos = db(db.auth_user.id == row('pets.id_usr') ).select()
      for dono in donos:
        msg = "Prezados(as). \r Lembrete automático do sistema PetAviso.  \r O alerta cadastrado %s, para o seu pet %s , com vencimento dia dia %s \r\r %s" \
        %(row('avisos.nome_controle') ,row('pets.nome') ,row('avisos.dt_fim_controle'),row('avisos.texto') )
        ret = envia_email( dono.email,'Aviso Automático do Sistema PetAviso',msg)
        print("ID - %s" %row('avisos.id'))
        print("Status %s" %ret)
        db.avisos_enviados.insert(id_avisos=row('avisos.id') ,data_envio=hj, status=ret)
        db.commit()
  return ret
  
def envia_email(para,assunto,mensagem):
  
  ev= mail.send(to=[para],  subject=assunto,
       # reply_to='contato_para_responder@email.com', # pode ser omitido
        message=mensagem
        )
  if ev:
    return 'Sucesso'
  else:
    return 'erro'

# scheduler = Scheduler(db,dict(envia_aviso=envia_aviso), migrate=False)
# def f():
 #   import time
  #  t=time.ctime()
   # open('tmp/tasks','w').write(t+'\n')
    # return t

# scheduler = Scheduler(db, tasks=dict(demo1=f), migrate=True)
# Scheduler(db,dict(our_function =f))
# scheduler.queue_task(, pvars=dict(a=1, b=2))
