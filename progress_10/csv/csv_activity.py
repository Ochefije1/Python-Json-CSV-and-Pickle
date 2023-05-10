import csv


path = "F:\data\google_stock_data.csv"
file = open(path, newline='')
reader = csv.reader(file)

header =  next(reader)
data = [row for row in reader]

print(header)
print(data[0])