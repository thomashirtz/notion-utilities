from notion_utilities.properties import Title


def get_title(page: dict):
    property_name_to_dictionary = page['properties']
    for property_name, dictionary in property_name_to_dictionary.items():
        if dictionary['type'] == 'title':
            return Title(property_name).get_value(dictionary)
