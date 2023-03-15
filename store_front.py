import datetime

from OrderProcess import OrderProcess


class Store:
    """
    This class represents a store that can check inventory, process online orders, and print out daily transactions.
    """
    def __init__(self):
        """
        Initializes Store.
        """
        self._inventory_dictionary = {}
        self._processed_order_list = []

    @property
    def inventory_dictionary(self):
        """
        Gets inventory dictionary
        :return: inventory as a dictionary
        """
        return self._inventory_dictionary

    @property
    def processed_order_dictionary(self):
        """
        Gets process order dictionary
        :return: process order as a dictionary
        """
        return self._processed_order_list

    def display_menu(self):
        """
        Creates the display menu.
        """
        try:
            user_input = None
            print("\nWelcome to the store")
            print("---------------")
            while user_input != 3:
                print("1. Process Web Orders")
                print("2. Check Inventory")
                print("3. Exit")
                string_input = input("Please select an option (1-3)")

                if string_input == "":
                    continue

                user_input = int(string_input)
                if user_input == 1:
                    path_input = input("What is the file path?")
                    self.process_web_orders(str(path_input))
                if user_input == 2:
                    self.check_inventory()
                if user_input == 3:
                    self.exit()
        except ValueError as e:
            print(e)
            print(f"Please input proper values.")
            self.display_menu()
        except FileNotFoundError as e:
            print(e)
            print(f"Please check your file path.")
            self.display_menu()

    def check_inventory(self):
        """
        Display inventory
        """
        if not self._inventory_dictionary:
            print("Inventory currently empty.")
        for value in self._inventory_dictionary.values():
            print(value[0])
            print(f"Stock status: {self.status_indicator(value[0])}\n")

    def process_web_orders(self, path):
        """
        Process web orders
        :param path: a string
        """
        order_process = OrderProcess()
        list_of_orders = order_process.read_excel_and_make_list_of_orders(path)
        for order in list_of_orders:
            factory = order.factory
            temp_dictionary = order.product_detail_dictionary
            temp_dictionary["name"] = order.name
            temp_dictionary["product_id"] = order.product_id
            if order.item.lower() == "toy":
                item = factory.create_toy(**temp_dictionary)
            elif order.item.lower() == "stuffedanimal":
                item = factory.create_stuffed_animal(**temp_dictionary)
            else:
                item = factory.create_candy(**temp_dictionary)
            if type(item) is str:
                corrupted_order = f"Order {order.order_number}, Could not process order data was corrupted, {item}"
                self._processed_order_list.append(corrupted_order)
            else:
                self.update_inventory(order, item)
                successful_order = f"Order {order.order_number}, Item {order.item}, Product ID {order.product_id}, " \
                                   f"Name {order.name}, Quantity {order.product_detail_dictionary['quantity']}"
                self._processed_order_list.append(successful_order)
        print("Orders processed!\n")

    def exit(self):
        """
        Display store daily transaction report.
        """
        if len(self._processed_order_list) == 0:
            print("\nHOLIDAY STORE - DAILY TRANSACTION REPORT (DRT) ")
            print("No orders processed.")
        else:
            print("\nHOLIDAY STORE - DAILY TRANSACTION REPORT (DRT) ")
            print(f"{datetime.datetime.now().month}-{datetime.datetime.now().day}-{datetime.datetime.now().year}"
                  f" {datetime.datetime.now().hour}-{datetime.datetime.now().minute}")
            for processed_order in self._processed_order_list:
                print(processed_order)

    def update_inventory(self, order, item):
        """
        Update inventory of store
        :param order: an Order
        :param item: an item
        """
        order_quantity = order.product_detail_dictionary["quantity"]
        if not self.find_item(item):
            self.add_item(item, 100 - order_quantity)
        else:
            current_quantity = self.check_item_quantity(item)
            if current_quantity - order_quantity < 0:
                difference = current_quantity - order_quantity
                self.set_item_quantity(item, 100 + difference)
            else:
                self.set_item_quantity(item, current_quantity - order_quantity)

    def add_item(self, item, quantity):
        """
        Add item
        :param item: an item
        :param quantity: an int
        """
        self._inventory_dictionary[item.name] = [item, quantity]

    def find_item(self, item):
        """
        Find item
        :param item: an item
        :return: item name as a string
        """
        return item.name in self._inventory_dictionary

    def check_item_quantity(self, item):
        """
        Check item quantity
        :param item: an item
        :return: item quantity as an int
        """
        return self._inventory_dictionary[item.name][1]

    def set_item_quantity(self, item, quantity):
        """
        Set item quantity
        :param item: an item
        :param quantity: quantity as an int
        """
        self._inventory_dictionary[item.name][1] = quantity

    def status_indicator(self, item):
        """
        Indicate stock status
        :param item: an item
        :return: status as a string
        """
        if self._inventory_dictionary[item.name][1] >= 10:
            return "In Stock"
        elif 10 > self._inventory_dictionary[item.name][1] >= 3:
            return "Low"
        elif 3 > self._inventory_dictionary[item.name][1] > 0:
            return "Very Low"
        else:
            return "Out of Stock"
