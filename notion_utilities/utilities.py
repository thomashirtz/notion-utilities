import collections.abc
from typing import List
from typing import Sequence
from typing import TypeVar
from typing import Union

from notion_utilities.properties import Title

T = TypeVar('T')


def get_title(page: dict) -> str:
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


def to_list(obj: Union[Sequence[T], T]) -> List[T]:
    """Transforms an object to a list.

    Args:
        obj: Any object.

    Returns:
        The object converted in a list.
    """
    if isinstance(obj, (str, bytes)):
        return [obj]
    elif isinstance(obj, collections.abc.Sequence):
        return list(obj)
    else:
        return [obj]
