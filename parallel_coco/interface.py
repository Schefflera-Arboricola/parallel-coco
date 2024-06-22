import coco
from parallel_coco.algorithms.processing import temper, melt

__all__ = ["ParallelChocolate", "BackendInterface"]


class ParallelChocolate:
    __coco_backend__ = "parallel"

    def __init__(self, chocolate_obj=None):
        if chocolate_obj is None:
            self.chocolate_obj = coco.Chocolate()
        elif isinstance(chocolate_obj, coco.Chocolate):
            self.chocolate_obj = chocolate_obj
        else:
            self.chocolate_obj = coco.Chocolate(chocolate_obj)

    def __getattr__(self, attr):
        return getattr(self.chocolate_obj, attr)


class BackendInterface:
    temper = temper
    melt = melt

    @staticmethod
    def convert_from_coco(chocolate, *args, **kwargs):
        if isinstance(chocolate, ParallelChocolate):
            return chocolate
        return ParallelChocolate(chocolate)

    @staticmethod
    def convert_to_coco(result):
        if isinstance(result, ParallelChocolate):
            return result.chocolate_obj
        return result
