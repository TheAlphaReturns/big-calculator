# Big Calculator

Big as in many functions and relatively large file size.
Only uses the builtin `math` module.

- Maintainer: TheAlphaReturns
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

It is mostly made to work with any project -- just
use `__init__.py`'s to import files from
other directories, and don't use `as` when
importing.

## Special thanks

- [@pg_4919](https://github.com/pg-4919) for the add/mult algorithm (seen in `modules/fectoring/aeq1.py class aeq1.getAddMult()`)

## License

GPL v3
