import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

for animal in animals_data:
  print(f"Name: {animal["name"]}")
  print(f"Diet: {animal["characteristics"]["diet"]}")
  str_locations = ','.join(animal["locations"])
  print(f"Location: {str_locations}")
  try:
    print(f"Type: {animal["characteristics"]["type"]}")
  except:
    KeyError
  print("")
