from edit_notion.main import edit_properties
from edit_notion.properties import Formula, RichText


def copy(source_value):
    return [source_value]


token = ''
database_id = ''

if __name__ == '__main__':
    edit_properties(
        token=token,
        database_id=database_id,
        source_list=[Formula(name='Tags')],
        target_list=[RichText(name='b')],
        editer=copy,
    )
