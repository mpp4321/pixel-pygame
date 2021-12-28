import esper
from types import Int, Tuple, String
from dataclasses import dataclass as component

# Structs

@component
class Sprite:
    def __init__(self, id: String, base_color: Tuple[Int, Int, Int]):
        self.id = id
        self.base_color = base_color

@component
class Position:
    def __init__(self, x: Int, y: Int):
        self.x = x
        self.y = y

@component
class Movement:
    def __init__(self, delta: Tuple[Int, Int], speed: Int):
        self.delta = delta
        self.speed = speed
    
    def update(self, position):
        position.x += self.delta[0]
        position.y += self.delta[1]
        self.delta = (0, 0)

# Functions

class WorldInstance:

    def __init__(self):
        self.world = esper.World()
    
    def c_player(self, p: Position):
        self.world.create_component(p, Movement((0, 0), 1))
