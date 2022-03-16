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
This program needs Python 3.10+ as it uses the new `match`/`case` switcher. 
If you plan to fork it to give support to older Python versions, 
note that this program also uses `math.lcm()` which is only available on Python 3.9+.

## Use as a module
This program is not available in pip, 
but if you would like, 
you can import anything in `modules/` for your own use. 
Importing `main.py` automatically imports all of the modules, 
and won't run the main menu (`__name__ == 'main'` thing)