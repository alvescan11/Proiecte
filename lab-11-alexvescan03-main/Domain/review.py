from dataclasses import dataclass

from Domain.entity import Entity

@dataclass
class Review(Entity):
    numeClient: str
    id_restaurant: str
    comentariu: str
    nota: int
