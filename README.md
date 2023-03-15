This program simulates inventory processing for a store that has seasonal items all year long. The program will take in bulk orders from the store's website in the form of an excel file and extracts, transforms, and load this data to be utilized in shipment ordering or cataloguing. The system will use abstract factory pattern to achieve this, identifying product families and variations.

The planning phase will be drawn out with a preliminary UML diagram to identify all the classes, attributes, and behaviors that we may need. Structure/design of classes will be maximized for code re-use, readability, and maintainability following SOLID principles and the Law of Demeter.

A sequence diagram depicts the flow of control when an order is ringed in.

Errors are handled gracefully.

Code contains an OrderProcessor class that is responsible for reading each row of the Excel file and creating and yielding an Order object. The OrderProcessor class contains a FactoryMapping which maps the holiday to the appropriate factory class. 
Each Order contains the following:

•	Order number

•	Product ID

•	Item - The type of item (Toy, StuffedAnimal and Candy)

•	Name of the item

•	A dictionary of product details. These details are the rest of the attributes of the item as specified in the excel sheet EXCEPT the name of the holiday — Easter, Christmas or Halloween.

•	The order also contains a reference to the appropriate Factory object that can create this item.


The Storefront

The system contains a Store class that is responsible for:

•	Receiving orders and maintaining its inventory

•	Getting items from a factory class if the store does not have enough stock

•	Creating the Daily Transaction Report

The first time the store receives an order for an item, it is likely that it won't have the item in it's inventory since the store will be initialized with an empty inventory. 
In the event the store receives an order for an item that it does not have inventory for, then it will go ahead and get a 100 of those items made by the corresponding factory class.



When program runs from driver.py, user is greeted with a terminal menu:

●	Process Web Orders

At the end of each day the store owner downloads an excel file of all the online orders placed that day and process them through the system. Code will prompt the user for the name of this file(ex. orders.xlsx) and uses the pandas package to read them in and process the order. The store owner can do this multiple times a day if need be.

●	Check Inventory

This allows the cashier to check what is currently in stock and will also provide a status indicator for items if the stock for this item is LOW, VERY LOW, IN STOCK, or OUT OF STOCK. Print a list of all the items, their information, and the stock status indicator
o In Stock - 10 or more items in stock 
o Low - Less than 10 items 
o Very Low - Less than 3 items 
o Out of Stock - 0 items 

●	Exit

Exits the program and prints out the daily transaction report.



The Inventory

The store maintains the following items:

Toys 
For each festive season, the store stocks a unique toy. Despite that, there are some properties of each toy that all toys have in common. These are:

•	Whether the toy is battery operated or not.

•	The minimum recommended age of the child that the toy is safe for.

•	A name

•	A description

•	Product ID (A unique combination of letters and numbers) 

The holiday specific toys are: 

1.	Santa's Workshop

The premium Christmas present, this is not a battery operated toy. The doll house comes in different varieties. They can vary in:

o	dimensions (width and height)

o	The number of rooms 

2.	RC (Remote Controlled) Spider

The RC Spider is the toy to get during Halloween. This toy is battery operated. The different varieties of spiders that are sold have the following properties:

o	Speed

o	Jump height

o	Some spiders glow in the dark, while others do not.

o	The type of spider - This can either be a Tarantula or a Wolf Spider and nothing else.


3.	Robot Bunny

The Robot Bunny is the toy for toddlers and infants out there. The toy is battery operated. These come in different varieties as well! Their properties are:

o	The number of sound effects

o	The colour - This can be either Orange, Blue, or Pink and nothing else


Stuffed Animals

All stuffed animals have the following attributes:

•	Stuffing - This can either be Polyester Fibrefill or Wool

•	Size - This can either be S, M or L

•	Fabric - This can either be Linen, Cotton or Acrylic

•	Name

•	Description

•	Product ID 


The holiday specific stuffed animals are: 

1.	Dancing Skeleton

The dancing skeleton is made out of Acrylic yarn and stuffed with Polyester Fibrefill. This skeleton is sure to add to your Halloween decorations.

o	The dancing skeleton also glows in the dark. 

2.	Reindeer

The reindeer comes with its very own personal mini sleigh and is the stuffed animal for Christmas. It is made out of Cotton and and stuffed with Wool.

o	Has a glow in the dark nose. 

3.	Easter Bunny

The Easter Bunny is made out of Linen and stuffed with Polyester Fibrefill.

o	It comes in different colours - White, Grey, Pink and Blue and nothing else. 

Candy 

All candies have the following properties:

•	A flag to check if it contains any nuts

•	A flag to check if it is lactose free

•	Name

•	Description

•	Product ID

The holiday specific candies are: 
1.	Pumpkin Caramel Toffee

The Pumpkin Caramel Toffee is Halloween themed and is not lactose free and may contain traces of nuts.

o	It comes in two varieties — Sea Salt and Regular. 

2.	Candy Canes

Candy Canes are Christmas themed. It is lactose free and does not contain nuts.

o	The stripes on the candy cane can either be Red or Green 

3.	Creme Eggs

Creme Eggs are Easter themed and are not lactose free and may contain traces of nuts.

o	Pack Size - The creme eggs come in different packets, each containing a different number of creme eggs. 





