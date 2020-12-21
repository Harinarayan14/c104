import csv
with open("SOCR-HeightWeight.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
height_data = []
for i in range(len(file_data)):
    height=file_data[i][1]
    height_data.append(float(height))
total_height=0
for l in height_data:
    total_height+=l
mean = total_height/len(height_data)
print("Mean = "+ str(mean) )
