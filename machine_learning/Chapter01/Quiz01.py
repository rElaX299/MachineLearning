# 1.1
from typing import Tuple, List
from dataclasses import dataclass
from enum import Enum, unique

@unique
class Color(Enum):
    GREEN = 0x0
    BLACK = 0x1
    NA = 0xff

@unique
class Root(Enum):
    CURLED = 0x0
    TWISTED = 0x1
    NA = 0xff

@unique
class Voice(Enum):
    MUFFLED = 0x0
    MURKY = 0x1
    NA = 0xff

@dataclass
class WatermelonStatus:
    color: Color
    root: Root
    voice: Voice

@dataclass
class Watermelon:
    status: WatermelonStatus
    is_good: bool

# 题目条件
good_watermelon1 = Watermelon(WatermelonStatus(
    Color.GREEN, Root.CURLED, Voice.MURKY), True)
bad_watermelon1 = Watermelon(WatermelonStatus(
    Color.BLACK, Root.TWISTED, Voice.MUFFLED), False)

# 解决方案
def solution() -> Tuple[int, List]:
    version_space_size = 0
    version_space = []

    def match_good_watermelon(color, root, voice):
        is_match = color == good_watermelon1.status.color or \
                   root == good_watermelon1.status.root or \
                   voice == good_watermelon1.status.voice
        return is_match

    positive_colors = [c for c in Color if c != bad_watermelon1.status.color]
    positive_roots = [r for r in Root if r != bad_watermelon1.status.root]
    positive_voices = [v for v in Voice if v != bad_watermelon1.status.voice]

    for c in positive_colors:
        for r in positive_roots:
            for v in positive_voices:
                if not match_good_watermelon(c, r, v):
                    continue
                version_space_size += 1
                hypothesis = (c.name, r.name, v.name)
                version_space.append(hypothesis)

    return version_space_size, version_space


if __name__ == "__main__":
    size, space = solution()

    print(size)
    for item in space:
        print(item)
