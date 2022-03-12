from notion_utilities.main import edit_properties
from notion_utilities.properties import Formula, RichText


def copy(source_value):  # unpacked values of the properties retrieved using source_list
    return [source_value]  # list of values that will be attributed to target_list


token = ''
database_id = ''

if __name__ == '__main__':
    # Example of usage: copy the content from the property named 'F1' to
    # the rich-text property named 'RT1'
    edit_properties(
        token=token,
        database_id=database_id,
        source_list=[Formula('F1')],
        target_list=[RichText('RT1')],
        editer=copy,
    )
