from dataclasses import dataclass


@dataclass
class test:
    prop1: str
    prop2: int


test1 = test("test1", 3)

print(test1)
