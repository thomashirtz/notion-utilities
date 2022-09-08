from abc import ABC
from typing import Any
from typing import Optional
from typing import List
from typing import Union

from notion_utilities.utilities import fallback, find


# todo add possibility give dict input
# todo how to manage staticmethod
# todo find way to simplify
# keep formatting
# use at your own danger => will never touch the source, so if you want to be sure to not loose data put it in new one
# change to property dict
# get_value(nexted_structure: Union|list, dict], path: list) -> Any find


class Property(ABC):
    def __init__(self, name):
        self.name = name

    def get_object(self, value: Any) -> dict:
        raise NotImplementedError

    def get_value(self, object_dict: dict) -> Any:
        raise NotImplementedError


class Title(Property):
    def get_value(self, object_dict: dict) -> Optional[str]:
        return find(object_dict, ['title', 0, 'text', 'content'])

    def get_object(self, value: Optional[str]) -> dict:
        return fallback(
            condition=value,
            default_value={'title': [{'text': {'content': value}}]},
            fallback_value={'title': []}
        )


class RichText(Property):
    def get_value(self, object_dict: dict) -> Optional[str]:
        # The default behavior is to give an empty string if it is empty, however
        # it doesn't mix well with the other properties, it is therefore coerced
        # into `None` if empty.
        content = find(object_dict, ['rich_text', 0, 'text', 'content'])
        return content if content != '' else None

    def get_object(self, value: Optional[str]) -> dict:
        value = '' if value is None else value
        return {'rich_text': [{'text': {'content': value}}]}


class Number(Property):
    def get_value(self, object_dict: dict) -> Any:
        return object_dict['number']

    def get_object(self, value: str) -> dict:
        return {'number': value}


class URL(Property):
    def get_value(self, object_dict: dict) -> str:
        return object_dict['number']

    def get_object(self, value: str) -> dict:
        return {'number': value}


class Checkbox(Property):
    def get_value(self, object_dict: dict) -> Any:
        return object_dict['checkbox']

    def get_object(self, value: str) -> dict:
        return {'checkbox': value}


class Formula(Property):
    def get_value(self, object_dict: dict) -> Any:
        formula_type = object_dict['formula']['type']
        return object_dict['formula'][formula_type]


class Select(Property):
    def get_value(self, object_dict: dict) -> str:
        return object_dict['select']['name']

    def get_object(self, value: str) -> dict:
        return {'select': {'name': value}}


class Status(Property):
    def get_value(self, object_dict: dict) -> str:
        status = object_dict['status']
        return '' if status is None else status['name']

    def get_object(self, value: Optional[str]) -> dict:
        if value is None or not value:
            return {'status': None}
        else:
            return {'status': {'name': value}}
