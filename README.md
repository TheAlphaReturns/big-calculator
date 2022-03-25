# Big Calculator

Big as in many functions and relatively large file size.
Only uses the builtin `math` module.

- Maintainer: Angad Tendulkar <angad.tendulkar@gmail.com>
- Status: Working

## Running

- Download Repo
- Have Python 3.10+ (See [Requirements](#requirements))
- `python main.py`

## Requirements

This program needs Python 3.10+,
as it uses the new `match`/`case` switcher.
If you plan to fork it to give support to older Python versions,
note that this program also uses `math.lcm()`,
made available in Python 3.9.

## Use as a module

This program is not available in pip,
but if you would like,
you can import anything in `modules/` for your own use.
Importing `main.py` automatically imports all of the modules,
and won't run the main menu, though it will still be imported.

## Bundler.py

`bundler.py` wraps up all deps, modules, etc.,
into one python file (`calc.bundle.py`),
for use in (e.g.) Ti-84 Python Edition.
Wouldn't recommend editing the bundled file directly,
its very messy and without proper newlines.

It works by removing all `import` and `from ... import` statements,
then copying all the files into `calc.bundle.py`
in the order of the dependency tree
(`Console.py` on top, and so on)
