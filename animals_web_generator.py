import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


with open("animals_template.html", "r") as fileobj:
  data = fileobj.readlines()
  #print(data[-4])

animals_data = load_data('animals_data.json')

output = "" # define an empty string
for animal in animals_data:
  # append information to each string
  output += '<li class="cards__item">'
  output += f"Name: {animal["name"]}<br/>\n"
  output += f"Diet: {animal["characteristics"]["diet"]}<br/>\n"
  str_locations = ','.join(animal["locations"])
  output += f"Location: {str_locations}<br/>\n"
  try:
    output += f"Type: {animal["characteristics"]["type"]}<br/>\n"
  except:
    KeyError
  output += '</li>'
  #output += "\n"

print(output)
new_data = data[-4].replace("__REPLACE_ANIMALS_INFO__", output)
data[-4] = new_data

with open("animals.html", "w") as fileobj:
  fileobj.writelines(data)
