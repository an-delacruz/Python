class Persona:
    def __init__(self,id_persona:None, nombre:None, apellido:None, email:None, edad:None):
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad

    def __str__(self):
        return f'Persona: {self.idpersona}, {self.nombre}, {self.apellido}, {self.email}, {self.edad}'

    @property
    def idPersona(self):
        return self.id_persona
    @idPersona.setter
    def idPersona(self,idPersona):
        self.id_persona = idPersona

    @property
    def nombre(self):
        return self.nombre
    @nombre.setter
    def nombre(self,nombre):
        self.nombre = nombre
        
    @property
    def apellido(self):
        return self.apellido
    @apellido.setter
    def apellido(self,apellido):
        self.apellido = apellido
    @property
    def email(self):
        return self.email
    @email.setter
    def email(self,email):
        self.email = email
    @property
    def edad(self):
        return self.edad
    @edad.setter
    def edad(self,edad):
        self.edad = edad