# GPGChat

## Set up

`pip install -U wxPython`

`pip install cryptography python-gnupg`

## Remove `info.txt`

`rm info.txt`

## Set up the GPG environment

To set up the GPG environment for GPGChat, you may need to modify the `gpgchat.py`.

Since the GPG environment vary across different platforms, on some platforms (such as MacOS), you need to set `gpgbinary='gpg2'` while on others (Windows) set `gpgbinary='gpg'`.

If both of these settings don't work for your system, please start a pull request.

## Run the demo

`pythonw gpgchat.py`