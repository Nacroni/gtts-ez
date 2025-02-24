# `gtts-ez`

a rushed project to make a [`gTTS`](https://pypi.org/project/gTTS/) player.

## basic syntax

`gtts-ez INPUT [ other arguments ]`

* **INPUT**: the input that `gTTS` feeds to [Google Translate](https://translate.google.com/).

## installing playsound gives a source code error

here's a simple fix:

```bash
pip install --upgrade setuptools wheel
pip install playsound
```

upgrading [`setuptools`](https://pypi.org/project/setuptools/) and most importantly [`wheel`](https://pypi.org/project/wheel/) fixes it.
