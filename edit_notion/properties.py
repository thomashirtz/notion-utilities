from abc import ABC
from typing import Any


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
    def get_value(self, object_dict: dict) -> Any:
        return object_dict['rich_text'][0]['text']['content']

    def get_object(self, value: str) -> dict:
        return {'rich_text': [{'text': {'content': value}}]}


class Number(Property):
    def get_value(self, object_dict: dict) -> Any:
        return object_dict['number']

    def get_object(self, value: str) -> dict:
        return {'number': value}


class URL(Property):
    def get_value(self, object_dict: dict) -> Any:
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
