# 1.1
from dataclasses import dataclass
from enum import Enum, unique

@unique
class Color(Enum):
    green = 0
    black = 1
    na = 9

@unique
class Root(Enum):
    curled = 0
    twisted = 1
    na = 9

@unique
class Voice(Enum):
    muffled = 0
    murky = 1
    na = 9

@dataclass
class WatermelonStatus:
    color: Color
    root: Root
    voice: Voice

@dataclass
class Watermelon:
    status: WatermelonStatus
    is_good: bool

def solution():
    good_watermelon1 = Watermelon(WatermelonStatus(
        Color.green, Root.curled, Voice.murky), True)
    bad_watermelon1 = Watermelon(WatermelonStatus(
        Color.black, Root.twisted, Voice.muffled), False)
    count = 0
    result = []
    for color in Color:
        if color == bad_watermelon1.status.color:
            continue
        for root in Root:
            if root == bad_watermelon1.status.root:
                continue
            for voice in Voice:
                if voice == bad_watermelon1.status.voice:
                    continue
                if (color != good_watermelon1.status.color and 
                    root != good_watermelon1.status.root and 
                    voice != good_watermelon1.status.voice):
                    continue
                count += 1
                tmp = (color.name, root.name, voice.name)
                result.append(tmp)
    print(count)
    for item in result:
        print(item)

if __name__ == "__main__":
    solution()
