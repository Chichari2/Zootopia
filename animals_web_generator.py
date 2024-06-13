import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


with open("animals_template.html", "r") as fileobj:
  data = fileobj.readlines()
  #print(data[-4])

animals_data = load_data('animals_data.json')

output = ""
for animal in animals_data:
  output += f"Name: {animal["name"]}\n"
  output += f"Diet: {animal["characteristics"]["diet"]}\n"
  str_locations = ','.join(animal["locations"])
  output += f"Location: {str_locations}\n"
  try:
    output += f"Type: {animal["characteristics"]["type"]}\n"
  except:
    KeyError
  output += "\n"

new_data = data[-4].replace("__REPLACE_ANIMALS_INFO__", output)
data[-4] = new_data

with open("animals.html", "w") as fileobj:
  fileobj.writelines(data)
