import csv
from bs4 import BeautifulSoup

with open('text_5_var_8.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()
    
soup = BeautifulSoup(html_content, 'lxml')

table = soup.find('table')

with open('output_5_var_8.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    for row in table.find_all('tr'):
        cells = row.find_all(['td', 'th'])

        data = [cell.get_text(strip=True) for cell in cells]

        csv_writer.writerow(data)