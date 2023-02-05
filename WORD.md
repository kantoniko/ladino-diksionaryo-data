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

* Each version **must** have a field called `ladino:` with the ladino word.
* It **might** have a field called `accented:`.   On the website is shows as `kon aksan`. e.g. [solu](https://kantoniko.com/words/ladino/solu).
* Every word  **must** have one ore more `translation`. Each translation has a languages (e.g. `english:` and has one or more values.) See the examples:

This means no french translation:

```
    french: ''
```

This means the word has a single turkish translation:

```
    turkish: ev
```

This means the word has 2 English translations:

```
    english:
      - house
      - home
```


