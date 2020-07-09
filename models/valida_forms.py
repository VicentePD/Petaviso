def valida_form_aviso(form):
   
    if form.vars.qtd_dias_primeiro_aviso > form.vars.duracao :
       form.errors.qtd_dias_primeiro_aviso = 'Quantidade de Dias do Primeiro aviso inválido !'
 