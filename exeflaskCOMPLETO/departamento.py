class Departamento:
    def __init__(self,nome):

        self._nome = nome


    def _get_nome(self):
        return self._nome
    
    def _get_funcionario(self):
        return self._funcionario
    
    def _get_id(self):
        return self._id
    
    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_id(self, id):
        self._id = id
    
    def _set_funcionario(self, funcionario):
        self._funcionario = funcionario
    

    nome = property(_get_nome,_set_nome)
    funcionario = property(_get_funcionario,_set_funcionario)
    id = property(_get_id,_set_id)



class Projeto:
    
    def __init__(self,nome,dataPrevista):
        self._nome = nome
        self._dataPrevista = format(datetime.strptime(str(dataPrevista),"%d/%m/%Y"),"%d/%m/%Y")
    
    def _get_nome(self):
        return self._nome
    
    def _get_dataPrevista(self):
        return self._dataPrevista
    
    def _get_id(self):
        return self._id

    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_id(self, id):
        self._id = id
    
    def _set_dataPrevista(self, dataPrevista):
        self._dataPrevista = format(datetime.strptime(str(dataPrevista),"%d/%m/%Y"),"%d/%m/%Y")
    

    nome = property(_get_nome,_set_nome)
    dataPrevista = property(_get_dataPrevista,_set_dataPrevista)
    id = property(_get_id,_set_id)