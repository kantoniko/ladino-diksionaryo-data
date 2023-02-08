# Contribution

This explanation is currently in English only as it is much easier for me to explain in English, but it will be translated to Ladino soon.

## Requirements

All the content of [Kantoniko](https://kantoniko.com/) is in a site called [GitHub](https://github.com/). Therefore in order to contribute to the Kantoniko web site directly you need to have an account (a user) on [GitHub](https://github.com/) and you must be logged in. It is much easier to do this on a computer than on a phone. The Kantoniko project is divided into several "repositories", but for most of the editing you don't need to care about this as you will have links from Kantoniko to the exact file you need to edit.

## Editing a word

1. On the main page of Kantoniko type in the word. (e.g. `kaza`) This will show you the word and the translations of the word in a line below.
1. The word itself will be a link. Click on in. This will lead you to the detailed page of that word. For example: [kaza](https://kantoniko.com/words/ladino/kaza).
1. Somewhere on the page there is an image of a pen  📝. Click on it. This will bring you to the file in GitHub that contains the word in all of its forms we have (e.g. singular, plural, masculine, feminine where these are applicable.) with all the translations we have.
1. There is another, slightly different image pen on this page as well. Click on that now. That will allow you to change the file.
1. Make your changes. (See below for more details.)
1. When you are done, go to the bottom of the page and click on the green button called "Propose changes".
1. Then click on the green button "Create pull request".
1. There is going to be another button called "Create pull request". Click on this too.

After you clicked the 2nd "Create pull request" button, you are done. The main administrator(s) of the project will receive a notification. When they have time they will integrate your changes into the rest of the site. In the meantime you can already look for another word and the the process again.

Check the description of a [word-file](WORD.md).

### Adding a translation to a word.

Follow the process as described above.

If the key of the language already exists but it has a pair of quotes like this:
```
  spanish: ''
```

then remove these quotes.

If you'd like to add one translation then it comes after the keyword:
```
  spanish: casa
```

if you'd like to add multiple translations then they are in the lines below starting with a dash:
```
  english:
    - home
    - house
```

### Finding a word that needs translation

* On the [Kantoniko web site](https://kantoniko.com/) in the "Listas" menu item click on "Traduksiones ke faltan".
* You will see a list of languages.
* Click on one of the languages. (e.g Hebrew)
* You'll see the list of all the words we have in the dictionary where we don't have Hebrew translation.
* Click on any words and you can go to the entry on "Adding a translation to a word".



### Adding gender and/or number to a word.

Some word-files might be missing the gender and number information. Follow the above process for [editing a word](#editing-a-word).

### Adding a new version of a word.

1. Follow the above process for [editing a word](#editing-a-word).
1. When editing the file copy-paste the existing version of the word (starting from the `- ladino:` part.)
1. Update the values.
1. In the languages where you don't know the translations of this version of the word. (e.g. don't know what is the Turkish version of `houses`) then replace the value of the `turkish` field by an empty pair of single-quotes. `turkish: ''`

## Adding a new word

1. Click [here](https://github.com/kantoniko/ladino-diksionaryo-data/new/main) to open the file editor for a new file.
1. In the middle of the screen you'll see `ladino-diksionaryo-data /` followed by a place to "Name your fiel...". Type in `words/` and then the name of the file.
    * The name should be the lower-case version of the ladino word with `.yaml` extension.
    * The exact filename is only important for the editors of the dictionary.
    * If the same ladin word has multiple meanings then we'll have more than one files. In this case we need to me creative. e.g. we have
    * `el.yaml` and also `el_the.yaml` for the word [el](https://kantoniko.com/words/ladino/el)
1. For nouns, adjectives we use the most simple form of the file: the masculine-singular if it exists, the feminine-singluare otherwise.
1. Copy the content of the [minimal skeleton](skeletons/minimal.yaml) to the open editor.
1. Edit the content: Remove the lines that are not necessary. Add the required values.
1. Click on "Propose new file".
1. Click on "Create pull request"
1. Click on the 2nd "Create pull request" button.

* You are done. You can now start doing something else. The maintainers of the site are notified and they can now integrate the new file.

## Add the translation of an example

1. Find the example on Kantoniko. You can see the list of [all the examples](https://kantoniko.com/egzempios/) and you can also arrive to an example from one of the word-pages.
1. On the page of the example you'll see a pen 📝. Click on it. That will lead you to the file that contains the example. (Each example is in its own file.)
1. There is another pen on this page as well. Click on it to edit the file.
1. Edit the file.
1. Click on "Propose changes"
1. Click on "Create pull request"
1. Click on the 2nd "Create pull request".

* You are done.

## Add audio to an example

TBD

## Add a new example without audio

TBD


