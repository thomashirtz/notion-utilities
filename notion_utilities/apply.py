from typing import Any
from typing import Callable
from typing import Sequence
from typing import Union

from notion_client import Client

from notion_utilities.properties import Property
from notion_utilities.query import query_database
from notion_utilities.utilities import get_title, to_list


def apply_to_database(
        token: str,
        database_id: str,
        function: Callable[..., Any],
        source: Union[Property, Sequence[Property]],
        target: Union[Property, Sequence[Property]],
        page_size: int = 100,
        update: bool = True
) -> None:
    """Apply a transformation to the `source` using the `function` in order to
    update the `target` property(ies) of a Notion database.

    Args:
        token: Notion token used to authenticate.
        database_id: ID of the database that needs to be transformed.
        function: Function that will be applied to the database.
        source: Source property(ies).
        target: Target property(ies)
        page_size: Number of pages to fetch at each iteration.
        update: Boolean whether to update the property(ies). It can be set to
            `False` in order to inspect the resulting target property(ies).
    """
    source_property_list = to_list(source)
    target_property_list = to_list(target)

    client = Client(auth=token)
    page_list = query_database(client, database_id, page_size)

    for i, page in enumerate(page_list):
        args = []
        for source in source_property_list:
            args.append(source.get_value(page['properties'][source.name]))

        properties = {}
        property_name_to_value = {}
        target_value_list = to_list(function(*args))

        assert len(target_value_list) == len(target_property_list)

        for value, target in zip(target_value_list, target_property_list):
            properties[target.name] = target.get_object(value)
            property_name_to_value[target.name] = value

        title = get_title(page)
        print(f'{i}/{len(page_list)} - {title} \n\t{property_name_to_value}')
        if update:
            client.pages.update(
                page_id=page['id'],
                properties=properties
            )
