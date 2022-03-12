from typing import Any
from typing import Callable
from typing import List

from notion_client import Client

from notion_utilities.properties import Property, Title
from notion_utilities.query import query_database
from notion_utilities.utilities import get_title


def apply_to_database(
        token: str,
        database_id: str,
        function: Callable[..., List[Any]],
        source_property_list: List[Property],
        target_property_list: List[Property],
        page_size: int = 100,
        update: bool = True
):
    client = Client(auth=token)
    page_list = query_database(client, database_id, page_size)
    for i, page in enumerate(page_list):
        args = []
        for source in source_property_list:
            args.append(source.get_value(page['properties'][source.name]))

        properties = {}
        property_name_to_value = {}
        target_value_list = function(*args)
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
