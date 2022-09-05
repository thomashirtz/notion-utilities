import collections.abc
from typing import List
from typing import Sequence
from typing import TypeVar
from typing import Union
from typing import Any

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


def find(nested_structure: Union[dict, list], key_list: List[str, int]) -> Any:
    """Find a value in a nested structure using a list of keys.

    Args:
        nested_structure: Nested structure to retrieve from.
        key_list: List of the keys and indexes forming the path to the value.

    Returns:
        Value at the path's location or `None` if the path did not exist.
    """
    try:
        tmp = dict(nested_structure)
        for key in key_list:
            tmp = tmp[key]
        return tmp
    except (IndexError, KeyError, TypeError):
        return None


def fallback(
    condition: Any,
    default_value: Any,
    fallback_value: Any,
    fallback_if_none: bool = True,
    fallback_if_not: bool = True,
) -> Any:
    """Function that will give value depending on `condition`. Giving the
    `default_value` by default, and the `fallback_value` depending on if
    `condition` is evaluated as `not` or `None`.

    The fallback only happens if the specific option is activated.

    Args:
        condition: Argument used as the condition.
        default_value: Default value.
        fallback_value: Value when the fallback occurs.
        fallback_if_none: Boolean to activate the fallback if `condition` is `None`.
        fallback_if_not: Boolean to activate the fallback if `condition` is `not`.

    Returns:
        The `default_value` or the `fallback_value`.
    """
    if fallback_if_not:
        if not condition:
            return fallback_value
    if fallback_if_none:
        if condition is None:
            return fallback_value
    else:
        return default_value
