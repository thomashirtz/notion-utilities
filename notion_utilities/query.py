from notion_client import Client


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
