

from datetime import *


def menu():
	if auth.user:
		if request.vars.p == "logou" :
			 response.flash = T("Bem Vindo %(first_name)s" % auth.user)
			 request.post_vars.p = ""
		grid = SQLFORM.grid(db.pets.id_usr == auth.user.id, showblobs=True,
			               fields=[db.pets.nome, db.pets.tipo,
			                   db.pets.data_nascimento], searchable=False,
			               create=False,
			               editable=False,
			               # selectable=(lambda ids : redirect(URL('cadastrar_peso',vars=dict(ids=id)))),
			               # selectable==,
			               ui='web2py',
			               # links_placement ='left',
			               showbuttontext=False,
			               # links = [dict(header='Virtual Field 1', body=lambda row:IMG( _src=URL('default', 'download', args=db(db.pets).select().first().img_thumbnail ))) ] ,
			               links=[dict(header='Foto', body=lambda row:IMG(_class='avatar img-responsive', _src=URL('default', 'download', args=db(db.pets.id == row.id).select().first().img_thumbnail))),
			               dict(header='', body=lambda row: A(SPAN(_class='icon pen icon-pencil glyphicon glyphicon-pencil', _id=0), _class='button btn btn-default btn-outline-primary', _title="Editar", _href=URL('editar_pet', args=[row.id], user_signature=True)) + " " +
			               A(SPAN(_class='icon balance icon-balance glyphicon glyphicon-balance', _id=1), _class='button btn btn-default btn-outline-primary', _title="Peso", _href=URL('lista_peso', args=[row.id], user_signature=True)) + " " +
			               A(SPAN(_class='icon bell icon-bell glyphicon glyphicon-bell', _id=2), _class='button btn btn-default btn-outline-primary',
			                 _title="Alertas", _href=URL('listar_avisos', args=[row.id], user_signature=True))
			                )],
			               csv=True, user_signature=True)  # btn btn-default
		# grid2= SQLFORM.smartgrid(db.pets, linked_tables=['pesos'])
		msg = alerta_avisos()
	else:
	  response.flash = T("Bem Vindo.")
	  redirect(URL(r=request, c='default', f='index'))
	  grid = ""
	return dict(message=T("%s" %msg), grid=grid)


