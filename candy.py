import abc


class Candy(abc.ABC):
    """
    An abstract base class representing Candy
    """
    def __init__(self, **kwargs):
        """
        Initializes Candy.
        :param: kwargs: a dictionary
        """
        self._contains_nuts = kwargs["contains_nuts"]
        self._is_lactose_free = kwargs["is_lactose_free"]
        self._name = kwargs["name"]
        self._description = kwargs["description"]
        self._product_id = kwargs["product_id"]

    @property
    def contains_nuts(self):
        """
        Getter for contains nuts.
        :return: "Y" (yes) or "N" (no) as a string
        """
        return self._contains_nuts

    @property
    def is_lactose_free(self):
        """
        Getter for lactose free.
        :return: "Y" (yes) or "N" (no) as a string
        """
        return self._is_lactose_free

    @property
    def name(self):
        """
        Getter for name.
        :return: name as a string
        """
        return self._name

    @property
    def description(self):
        """
        Getter for description.
        :return: description as a string
        """
        return self._description

    @property
    def product_id(self):
        """
        Getter for product id
        :return: product id as an int
        """
        return self._product_id


class PumpkinCaramelToffee(Candy):
    """
    Represents a pumpkin caramel toffee Halloween candy.
    """
    def __init__(self, **kwargs):
        """
        Initializes PumpkinCaramelToffee.
        :param: kwargs: a dictionary
        """
        super().__init__(**kwargs)
        self._variety = kwargs["variety"]

    @property
    def variety(self):
        """
        Getter for variety.
        :return: variety as a string
        """
        return self._variety

    def __str__(self):
        """A string representation of PumpkinCaramelToffee
        """
        return f"Name: {self.name}\n" \
               f"Description: {self.description}\n" \
               f"Product id: {self.product_id}\n" \
               f"Contains nuts: {self.contains_nuts}\n" \
               f"Lactose free: {self.is_lactose_free}\n" \
               f"Variety: {self.variety}"


class CandyCane(Candy):
    """
    Represents a CandyCane Candy.
    """
    def __init__(self, **kwargs):
        """
        Initializes CandyCane
        :param kwargs: a dictionary
        """
        super().__init__(**kwargs)
        self._colour = kwargs["colour"]

    @property
    def colour(self):
        """
        Gets colour
        :return: colour as a string
        """
        return self._colour

    def __str__(self):
        """
        :return: a string representation of a CandyCane
        """
        return f"Name: {self.name}\n" \
               f"Description: {self.description}\n" \
               f"Product id: {self.product_id}\n" \
               f"Contains nuts: {self.contains_nuts}\n" \
               f"Lactose free: {self.is_lactose_free}\n" \
               f"Colour: {self.colour}"


class CremeEgg(Candy):
    """
    Represents a CremeEgg Candy.
    """
    def __init__(self, **kwargs):
        """
        Initializes CremeEgg
        :param kwargs: a dictionary
        """
        super().__init__(**kwargs)
        self._pack_size = kwargs["pack_size"]

    @property
    def pack_size(self):
        """
        Gets pack size.
        :return: pack size as an int
        """
        return self._pack_size

    def __str__(self):
        """
        :return: a string representation of a CremeEgg
        """
        return f"Name: {self.name}\n" \
               f"Description: {self.description}\n" \
               f"Product id: {self.product_id}\n" \
               f"Contains nuts: {self.contains_nuts}\n" \
               f"Lactose free: {self.is_lactose_free}\n" \
               f"Pack size: {self.pack_size}"
