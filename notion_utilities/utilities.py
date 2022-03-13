from notion_utilities.properties import Title
import collections
from typing import Any


def get_title(page: dict) -> str:
    property_name_to_dictionary = page['properties']
    for property_name, dictionary in property_name_to_dictionary.items():
        if dictionary['type'] == 'title':
            return Title(property_name).get_value(dictionary)


def is_sequence(obj: Any) -> bool:
    if isinstance(obj, str):
        return False
    return isinstance(obj, collections.abc.Sequence)  # noqa


def to_list(obj: Any) -> list:
    return obj if is_sequence(obj) else [obj]
