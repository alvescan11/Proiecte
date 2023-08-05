from dataclasses import dataclass

from Domain.entity import Entity

@dataclass
class Restaurant(Entity):
    nume: str
    adresa: str
    vegetarian: bool