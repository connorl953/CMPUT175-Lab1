"""
Exercise 2A:
Create a Python program that reads the data stored in the provided rainfall.txt, where each line
in the text file contains the name of a city, followed by whitespace, followed by the city’s annual
rainfall (in mm). Process this data so that it is grouped by annual rainfall into the following
categories: [50-60 mm), [60-70 mm), [70-80 mm), [80-90 mm), [90-100 mm], and then sorted
from lowest to highest rainfall within each category. Write this processed data to a new file
called rainfallfmt.txt, so that under each category the city name is centered in a field that is 25
characters wide and is in all uppercase letters. The city name should be followed by its rainfall,
right-aligned in a field that is 5 characters wide with 1 digit to the right of the decimal point.
"""


def main():
    with open("rainfall.txt", "r") as f:
        cities = {
            "50-60": [],
            "60-70": [],
            "70-80": [],
            "80-90": [],
            "90-100": [],
        }
        for line in f:
            line = line.strip()
            line = line.split()
            city = line[0].strip()
            rainfall = round(float(line[1].strip()), 1)
            if (rainfall >= 50 and rainfall < 60):
                cities["50-60"].append([city, rainfall])
            elif (rainfall >= 60 and rainfall < 70):
                cities["60-70"].append([city, rainfall])
            elif (rainfall >= 70 and rainfall < 80):
                cities["70-80"].append([city, rainfall])
            elif (rainfall >= 80 and rainfall < 90):
                cities["80-90"].append([city, rainfall])
            elif (rainfall >= 90 and rainfall <= 100):
                cities["90-100"].append([city, rainfall])
        with open("rainfallfmt.txt", "w") as f2:
            for category in cities:
                f2.write("[" + category + ")\n")
                for city in cities[category]:
                    f2.write(city[0].upper().center(25) + str(city[1]).rjust(5, " ") + "\n")

    pass


main()
