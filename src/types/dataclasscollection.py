from typing import TypeVar

T = TypeVar("T")

# class DataclassCollection[T]:
#     def __init__(self, indexProperty:str, dataclasses:list[dataclass] *args):
#         self.collection = dataclasses
#         self.indexProperty = indexProperty
#         for arg in args:
#             self.collection.append(dataclass(*arg))
