# TinyLetter Script

> A script to send tinyletter emails from your command line

## Install

Clone, `pip install tinyapi`, `chmod a+x`, `ln -s <source> /usr/local/bin/tinyletter`.

## Usage

```
usage: tinyletter.py [-h] [--body BODY] [--title TITLE] [--id ID]
                     [-preview | -send]

optional arguments:
  -h, --help     show this help message and exit
  --body BODY    Which file to read
  --title TITLE  A title for the newsletter
  --id ID        The id of a newsletter
  -preview       preview a newsletter
  -send          Send a newsletter
```

### Example

```
tinyletter --body=/Users/richard/file --title="This is my newsletter"
# Prints id
tinyletter -preview
# Shows all ids
tinyletter -preview <id>
# Sends preview email
tinyletter -send <id>
```

## Maintainer

[@RichardLitt](https://github.com/RichardLitt).

## Contribute

Please do!

## License

[MIT](LICENSE) © 2017 Richard Littauer
