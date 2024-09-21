# core/entities/animal.py

class Animal:
    """
    Representa un animal en la finca.
    
    Attributes:
        id (int): Identificador único del animal.
        especie (str): Especie del animal (e.j., 'Bovino').
        raza (str): Raza del animal.
        fecha_nacimiento (date): Fecha de nacimiento del animal.
        peso (float): Peso actual del animal en kg.
        estado_salud (str): Estado de salud actual del animal.
    """
    
    def __init__(self, id, especie, raza, fecha_nacimiento, peso, estado_salud):
        self.id = id
        self.especie = especie
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.estado_salud = estado_salud

# core/use_cases/registrar_produccion.py

from datetime import datetime

class RegistrarProduccion:
    """
    Caso de uso para registrar la producción de leche de un animal.
    """
    
    def __init__(self, animal_repository, produccion_repository):
        self.animal_repository = animal_repository
        self.produccion_repository = produccion_repository
    
    def execute(self, animal_id, cantidad, fecha=None):
        """
        Ejecuta el caso de uso.
        
        Args:
            animal_id (int): ID del animal.
            cantidad (float): Cantidad de leche producida en litros.
            fecha (datetime, optional): Fecha de la producción. Si no se proporciona, se usa la fecha actual.
        
        Returns:
            bool: True si el registro fue exitoso, False en caso contrario.
        """
        animal = self.animal_repository.get_by_id(animal_id)
        if not animal:
            return False
        
        if fecha is None:
            fecha = datetime.now()
        
        produccion = Produccion(animal_id=animal_id, cantidad=cantidad, fecha=fecha)
        return self.produccion_repository.add(produccion)

# infrastructure/repositories/animal_repository.py

from core.entities.animal import Animal

class AnimalRepository:
    """
    Repositorio para la entidad Animal.
    """
    
    def __init__(