@auth.requires_login()
def novo_pet():
    form = SQLFORM(db.pets)
    form.add_button(T('Back'), URL('menu'), _class='btn btn-danger')
    form.vars.id_usr = auth.user.id
    if form.process().accepted:
        session.flash = 'Novo Pet cadastrado: %s' % form.vars.nome
        redirect(URL('novo_pet'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)


def editar_pet():
    form = SQLFORM(db.pets, request.args(0), upload=URL('download'),
    			   buttons=[A(T("Back"), _class='btn btn-danger', _href=URL("menu")),
    			   TAG.button('Salvar', _type="submit", _class='btn btn-info')])
    # form.add_button('Voltar', URL('menu'))
    if form.process().accepted:
        session.flash = 'Novo Pet cadastrado: %s' % form.vars.nome
        redirect(URL('menu'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)


def download():
    return response.download(request, db)

@auth.requires_login()
def lista_peso():
	if request.args(0) ==  None: 
		grid2= SQLFORM.grid((db.pesos.id_pet == db.pets.id) &(db.pets.id_usr == auth.user.id) ,user_signature=True, 		
		showblobs=True,
		searchable=False,
		create=False,
		editable=False,
		showbuttontext=False,
		details=False,
		# sorter_icons=True,
		fields=[db.pesos.id_pet,db.pesos.dt_medicao,db.pesos.peso])
		bt_incluir = A( SPAN(  _class='icon plus icon-plus glyphicon glyphicon-plus', _id=0),_class='button btn btn-default btn-outline-primary',
		_title="Cadastrar Peso",_href=URL('cadastrar_peso', args=[] ,user_signature=True)) 
	else:
		grid2=grid2= SQLFORM.grid(db.pesos.id_pet == request.args(0),user_signature=True, 		
		showblobs=True,
		searchable=False,
		create=False,
		editable=False,
		showbuttontext=False,
		details=False,
		# sorter_icons=True,
		fields=[db.pesos.id_pet,db.pesos.dt_medicao,db.pesos.peso])
		bt_incluir = A( SPAN(  _class='icon plus icon-plus glyphicon glyphicon-plus', _id=0),_class='button btn btn-default btn-outline-primary',
		_title="Cadastrar Peso",_href=URL('cadastrar_peso', args=[request.args(0)] ,user_signature=True)) 
	return dict(grid=grid2,bt_incluir=bt_incluir)

@auth.requires_login()
def cadastrar_peso():
	if request.args(0) != None:
		rows = db(db.pets.id == request.args(0)).select()
	else:
		rows = db(db.pets.id_usr == auth.user.id, ).select()
	pets_sel_id = []
	pets_sel_nome = []
	for row in rows:
		pets_sel_id.append(row('pets.id'))
		pets_sel_nome.append(row('pets.nome'))

	form = SQLFORM.factory(Field('id_pet', 'list:string', requires=IS_IN_SET(pets_sel_id, pets_sel_nome), label='Pets'),
		Field('dt_medicao', 'date', label='Data da Medição',
								requires=[IS_NOT_EMPTY(),
								IS_DATE(error_message='Data Inválida')],
								default=request.now),
    	Field('peso', 'decimal(4,2)', label='Peso', requires=IS_NOT_EMPTY())
    )
    
	if form.process().accepted:
		try:
			db.pesos.insert(dt_medicao=form.vars.dt_medicao, peso=form.vars.peso, id_pet=form.vars.id_pet )
			session.flash = 'Peso cadastrado'
			redirect(URL('menu')) 
		except Exception as e:
			session.flash = 'Erro cadastrando o Peso %s' %str(e)	
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	form.add_button(T("Back"),URL('lista_peso'), _class='btn btn-danger')
	return dict(form=form)
	# requires = IS_DATE(format=T('%Y-%m-%d'),
    #               error_message='must be YYYY-MM-DD!') 
@auth.requires_login()
def listar_avisos():
	if request.args(0) != None:
		grid= SQLFORM.grid((db.avisos.id_pet == db.pets.id) &(db.pets.id_usr == auth.user.id) & (db.pets.id == request.args(0)) ,user_signature=True, 		
		showblobs=True,
		searchable=False,
		create=False,
		editable=False,
		showbuttontext=False,
		orderby=~db.avisos.dt_fim_controle,
		details=True,
		# sorter_icons=True,
		fields=[db.avisos.id_pet,db.avisos.nome_controle,db.avisos.dt_fim_controle  ]
		 )
		bt_incluir = A( SPAN(  _class='icon plus icon-plus glyphicon glyphicon-plus', _id=0),_class='button btn btn-default btn-outline-primary',
		_title="Cadastrar Aviso",_href=URL('cadastrar_aviso', args=[request.args(0)] ,user_signature=True)) 
	else:
		grid= SQLFORM.grid((db.avisos.id_pet == db.pets.id) &(db.pets.id_usr == auth.user.id) ,user_signature=True, 		
			showblobs=True,
			searchable=False,
			create=False,
			editable=False,
			showbuttontext=False,
			orderby=~db.avisos.dt_fim_controle,
			details=True,
			# sorter_icons=True,
			fields=[db.avisos.id_pet,db.avisos.nome_controle,db.avisos.dt_fim_controle  ]
		 )
		bt_incluir = A( SPAN(  _class='icon plus icon-plus glyphicon glyphicon-plus', _id=0),_class='button btn btn-default btn-outline-primary',
		_title="Cadastrar Aviso",_href=URL('cadastrar_aviso', args=[request.args(0)] ,user_signature=True)) 
	return dict(grid=grid, bt_incluir = bt_incluir)	

@auth.requires_login()
def cadastrar_aviso( ):
	rows = db(db.pets.id_usr == auth.user.id ).select()
	pets_sel_id=[]
	pets_sel_nome=[]
	for row in rows:
		pets_sel_id.append(row('pets.id'))
		pets_sel_nome.append(row('pets.nome'))
	

	form=SQLFORM.factory( Field('id_pet','list:string',requires=IS_IN_SET(pets_sel_id,pets_sel_nome),label='Pets'),
						  Field('nome_controle','string',label='Nome do Controle', requires=[IS_NOT_EMPTY()]),
						  Field('duracao','integer',label='Duração em Dias', default=1,onchange="myFunction",requires=[IS_NOT_EMPTY(),IS_INT_IN_RANGE(1,721,error_message='Valores válidos de 1 dias a 720 dias')]),
						  Field('dt_inicio_controle', 'date', label='Data de Início',
								requires=[IS_NOT_EMPTY(),
								IS_DATE(error_message='Data Inválida')],
								default=request.now),
						  Field('dt_fim_controle', 'date', label='Data de Término',
								requires=[IS_NOT_EMPTY(),
								IS_DATE(error_message='Data Inválida')],
								default=request.now + timedelta(days = 1)),
						 # Field('qtd_aviso','integer',label='Quantidade de Avisos',default=1,requires=[IS_NOT_EMPTY(),IS_INT_IN_RANGE(1,21,error_message='Valores válidos de 1 dias a 20 dias')]),
    					  Field('qtd_dias_primeiro_aviso','integer',label='Quantidade de Dias Para o Prímeiro Aviso',
    					  	default=1,requires=[IS_NOT_EMPTY(),IS_INT_IN_RANGE(1,21,error_message='Valores válidos de 1 dias a 20 dias')] ),
    					  Field('texto','text',label='Texto do Aviso'),
    					  )
	form.add_button(T("Back"),URL('listar_avisos'), _class='btn btn-danger')
	if form.process(onvalidation = valida_form_aviso).accepted:
		try:
			db.avisos.insert(nome_controle=form.vars.nome_controle, duracao=form.vars.duracao, id_pet=form.vars.id_pet, 
				dt_inicio_controle=form.vars.dt_inicio_controle,dt_fim_controle=form.vars.dt_fim_controle, qtd_aviso=form.vars.qtd_aviso,
				qtd_dias_primeiro_aviso=form.vars.qtd_dias_primeiro_aviso, texto= form.vars.texto )
			print("teste Insert")
			session.flash = 'Controle cadastrado'
		except Exception as e:
			session.flash = 'Erro cadastrando o Controle %s' %str(e)
			print("Erro %s" %str(e))
			return dict(form=form)
		redirect(URL(r=request,c='petcontrol', f='listar_avisos'))
		print("teste Insert 2") 
	elif form.errors:
		response.flash = 'Erros no formulário!'
	else:
		if not response.flash:
			response.flash = 'Preencha o formulário!'
	return dict(form=form)




def teste():
	envia_aviso()
	redirect(URL(r=request,c='default',f='index'))
	return dict()

