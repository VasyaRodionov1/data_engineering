import json
import csv

with open('text_6_var_8.json', 'r') as json_file:
    data = json.load(json_file)

with open('output_6_var_8.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    headers = data[0].keys()
    csv_writer.writerow(headers)

    for item in data:
        csv_writer.writerow(item.values())



#api json взят отсюда: https://www.geojs.io/docs/v1/endpoints/geo/ 

