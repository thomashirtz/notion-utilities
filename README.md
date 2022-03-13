# notion-utilities

Library to perform basic transformation on notion database.


## Example of use case:


### Add a suffix, a prefix or apply a transformation

```
from notion_utilities import apply_to_database
from notion_utilities.properties import RichText


def suffix_and_prefix(value):
    return 'suffix_' + value + '_prefix'


token = ''
database_id = ''

if __name__ == '__main__':
    apply_to_database(
        token=token,
        database_id=database_id,
        source=RichText('Input'),
        target=RichText('Output'),
        function=copy,
    )
```

### Possibility to use several properties and assign to several properties


```
from notion_utilities import apply_to_database
from notion_utilities.properties import RichText


def transform(input_1, input_2):  
    # some useful transformation
    return output


token = ''
database_id = ''

if __name__ == '__main__':
    apply_to_database(
        token=token,
        database_id=database_id,
        source=[RichText('Input 1'), RichText('Input 2')],
        target=RichText('Output'),
        function=get_pinyin,
    )
```

```
from notion_utilities import apply_to_database
from notion_utilities.properties import RichText


def transform(input):  
    # some useful transformation
    return output_1, output_2


token = ''
database_id = ''

if __name__ == '__main__':
    apply_to_database(
        token=token,
        database_id=database_id,
        source=RichText('Input'),
        target=[RichText('Output 1'), RichText('Output 2')],
        function=get_pinyin,
    )
```


### Property transformation (e.g. transform to pinyin)
```
import pinyin

from notion_utilities import apply_to_database
from notion_utilities.properties import RichText


def get_pinyin(chinese):  
    return pinyin.get(chinese)


token = ''
database_id = ''

if __name__ == '__main__':
    apply_to_database(
        token=token,
        database_id=database_id,
        source=RichText('Chinese'),
        target=RichText('Pinyin'),
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
