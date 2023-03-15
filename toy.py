import abc


class Toy(abc.ABC):
    """
    Represents a Toy.
    """
    def __init__(self, is_battery=None, min_age=None, **kwargs):
        """
        Initializes Toy.
        :param: is_battery: a string
        :param min_age: an int
        :param kwargs: a dictionary
        """
        self._is_battery = is_battery
        self._min_age = min_age
        self._name = kwargs["name"]
        self._description = kwargs["description"]
        self._product_id = kwargs["product_id"]

    @property
    def is_battery(self):
        """
        :return: a string
        """
        return self._is_battery

    @property
    def min_age(self):
        """
        Get age
        :return: age as an int
        """
        return self._min_age

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


class SantasWorkshop(Toy):
    """
    Represents Santa's workshop
    """
    def __init__(self, **kwargs):
        """
        Initializes SantasWorkshop
        :param kwargs: a dictionary
        """
        super().__init__(**kwargs)
        self._dimensions = kwargs["dimensions"]
        self._number_of_rooms = kwargs["number_of_rooms"]

    @property
    def dimensions(self):
        """
        Get dimensions
        :return: a string
        """
        return self._dimensions

    @property
    def number_of_rooms(self):
        """
        Get number of rooms
        :return: an int
        """
        return self._number_of_rooms

    def __str__(self):
        """
        :return: a string representation of SantasWorkshop
        """
        return f"Name: {self.name}\n" \
               f"Minimum age required: {self.min_age}\n" \
               f"Description: {self.description}\n" \
               f"Battery operated: {self.is_battery}\n" \
               f"Product id: {self.product_id}\n" \
               f"Dimensions: {self.dimensions}\n" \
               f"Number of rooms: {self.number_of_rooms}"


class RCSpider(Toy):
    """
    Represents a remote-controlled spider toy.
    """
    def __init__(self, **kwargs):
        """
        Initializes RCSpider
        :param kwargs: a dictionary
        """
        super().__init__(**kwargs)
        self._speed = kwargs["speed"]
        self._jump_height = kwargs["jump_height"]
        self._is_glow = kwargs["is_glow"]
        self._type_of_spider = kwargs["type_of_spider"]

    @property
    def speed(self):
        """
        Get speed
        :return: an int
        """
        return self._speed

    @property
    def jump_height(self):
        """
        Get jump height
        :return: an int
        """
        return self._jump_height

    @property
    def is_glow(self):
        """
        :return: a string
        """
        return self._is_glow

    @property
    def type_of_spider(self):
        """
        Get type of spider
        :return: a string
        """
        return self._type_of_spider

    def __str__(self):
        """
        :return: a string representation of RCSpider
        """
        return f"Name: {self.name}\n" \
               f"Minimum age required: {self.min_age}\n" \
               f"Description: {self.description}\n" \
               f"Battery operated: {self.is_battery}\n" \
               f"Product id: {self.product_id}\n" \
               f"Speed: {self.speed}\n" \
               f"Jump Height: {self.jump_height}\n" \
               f"Has glow: {self.is_glow}\n" \
               f"Type of Spider: {self.type_of_spider}"


class RobotBunny(Toy):
    """
    Represents a robot bunny toy.
    """
    def __init__(self, **kwargs):
        """
        Initializes RobotBunny
        :param kwargs: a dictionary
        """
        super().__init__(**kwargs)
        self._number_of_sound_effects = kwargs["number_of_sound_effects"]
        self._colour = kwargs["colour"]

    @property
    def number_of_sound_effects(self):
        """
        Get number of sound effects
        :return: an int
        """
        return self._number_of_sound_effects

    @property
    def colour(self):
        """
        Get colour
        :return: a string
        """
        return self._colour

    def __str__(self):
        """
        :return: a string representation of RobotBunny
        """
        return f"Name: {self.name}\n" \
               f"Minimum age required: {self.min_age}\n" \
               f"Description: {self.description}\n" \
               f"Battery operated: {self.is_battery}\n" \
               f"Product id: {self.product_id}\n" \
               f"Number of sound effects: {self.number_of_sound_effects}\n" \
               f"Colour: {self.colour}"
