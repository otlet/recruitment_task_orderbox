from pprint import pprint
from typing import Dict


class OrderSizeException(Exception):
    def __init__(self, message):
        self.message = message


class GeneratorOrderBox:
    """
    A class used to generate number of box need to handle a order

    Attributes
    ----------
    quantity : int
        Number of ordered products
    order_boxes : Dict[str, int]
        number of boxes need to send order

    Methods
    -------
    __check_quanity__(quantity: int = None)
        Checking that the quantity of products is allowed to be packed
    __get_box_multiply__() -> int
        Returns information with the number of collective cartons
    get_box_quantity(self, quantity: int) -> Dict[str, int]
        The method returns the number of boxes needed for packing based on the quantity of products ordered.
    """

    quantity: int = None
    order_boxes: Dict[str, int] = {
        'large_box': 0,
        'average_box': 0,
        'small_box': 0,
        'multiply': 0
    }

    def __init__(self):
        pass

    def __check_quanity__(self, quantity: int):
        self.order_boxes = {
            'large_box': 0,
            'average_box': 0,
            'small_box': 0
        }
        if quantity < 0 or quantity > 100:
            raise OrderSizeException("Quantity not allowed!")
        self.quantity = quantity

    def __get_box_multiply__(self) -> int:
        box_quantity = sum(self.order_boxes.values())
        if box_quantity < 2:
            return 0
        return int(box_quantity / 4) + 1

    def get_box_quantity(self, quantity: int) -> Dict[str, int]:
        self.__check_quanity__(quantity)
        check = True
        first_run = True
        while check:
            if 9 < self.quantity <= 15 and first_run is True:
                if self.quantity <= 12:
                    self.order_boxes['average_box'] = 2
                else:
                    self.order_boxes['large_box'] = 2
                check = False
            elif 0 < self.quantity <= 3:
                self.order_boxes['small_box'] += 1
                self.quantity -= 3
            elif 3 < self.quantity <= 6:
                self.order_boxes['average_box'] += 1
                self.quantity -= 6
            elif 6 < self.quantity:
                self.order_boxes['large_box'] += 1
                self.quantity -= 9
            else:
                check = False
            first_run = False
        self.order_boxes['multiply'] = self.__get_box_multiply__()
        return self.order_boxes
