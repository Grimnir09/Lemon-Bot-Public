# lemon-bot
Quick and easy backup bot for when notsobot is down.

## Development install
### Pre-reqs
- Rename your .env.example to .env.
- Put required tokens into .env file.
- (Optional) create sounds directory inside main folder.

### Using Pipenv
- ```pipenv --python 3.9```
- ```pipenv install```
- ```python -m bot.py```

#### Optional Vscode F5 enjoyer
```
    {
      "name": "Python: Lemon Bot",
      "type": "python",
      "request": "launch",
      "program": "bot.py",
      "console": "integratedTerminal"
    }  
```

## Heroku Deployment

### Required Heroku Buildpacks 🧰
- heroku/python
- https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
- https://github.com/xrisk/heroku-opus.git


## Dependencies 🛠️
- discord.py
- google-images-search
- pynacl
- youtube-search-python

### windows related dependencies 
- windows-curses

### Python
- Python 3.9
