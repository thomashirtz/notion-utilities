from abc import ABC
from typing import Any
from typing import Optional


# todo add possibility give dict input
# todo how to manage staticmethod
# todo find way to simplify


class Property(ABC):
    def __init__(self, name):
        self.name = name

    def get_object(self, value: Any) -> dict:
        raise NotImplementedError

    def get_value(self, object_dict: dict) -> Any:
        raise NotImplementedError


class Title(Property):
    def get_value(self, object_dict: dict) -> Any:
        return object_dict['title'][0]['text']['content']

    def get_object(self, value: str) -> dict:
        return {'title': [{'text': {'content': value}}]}


class RichText(Property):
    def get_value(self, object_dict: dict) -> str:
        # todo fix bug empty property
        return object_dict['rich_text'][0]['text']['content']

    def get_object(self, value: str) -> dict:
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
