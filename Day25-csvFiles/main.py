# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

print(data["temp"].mean())
print(data["temp"].max())

#get data in colums

# print(data["condition"])
print(data.condition)

#get data from rows

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print((monday.temp[0] * 9/5) + 32 )

#create data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("new_data.csv")