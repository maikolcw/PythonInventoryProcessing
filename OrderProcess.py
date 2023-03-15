import pandas

from Order import Order
from abstract_factory import ChristmasItemFactory, HalloweenItemFactory, EasterItemFactory


class OrderProcess:
    """This class process orders and returns a list of orders."""

    @staticmethod
    def read_excel_and_make_list_of_orders(path):
        """
        Reads Excel file and returns a list of orders
        :param path: a string
        :return: orders as a list
        """
        pd = pandas
        dataframe = pd.read_excel(path)
        list_of_orders = []
        for row in list(range(len(dataframe.index))):
            if dataframe.iloc[row]["holiday"] == "Christmas":
                factory = ChristmasItemFactory()
            elif dataframe.iloc[row]["holiday"] == "Halloween":
                factory = HalloweenItemFactory()
            else:
                factory = EasterItemFactory()
            product_detail_dictionary = {"quantity": dataframe.iloc[row]["quantity"],
                                         "description": dataframe.iloc[row]["description"],
                                         "is_battery": dataframe.iloc[row]["has_batteries"],
                                         "min_age": dataframe.iloc[row]["min_age"],
                                         "dimensions": dataframe.iloc[row]["dimensions"],
                                         "number_of_rooms": dataframe.iloc[row]["num_rooms"],
                                         "speed": dataframe.iloc[row]["speed"],
                                         "jump_height": dataframe.iloc[row]["jump_height"],
                                         "is_glow": dataframe.iloc[row]["has_glow"],
                                         "type_of_spider": dataframe.iloc[row]["spider_type"],
                                         "number_of_sound_effects": dataframe.iloc[row]["num_sound"],
                                         "colour": dataframe.iloc[row]["colour"],
                                         "is_lactose_free": dataframe.iloc[row]["has_lactose"],
                                         "contains_nuts": dataframe.iloc[row]["has_nuts"],
                                         "variety": dataframe.iloc[row]["variety"],
                                         "pack_size": dataframe.iloc[row]["pack_size"],
                                         "stuffing": dataframe.iloc[row]["stuffing"],
                                         "size": dataframe.iloc[row]["size"], "fabric": dataframe.iloc[row]["fabric"]}
            order = Order(dataframe.iloc[row]["order_number"], dataframe.iloc[row]["product_id"],
                          dataframe.iloc[row]["item"], dataframe.iloc[row]["name"],
                          product_detail_dictionary, factory)
            list_of_orders.append(order)
        for order in list_of_orders:
            yield order
