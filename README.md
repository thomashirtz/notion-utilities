# notion-utilities

Library to perform basic transformation on notion database. It is possible to 
apply function on a property or combinations of properties in order to edit properties.

⚠ Use at your own risk. If you want to be safe, please apply the functions on copies of the
properties you want to edit (Or at least when testing the proper working of your code).

## Installation

```console
pip install git+https://github.com/thomashirtz/notion-utilities#egg=notion-utilities
```

## How to set up ?

### 1. Creation of an integration

Create an [integration](https://www.notion.so/my-integrations) for the notion-utilities library. The integration needs to target the workplace containing the database that will be modified.

Option needed:
- [x] Read content
- [x] Update content
- [x] Insert content

Copy the `Internal Integration Token`, it will be the `token` argument of the functions.

### 2. Share the database with the Integration

Go to your database in notion => Click on `Share` => `Invite` => Select the integration that you just created.

Copy the link of the database (simply the URL on a browser, on the application => Click on `...` => `Copy Link`).

Extract the `database_id` from the URL : `https://www.notion.so/<workspace_name>/<database_id>?v=<view_id>`

### 3. Run your scripts

Create the script that you want to run and set the `token` and the `database_id` with the one got from the [step 1](#1-creation-of-an-integration) and the [step 2](#2-share-the-database-with-the-integration), respectively.

## Examples

<details open>

  <summary><b>Add a suffix, a prefix or apply a transformation</b></summary>

  ```python
from notion_utilities import apply_to_database
from notion_utilities.properties import RichText


def add_suffix_and_prefix(value):
    return 'suffix_' + value + '_prefix'


token = ''
database_id = ''

if __name__ == '__main__':
    apply_to_database(
        token=token,
        database_id=database_id,
        source=RichText('Input'),
        target=RichText('Output'),
        function=add_suffix_and_prefix,
    )
```

</details>



<details>

  <summary><b>Possibility to use several properties and assign to several properties</b></summary>

```python
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
        function=transform,
    )
```

```python
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
        function=transform,
    )
```

</details>


<details>

  <summary><b>Property transformation (e.g. transform chinese characters to pinyin)</b></summary>

```python
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

</details>

## License

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
