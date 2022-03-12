from typing import Any
from typing import Callable
from typing import List

from notion_client import Client
from edit_notion.properties import Property


def query_database(client: Client, database_id: str, page_size: int = 100):
    results = []
    query = client.databases.query(
        database_id=database_id, page_size=page_size,
    )
    results.extend(query['results'])
    while query['next_cursor'] or (query['results'] is None and not results):
        query = client.databases.query(
            database_id=database_id,
            start_cursor=query['next_cursor'],
            page_size=page_size,
        )
        results.extend(query['results'])
    return results


def edit_properties(
        token: str,
        database_id: str,
        source_list: List[Property],
        target_list: List[Property],
        editer: Callable[..., List[Any]],
        page_size: int = 100,
        update: bool = True
):
    client = Client(auth=token)
    page_list = query_database(client, database_id, page_size)
    for page in page_list:
        args = []
        for source in source_list:
            value = source.get_value(page['properties'][source.name])
            args.append(value)

        properties = {}
        value_list = editer(*args)
        for v, p in zip(value_list, target_list):
            properties[p.name] = p.get_object(v)

        print(properties)
        if update:
            client.pages.update(
                page_id=page['id'],
                properties=properties
            )
