





def main():



    """1. Bluebell Greenhouses sells the following Spring flower bulbs. Create a dictionary that stores
    this information. Which data should be the keys (must be unique), and which should be the
    values?"""

    prices = {
        "daffodil": 0.35,
        "tulip": 0.33,
        "crocus": 0.25,
        "hyacinth": 0.75,
        "bluebell": 0.50,
    }

    """
    2. Mary has a standing order with Bluebell Greenhouses for 50 daffodil bulbs and 100 tulip
    bulbs every year. Create a new dictionary that stores this information.
    """
    customers = {
        "Mary": {
            "daffodil": 50,
            "tulip": 100,
        }
    }

    """"
    3. Demand for tulips this year has dramatically outpaced demand. As a result, the price of tulip
bulbs has increased by 25%. Update the price of tulip bulbs in the appropriate dictionary.
(Round the price per bulb to 2 decimal places.)
    """
    prices["tulip"] = round((prices["tulip"] * 1.25), 2)

    """
    4. This year, Mary would also like to try planting hyacinths. Add 30 hyacinth bulbs to the
dictionary that is storing her order.
    """

    customers["Mary"]["hyacinth"] = 30

    """
    5. Display Mary’s purchase order for this year on the screen. Each line should be formatted as
follows: bulb code(field width: 5, left aligned) * number of bulbs(field width: 4, right aligned) = $ subtotal(field width: 6, right-aligned, 2 decimal)
where the code for each bulb name is the first three letters of its name, all in capital letters.
The lines should be printed so that the bulb codes are in alphabetical order.
"""


    print("You have purchased the following bulbs:")
    total = 0
    for bulb in sorted(customers["Mary"]):
        subtotal = prices[bulb] * customers["Mary"][bulb]
        total += subtotal
        print(bulb[:3].upper().ljust(5) + " * " + str(customers["Mary"][bulb]).rjust(4) + " = " + ("$ " + str(format(subtotal, ".2f"))).rjust(6, " "))

    """
    6. Calculate the total number of bulbs that Mary purchased this year, as well as the total cost of
her order. Include this information at the bottom of her purchase order. Format the total cost
float value so that it is right-aligned in a field width of 6, with 2 decimal places 
"""
    totalBulbs = sum(customers["Mary"].values())
    totalCost = total
    print("Thank you for purchasing " + str(totalBulbs) + " bulbs from Bluebell Greenhouses.")
    print("Your total cost comes to " + ("$ " + str(format(totalCost, ".2f"))).rjust(6) + ".")


    pass


main()
