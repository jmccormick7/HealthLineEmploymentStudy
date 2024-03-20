import csv;

varnames = input("Variable Codebook (csv): ")
data_csv = input("Data (csv): ")
vardict = {}
with open(varnames, 'r', encoding="utf8") as data:
    csv_reader = csv.reader(data)
    keys = next(csv_reader)
    values = next(csv_reader)
    for key, value in zip(keys, values):
        vardict[key] = value
#print(vardict);

# Replace values with keys' values in the data CSV
output_data = []
with open(data_csv, 'r', encoding="utf8") as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
        new_row = [vardict.get(value, value) for value in row]
        output_data.append(new_row)

# Write the modified data to a new CSV file
output_csv = input("Output CSV: ")
with open(output_csv, 'w', newline='', encoding="utf8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(output_data)

print("Replacement completed and saved to", output_csv)