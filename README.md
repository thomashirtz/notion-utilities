# notion-utilities



## Use case examples:


```
from notion_utilities import apply_to_database
from notion_utilities.properties import Formula, RichText


def copy(source_value):  # unpacked values of the properties retrieved using source_list
    return [source_value]  # list of values that will be attributed to target_list


token = ''
database_id = ''

if __name__ == '__main__':
    # Example of usage: copy the content from the property named 'Input' to
    # the rich-text property named 'Output'
    apply_to_database(
        token=token,
        database_id=database_id,
        source_property_list=[Formula('Input')],
        target_property_list=[RichText('Output')],
        function=copy,
    )
```

```
import pinyin

from notion_utilities import apply_to_database
from notion_utilities.properties import RichText


def get_pinyin(source_value):  
    return [pinyin.get(source_value, format="strip")] 


token = ''
database_id = ''

if __name__ == '__main__':
    apply_to_database(
        token=token,
        database_id=database_id,
        source_property_list=[RichText('Chinese')],
        target_property_list=[RichText('Pinyin')],
        function=get_pinyin,
    )
```

# License

     Copyright 2022 Thomas Hirtz

     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.
