from notion_client import Client
from typing import List


def query_database(
        client: Client,
        database_id: str,
        page_size: int = 100
) -> List[dict]:
    """Query a Notion database and return the results.

    Args:
        client: Notion client.
        database_id: ID of the database.
        page_size: Number of pages to query at each iteration.

    Returns:
        List of the pages present in the database.
    """
    results = []
    query = client.databases.query(
        database_id=database_id, page_size=page_size,
    )
    results.extend(query['results'])  # todo simplify process
    while query['next_cursor'] or (query['results'] is None and not results):
        query = client.databases.query(
            database_id=database_id,
            start_cursor=query['next_cursor'],
            page_size=page_size,
        )
        results.extend(query['results'])
    return results
