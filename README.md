# Draws

Take a file containing comma separated values and pick a winner in a stylish way.
We made this to automate the draw that took place at the end of PyConUy 2013.

## Usage

``draws.py`` takes by default the fields `name` and `email` from a csv file.

So, if you have a `mydraw.csv` file with this content:

```bash
name,email
Pablo Ricco,pricco@sophilabs.com
Eduardo Veiga,eveiga@sophilabs.com
Richard Stallman,rms@gnu.org
Sebastian Nogara,snogara@sophilabs.com
```

It will work without any extra arguments:
```bash
./draws.py mydraw.csv
```

But you can specify your own to fit your needs.

In this example first name, last name, and email:
```bash
./draws.py sophilabs.csv --winner-label "{first} {last} <{email}>" --list-label "{first} {last}"
```
![draws.py](http://media.site.sophilabs.com/experiments/images/draws-no-logo.png "draws.py")


With the extra argument ``--logo`` you can put an ascii drawing on top of the draw.

```bash
./draws.py sophilabs.csv --logo sophilabs.logo
```

![draws.py with logo](http://media.site.sophilabs.com/experiments/images/draws-with-logo.png "draws.py with logo")

## Installation
Draws uses modules present in the python standard library, so just clone and hack.
