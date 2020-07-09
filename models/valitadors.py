## Validadores de Pet
db.pets.nome.requires = [IS_NOT_EMPTY(),
IS_NOT_IN_DB(db, 'pets.nome' ,error_message='Nome Já cadastrado!'),]
db.pets.raca.requires = IS_UPPER()
db.pets.tipo.requires = IS_UPPER()
db.avisos.nome_controle.requires = IS_UPPER()

#db.pesos.dt_medicao = IS_NOT_EMPTY()
#db.pesos.peso = IS_NOT_EMPTY()
db.pets.img.requires = [IS_NOT_EMPTY()] 
##Pet.generos.requires = IS_NOT_EMPTY()
##Filmes.diretor.requires = IS_NOT_EMPTY()
##Filmes.capa.requires = IS_EMPTY_OR(IS_IMAGE())

