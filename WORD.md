# Description of the format of a word-file.


* `grammar:` this is required field, but it is also a bit problematic. The valid values of the field can be found in [config.yaml](config.yaml). It must have a single value.
* `id:` This field refers to the ID in the original Excel file. New words won't have it.
* `orijen:` holds the origin of the word. It had a slighly mixed meaning. It holds the name of the place where this word is used in. (Currently it must have exactly one value. We'll have to change this to be able to accept more than one values.
* `kategorias:`



Each word can have 1 or more "versions". Eg. a noun or an adjective migh have a maculine-singular, masculine-plural, feminine-singular, feminine-plural version. A verb can have many conjugations. Those are stored seperately.

* Each word version **must** have a field called `ladino:` with the ladino word.
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


