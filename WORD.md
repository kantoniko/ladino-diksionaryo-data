# Description of the format of a word-file.

## Generic information

* The spelling and even the case of both the field and the values are important.
* There is a file called [config.yaml](config.yaml) with the list of valid values for all the fields. We have this file to make it easy to verify that none of us make a typo when adding a value. We can update the accepted values any time we like to add new valid values.


## Main fields:

* `grammar:` **required** field, but it is also a bit problematic. The valid values of the field can be found in [config.yaml](config.yaml). It must have a single value.
* `id:` This field refers to the ID in the original Excel file. New words won't have it.
* `orijen:` **required** holds the origin of the word. It had a slighly mixed meaning. It holds the name of the place where this word is used in. (Currently it must have exactly one value. We'll have to change this to be able to accept more than one values.
* `kategorias:` Each word can be in one or more categories. We have a page lisging all the [categories](https://kantoniko.com/kategorias/) and we have a separate page for each category. See `kategorias` in [config.yaml](config.yaml) for valid values.
* `linguas:` In which other language do we have a similar word. (Likely the origin of the word.) See `linguas` in [config.yaml](config.yaml) for valid values.


`versions:` Each word can have 1 or more "versions". Eg. a noun or an adjective migh have a maculine-singular, masculine-plural, feminine-singular, feminine-plural version. A verb can have many conjugations. Those are stored seperately.

## version fields:

* Each version **must** have a field called `ladino:` with the ladino word. This field can only have a single value. Please don't use `;` or `,` or anything else to separate words. Each ladino spelling must have either its own entry in the `versions` or its own YAML file.
* It **might** have a field called `accented:`.   On the website is shows as `kon aksan`. e.g. [solu](https://kantoniko.com/words/ladino/solu) has it.
* Every `noun` and `pronoun` must have a field called `gender` and a field called `number`:
* `gender` valid values are listed in  [config.yaml](config.yaml) under `gender`.
* `number` valid values are listed in  [config.yaml](config.yaml) under `numero`.
* TODO: Which other grammar-types should require a gender and number field? adjectives? others?

* `alternative-spelling` an optional list of alternative spellings of the ladino word. It can be y/i replacement as in [syelo](https://kantoniko.com/words/ladino/syelo). (TODO: An undecided topic: should synonimes have their own file or listed as alternative-spelling? The former would require the duplication of the translation, but it might be the more correct way.)


* Every version  **must** have an entry called `translations` with at least one language in it. Each translation has a languages (e.g. `english:` and has one or more values.) See the examples:

This means no french translation:

```
    french: ''
```

This means the word has a single turkish translation:

```
    turkish: ev
```

If a word has more than one translations we can list them this way. This word has 2 English translations:

```
    english:
      - house
      - home
```

If a word has two subtsantially different meaning in Ladino (e.g. the word `el` can be both `he` and `the`), then we need to create two separate YAML files for these two meanings. The names of the YAML file of the words don't participate in the creation of the dictionary. They are only important for the editor to make it easier to find and recognize a file.



