# Fnotes.py
Fnotes for py

#Lab project initialization

To proceed with this project we need to have ubuntu preinstalled on VM <br/>

After that we need to install pyenv<br/>
to proceed with automatic installation visit https://github.com/pyenv/pyenv-installer

Step by step:<br/>

- Once prerequisites have been installed correctly:

`$ curl https://pyenv.run | bash'`

- pyenv.run redirects to the install script in this repository and the invocation above is equivalent to:<br/>

`$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash`

- Restart your shell so the path changes take effect:

`$ exec $SHELL`

You can now begin using pyenv.

*dont forget to install curl `sudo apt-get install curl`

Then you need to add load path to pyenv woth your text editor

By using command `pyenv install --list` you can see all possibel versions of PY to be installed 

`pyenv install x.x.x` to install version you need 
`subl ~/.pyenv/version` to setup defailt PY version
