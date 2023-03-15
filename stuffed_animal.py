import abc


class StuffedAnimal(abc.ABC):
    """
    Represents a Stuffed Animal.
    """
    def __init__(self, stuffing=None, size=None, fabric=None, **kwargs):
        """
        Initializes StuffedAnimal
        :param stuffing: a string
        :param size: a string
        :param fabric: a string
        :param kwargs: a dictionary
        """
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric
        self._name = kwargs["name"]
        self._description = kwargs["description"]
        self._product_id = kwargs["product_id"]

    @property
    def stuffing(self):
        """
        Get stuffing
        :return: stuffing as a string
        """
        return self._stuffing

    @property
    def size(self):
        """
        Get size
        :return: size as a string
        """
        return self._size

    @property
    def fabric(self):
        """
        Get fabric
        :return: fabric as a string
        """
        return self._fabric

    @property
    def name(self):
        """
        Get name
        :return: name as a string
        """
        return self._name

    @property
    def description(self):
        """
        Get description
        :return: description as a string
        """
        return self._description

    @property
    def product_id(self):
        """
        Get product id
        :return: product id as a string
        """
        return self._product_id


class DancingSkeleton(StuffedAnimal):
    """
    Represents a dancing skeleton stuffed animal.
    """
    def __init__(self, **kwargs):
        """
        Initializes DancingSkeleton
        :param kwargs: a dictionary
        """
        super().__init__(**kwargs)
        self._is_glow = kwargs["is_glow"]

    @property
    def is_glow(self):
        """
        :return: a string
        """
        return self._is_glow

    def __str__(self):
        """
        :return: a string representation of a dancing skeleton stuffed animal
        """
        return f"Name: {self.name}\n" \
               f"Description: {self.description}\n" \
               f"Product id: {self.product_id}\n" \
               f"Stuffing: {self.stuffing}\n" \
               f"Size: {self.size}\n" \
               f"Fabric: {self.fabric}\n" \
               f"Has glow: {self.is_glow}"


class Reindeer(StuffedAnimal):
    """
    Represents a reindeer stuffed animal.
    """
    def __init__(self, **kwargs):
        """
        Initializes a Reindeer
        :param kwargs: a dictionary
        """
        super().__init__(**kwargs)
        self._is_glow = kwargs["is_glow"]

    @property
    def is_glow(self):
        """
        :return: a string
        """
        return self._is_glow

    def __str__(self):
        """
        :return: a string representation of a reindeer stuffed animal
        """
        return f"Name: {self.name}\n" \
               f"Description: {self.description}\n" \
               f"Product id: {self.product_id}\n" \
               f"Stuffing: {self.stuffing}\n" \
               f"Size: {self.size}\n" \
               f"Fabric: {self.fabric}\n" \
               f"Has glow: {self.is_glow}"


class EasterBunny(StuffedAnimal):
    """
    Represents an Easter bunny stuffed animal.
    """
    def __init__(self, **kwargs):
        """
        Initializes EasterBunny
        :param kwargs: a dictionary
        """
        super().__init__(**kwargs)
        self._colour = kwargs["colour"]

    @property
    def colour(self):
        """
        Get colour
        :return: colour as a string
        """
        return self._colour

    def __str__(self):
        """
        :return: a string representation of an Easter bunny stuffed animal
        """
        return f"Name: {self.name}\n" \
               f"Description: {self.description}\n" \
               f"Product id: {self.product_id}\n" \
               f"Stuffing: {self.stuffing}\n" \
               f"Size: {self.size}\n" \
               f"Fabric: {self.fabric}\n" \
               f"Colour: {self.colour}"
