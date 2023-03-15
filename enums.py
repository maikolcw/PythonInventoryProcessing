import enum


class Colour(enum.Enum):
    """
    Colors
    """
    ORANGE = "Orange"
    BLUE = "Blue"
    PINK = "Pink"
    WHITE = "White"
    GREY = "Grey"
    RED = "Red"
    GREEN = "Green"


class Spider(enum.Enum):
    """
    Spider toy type
    """
    TARANTULA = "Tarantula"
    WOLFSPIDER = "Wolf Spider"


class Stuffing(enum.Enum):
    """
    Stuffing type for toys
    """
    POLYESTER_FIBREFILL = "Polyester Fibrefill"
    WOOL = "Wool"


class Size(enum.Enum):
    """
    Permissible sizes
    """
    S = "S"
    M = "M"
    L = "L"


class Fabric(enum.Enum):
    """
    Fabric types
    """
    LINEN = "Linen"
    COTTON = "Cotton"
    ACRYLIC = "Acrylic"


class Nut(enum.Enum):
    """
    Variety for nut
    """
    SEA_SALT = "Sea Salt"
    REGULAR = "Regular"
