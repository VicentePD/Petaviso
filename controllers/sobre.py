

def contato():
	form = SQLFORM(db.topicos)
	form.add_button(T('Back'), URL(c='petcontrol',f='menu'), _class='btn btn-danger')
	form.vars.id_usr = auth.user.id
	if form.process().accepted:
		session.flash = 'Comentário Enviado'
		redirect(URL(c='petcontrol',f='menu'))
	elif form.errors:
		response.flash('Erros no formulário !')
	else:
		if not response.flash:
			response.flash = 'Prencha o formulário'
	return dict(form=form)