class Persona:
  def __init__(self, nombre, edad, genero):
    self.nombre = nombre
    self.edad = edad
    self.genero = genero

  def saludar(self):
    return ('Bienvenido, soy ' + self.nombre)

persona = Persona("rick", 25, "macho")
print (persona.saludar(), "ahora tengo ", persona.edad, "años y soy un", persona.genero, "macho")

class Empleado(Persona):
  def __init__(self, nombre, edad, genero, salario, puesto):
    super().__init__(nombre, edad, genero)
    self.salario = salario
    self.puesto = puesto

  def trabajar(self):
    return "esta trabajando"
empleado = Empleado("rick", 25, "macho", 1300, 1)
print(persona.nombre, "tiene un salario de:", empleado.salario, "y esta en el puesto #",empleado.puesto, "y en este momento",persona.nombre, empleado.trabajar())

class Estudiante(Persona):
  def __init__(self, nombre, edad, genero, grado, escuela):
    super().__init__(nombre, edad, genero)
    self.grado = grado
    self.escuela = escuela

  def estudiar(self):
    return "esta estudiando"

estudiante = Estudiante("rick", 25, "macho", 11, "gar")
print(persona.nombre, "esta en el grado:", estudiante.grado, "en el colegio",
      estudiante.escuela, "y en este momento",persona.nombre, estudiante.estudiar())

#clase rectangulo
class Rectangulo:
  def __init__(self, longitud, ancho):
    self.longitud = longitud
    self.ancho = ancho

  def area(self):
    area = self.longitud * self.ancho
    return area

  def perimetro(self):
    perimetro = 2*(self.longitud + self.ancho)
    return perimetro

rectangulo = Rectangulo(5, 2)
area_rectangulo = rectangulo.area()
perimetro_rectangulo = rectangulo.perimetro()
print("el area del rectangulo es: ", area_rectangulo, "y el perimetro es: ", perimetro_rectangulo)