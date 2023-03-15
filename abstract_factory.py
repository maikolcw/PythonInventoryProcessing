import abc

from candy import Candy, CandyCane, PumpkinCaramelToffee, CremeEgg
from enums import Spider, Colour, Fabric, Stuffing, Nut
from exception import InvalidDataError
from stuffed_animal import StuffedAnimal, Reindeer, DancingSkeleton, EasterBunny
from toy import Toy, SantasWorkshop, RCSpider, RobotBunny


class ItemFactory(abc.ABC):
    """
    Abstract factory class that represents an Item factory.
    """
    @abc.abstractmethod
    def create_toy(self, **kwargs):
        """
        Create toy item.
        :param: kwargs: a dictionary
        :return: an item of type Toy
        """
        return Toy(**kwargs)

    @abc.abstractmethod
    def create_stuffed_animal(self, **kwargs):
        """
        Create a stuffed animal.
        :param: kwargs: a dictionary
        :return: an item of type StuffedAnimal
        """
        return StuffedAnimal(**kwargs)

    @abc.abstractmethod
    def create_candy(self, **kwargs):
        """
        Create a Candy item.
        :param: kwargs:
        :return:
        """
        return Candy(**kwargs)


class ChristmasItemFactory(ItemFactory):
    """
    Item Factory class for Christmas items.
    """
    def create_toy(self, **kwargs):
        """
        Create a toy from Santa's workshop
        :param kwargs: a dictionary
        :return: a toy of type SantasWorkshop
        """
        try:
            if kwargs["is_battery"] != "N":
                raise InvalidDataError(f"Battery operation is not {kwargs['is_battery']}")
            else:
                return SantasWorkshop(**kwargs)
        except InvalidDataError as e:
            return f"{e} {e.message}"

    def create_stuffed_animal(self, **kwargs):
        """
        Create a Reindeer stuffed animal.
        :param: kwargs: a dictionary
        :return: a Reindeer StuffedAnimal
        """
        try:
            if kwargs["fabric"] != Fabric.COTTON.value:
                raise InvalidDataError(f"Fabric can only be {Fabric.COTTON.value}")
            elif kwargs["stuffing"] != Stuffing.WOOL.value:
                raise InvalidDataError(f"Stuffing can only be {Stuffing.WOOL.value}")
            elif kwargs["is_glow"] != "Y":
                raise InvalidDataError(f"This item only has glow in the dark nose.")
            else:
                return Reindeer(**kwargs)
        except InvalidDataError as e:
            return f"{e} {e.message}"

    def create_candy(self, **kwargs):
        """
        Create a CandyCane item.
        :param: kwargs: a dictionary
        :return: an item of type CandyCane
        """
        permissible_color_list = [Colour.RED.value, Colour.GREEN.value]
        try:
            if kwargs["is_lactose_free"] != "Y":
                raise InvalidDataError(f"This item is lactose free.")
            elif kwargs["contains_nuts"] != "N":
                raise InvalidDataError(f"This item does not contain nuts.")
            elif kwargs["colour"] not in permissible_color_list:
                raise InvalidDataError(f"This item stripe color can only be {permissible_color_list}")
            else:
                return CandyCane(**kwargs)
        except InvalidDataError as e:
            return f"{e} {e.message}"


class HalloweenItemFactory(ItemFactory):
    """
    Item Factory class for halloween items.
    """

    def create_toy(self, **kwargs):
        """
        Create a RCSpider item.
        :param: kwargs: a dictionary
        :return: a RCSpider toy
        """
        permissible_spider_type_list = [e.value for e in Spider]
        try:
            if kwargs["is_battery"] != "Y":
                raise InvalidDataError(f"Battery operation is not {kwargs['is_battery']}")
            elif kwargs["type_of_spider"] not in permissible_spider_type_list:
                raise InvalidDataError(f"Spider type can only be {permissible_spider_type_list}")
            else:
                return RCSpider(**kwargs)
        except InvalidDataError as e:
            return f"{e} {e.message}"

    def create_stuffed_animal(self, **kwargs):
        """
        Create a DancingSkeleton stuffed animal.
        :param: kwargs: a dictionary
        :return: a DancingSkeleton StuffedAnimal
        """
        try:
            if kwargs["fabric"] != Fabric.ACRYLIC.value:
                raise InvalidDataError(f"Fabric can only be {Fabric.ACRYLIC.value}")
            elif kwargs["stuffing"] != Stuffing.POLYESTER_FIBREFILL.value:
                raise InvalidDataError(f"Stuffing can only be {Stuffing.POLYESTER_FIBREFILL.value}")
            else:
                return DancingSkeleton(**kwargs)
        except InvalidDataError as e:
            return f"{e} {e.message}"

    def create_candy(self, **kwargs):
        """
        Create a halloween candy item.
        :param: kwargs: a dictionary
        :return: a PumpkinCaramelToffee Candy
        """
        permissible_variety_list = [e.value for e in Nut]
        try:
            if kwargs["is_lactose_free"] != "N":
                raise InvalidDataError(f"This item is not lactose free.")
            elif kwargs["contains_nuts"] != "Y":
                raise InvalidDataError(f"This item may contain traces of nuts.")
            elif kwargs["variety"] not in permissible_variety_list:
                raise InvalidDataError(f"This item variety can only be {permissible_variety_list}")
            else:
                return PumpkinCaramelToffee(**kwargs)
        except InvalidDataError as e:
            return f"{e} {e.message}"


class EasterItemFactory(ItemFactory):
    """
    Item factory class for Easter items.
    """
    def create_toy(self, **kwargs):
        """
        Create an Easter toy.
        :param: kwargs: a dictionary
        :return: a RobotBunny toy
        """
        permissible_colour_list = [Colour.ORANGE.value, Colour.BLUE.value, Colour.PINK.value]
        try:
            if kwargs["is_battery"] != "Y":
                raise InvalidDataError(f"Battery operation is not {kwargs['is_battery']}")
            elif kwargs["colour"] not in permissible_colour_list:
                raise InvalidDataError(f"Colour can only be {permissible_colour_list}")
            else:
                return RobotBunny(**kwargs)
        except InvalidDataError as e:
            return f"{e} {e.message}"

    def create_stuffed_animal(self, **kwargs):
        """
        Create an Easter stuffed animal
        :param kwargs: a dictionary
        :return: An EasterBunny StuffedAnimal
        """
        permissible_colour_list = [Colour.WHITE.value, Colour.GREY.value, Colour.PINK.value, Colour.BLUE.value]
        try:
            if kwargs["fabric"] != Fabric.LINEN.value:
                raise InvalidDataError(f"Fabric can only be {Fabric.LINEN.value}")
            elif kwargs["stuffing"] != Stuffing.POLYESTER_FIBREFILL.value:
                raise InvalidDataError(f"Stuffing can only be {Stuffing.POLYESTER_FIBREFILL.value}")
            elif kwargs["colour"] not in permissible_colour_list:
                raise InvalidDataError(f"Colour can only be {permissible_colour_list}")
            else:
                return EasterBunny(**kwargs)
        except InvalidDataError as e:
            return f"{e} {e.message}"

    def create_candy(self, **kwargs):
        """
        Create an Easter candy.
        :param: kwargs: a dictionary
        :return: a CremeEgg Candy
        """
        try:
            if kwargs["is_lactose_free"] != "N":
                raise InvalidDataError(f"This item is not lactose free.")
            elif kwargs["contains_nuts"] != "Y":
                raise InvalidDataError(f"This item may contain traces of nuts.")
            else:
                return CremeEgg(**kwargs)
        except InvalidDataError as e:
            return f"{e} {e.message}"
