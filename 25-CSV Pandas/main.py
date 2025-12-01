# """1st to read files"""

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# """2nd to read csv files"""
# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     # print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# """3rd to read csv files using 3rd party pandas library"""
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# """Change data to dict or list"""
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
#
# """Average in series data"""
# average_temp = 0
# for temp in temp_list:
#     average_temp = average_temp + temp
# average_temp = average_temp/len(temp_list)

# average_temp = sum(temp_list) / len(temp_list)
# average_temp = data["temp"].mean()
# print(average_temp)

# """Get data in Column"""
# max_temp = data["temp"].max()
# max_temp = data.temp.max()
# print(max_temp)

# """Get data in Row"""
# print(data[data.day == "Monday"])
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# # print(monday)
# mon_temp = monday.temp
# mon_temp_fahrenheit = (mon_temp * 9/5) + 32
#
# tuesday = data[data.day == "Tuesday"]
# tue_temp = tuesday.temp
# print(type(tue_temp))
# tue_temp_fahrenheit = (tue_temp * 9/5) + 32
# print(tue_temp_fahrenheit)

# """Create DataFrames from scratch"""
# data_dictionary = {
#     "student" : ["Amy","James","Arnold"],
#     "scores" : [76, 56, 66]
# }
#
# data_scratch = pandas.DataFrame(data_dictionary)
# data_scratch.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_fur_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_fur_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur_squirrel = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_fur_squirrel, red_fur_squirrel, black_fur_squirrel]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")