# Big Calculator
Its a big calculator

- Maintainer: Angad Tendulkar <angad.tendulkar@gmail.com>
- Status: Working

## Running
- Download Repo
- Have Python 3.10+ (See [Requirements](#requirements))
- `python main.py`

## Requirements
This program needs Python 3.10+ as it uses the new `match`/`case` switcher. If you plan to fork it to remove the match-case and give support to older Python versions, note that this program also uses `math.lcm()` which is only available on Python 3.9+.

## Module
This program is not available in pip, but if you would like, you can import anything in `modules/` for your own use. Importing `main.py` automatically imports all of the modules, and doesn't run the main menu (`__name__ == 'main'` thing)