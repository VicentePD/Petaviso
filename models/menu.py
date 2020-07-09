# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('petcontrol', 'menu'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
       ## (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('Pet'), False, '#', [
            (T('Cadastrar Pet'), False, URL(c='petcontrol', f='novo_pet')),
            (T('Listar Pesos'), False, URL(c='petcontrol', f='lista_peso')),
            (T('Listar Alertas'), False, URL(c='petcontrol', f='listar_avisos')),
        ]),
        (T('Peso'), False, '#', [
            (T('Listar Pesos'), False, URL(c='petcontrol', f='lista_peso')),
            (T('Cadastrar Peso'), False, URL(c='petcontrol', f='cadastrar_peso')),
        ]),
        ('Alertas', False, '#', [
            ( (T('Listar Alertas'), False, URL(c='petcontrol', f='listar_avisos'))),
            ( (T('Cadastrar Alertas'), False, URL(c='petcontrol', f='cadastrar_aviso')))
        ])
       
    ]
if configuration.get('app.informacao'):
    response.menu_inf = [
         ('Informações', False, '#', [
                ( (T('Contato'), False, URL('contato'))),
                ( (T('Sobre'), False, URL('cadastrar_aviso')))
            ])
    ]