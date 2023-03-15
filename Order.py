class Order:
    """
    This class represents an order.
    """
    def __init__(self, order_number, product_id, item, name, product_detail_dictionary, factory):
        """
        Initializes Order object.
        :param: order_number: an int
        :param product_id: a string
        :param item: a string
        :param name: a string
        :param product_detail_dictionary: a dictionary
        :param factory: a factory
        """
        self._order_number = order_number
        self._product_id = product_id
        self._item = item
        self._name = name
        self._product_detail_dictionary = product_detail_dictionary
        self._factory = factory

    @property
    def name(self):
        """
        Gets name
        :return: name as a string
        """
        return self._name

    @property
    def order_number(self):
        """
        Gets order number
        :return: order number as an int
        """
        return self._order_number

    @property
    def product_id(self):
        """
        Gets product id
        :return: product id as a string
        """
        return self._product_id

    @property
    def item(self):
        """
        Gets item
        :return: item as a string
        """
        return self._item

    @property
    def product_detail_dictionary(self):
        """
        Gets product detail dictionary
        :return: product detail dictionary as a dictionary
        """
        return self._product_detail_dictionary

    @property
    def factory(self):
        """
        Gets factory
        :return: factory as an ItemFactory
        """
        return self._factory
