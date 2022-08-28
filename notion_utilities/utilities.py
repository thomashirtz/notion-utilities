from notion_utilities.properties import Title
import collections
from typing import Any


def get_title(page: dict) -> str:  # todo simplify code
    """Return the title of a page when a dictionary of the page is inputted.

    Args:
        page: Dict of all the Notion page properties.

    Returns:
        The title of a Notion page.
    """
    property_name_to_dictionary = page['properties']
    for property_name, dictionary in property_name_to_dictionary.items():
        if dictionary['type'] == 'title':
            return Title(property_name).get_value(dictionary)


def is_sequence(obj: Any) -> bool:
    """Check whether an object is a sequence.

    Args:
        obj: Any object to inspect.

    Returns:
        A boolean indicating if the object is a sequence.
    """
    if isinstance(obj, str):
        return False
    return isinstance(obj, collections.abc.Sequence)  # noqa


def to_list(obj: Any) -> list:
    return obj if is_sequence(obj) else [obj]
