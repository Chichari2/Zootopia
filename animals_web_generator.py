import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


with open("animals_template.html", "r") as fileobj:
  data = fileobj.readlines()
  #print(data[-4])


animals_data = load_data('animals_data.json')

def serialize_animal(animal_obj):
  output = ""  # define an empty string
  output += '<li class="cards__item">'
  output += f'<div class="card__title">{animal_obj["name"]}</div>'
  output += '<p class="card__text">'
  output += f"<strong>Diet</strong>: {animal_obj["characteristics"]["diet"]}<br/>\n"
  str_locations = ','.join(animal_obj["locations"])
  output += f"<strong>Location</strong>: {str_locations}<br/>\n"
  try:
    output += f"<strong>Type</strong>: {animal_obj["characteristics"]["type"]}<br/>\n"
  except:
    KeyError
  try:
    output += f"<strong>Color</strong>: {animal_obj["characteristics"]["color"]}<br/>\n"
  except:
    KeyError
  output += '</p>'
  output += '</li>'
  return output

output = ''
for animal_obj in animals_data:
    output += serialize_animal(animal_obj)

new_data = data[-4].replace("__REPLACE_ANIMALS_INFO__", output)
data[-4] = new_data

with open("animals.html", "w") as fileobj:
  fileobj.writelines(data)
