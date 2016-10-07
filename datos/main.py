import csv
from difflib import SequenceMatcher


def clean_parcelas():
  with open('./frentesParcelas/frentesParcelas.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    with open('./frentes_parcelas_limpio.csv', 'wb') as new_csv_file:
      csv_writer = csv.writer(new_csv_file, delimiter=';')
      for row in csv_reader:
        csv_writer.writerow([
          row[3],
          row[8],
          row[15]
        ])


def clean_coords():
  with open('./frentes_parcelas_limpio.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    with open('./frentes_parcelas_coords_limpias.csv', 'wb') as new_csv_file:
      csv_writer = csv.writer(new_csv_file, delimiter=';')

      i = 0
      for row in csv_reader:
        i += 1
        if i == 1:
          continue

        name, number, coords = row

        try:
          clean_coords = coords[17:-2]
          all_coords = clean_coords.split(',')

          lats = [float(t.split(' ')[0]) for t in all_coords]
          lat = sum(lats)/len(lats)

          lngs = [float(t.split(' ')[1]) for t in all_coords]
          lng = sum(lngs)/len(lngs)

          csv_writer.writerow([name, number, lat, lng])
        except:
          print coords

def read_parcelas():
  locations = []
  with open('./direcciones_y_sexo_sofi.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
      name, gender = row
      words = name.strip().split(' ')

      address_name = []
      address_number = 0
      successful = False
      for word in words:
        try: 
          address_number = convert_number(word)
          successful = True
        except:
          address_name.append(word)
        if successful:
          break

      locations.append([
        ' '.join(address_name),
        address_number,
        gender
      ])
  
  with open('./direcciones_y_sexo_sofi_NUMERICO.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
      name, gender = row
      words = name.strip().split(' ')

      address_name = []
      address_number = 0
      successful = False
      i = 0
      for word in words:
        try: 
          if i > 0:
            address_number = convert_number(word)
            successful = True
          else:
            address_name.append(word)  
        except:
          address_name.append(word)
        i += 1
        if successful:
          break

      locations.append([
        ' '.join(address_name),
        address_number,
        gender
      ])

  with open('./direcciones_normalizadas_sexo.csv', 'wb') as new_csv_file:
    csv_writer = csv.writer(new_csv_file, delimiter=';')
    for location in locations:
      csv_writer.writerow(location)


def convert_number(s):
  if '/' in s:
    s = s.split('/')[0]
  if '.' in s:
    s.split('.')[0]
  return int(s)


def match_locations():
  locations = []
  with open('./direcciones_normalizadas_sexo.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
      locations.append(row + [0, 0, 0])
  with open('./frentes_parcelas_coords_limpias.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    with open('./direcciones_normalizadas_sexo_y_coords.csv', 'wb') as new_csv_file:
      csv_writer = csv.writer(new_csv_file, delimiter=';')

      for i in range(len(locations)):
        csv_file.seek(0)
        for row in csv_reader:
          if len(row) == 3:
            continue
          parcela_name, numbers, lat, lng = row
          if locations[i][1] in numbers:
            location_name = locations[i][0]
            alikeness_coef = alikeness(parcela_name, location_name)
            if alikeness_coef >= locations[i][3]:
              locations[i][3] = alikeness_coef
              locations[i][4] = lat
              locations[i][5] = lng

        csv_writer.writerow(locations[i])
  
def alikeness(a, b):
  return SequenceMatcher(None, a, b).ratio()

clean_parcelas()
clean_coords()
read_parcelas()
match_locations()