# Python 3.13t (experimental version) - Quick start

Python 3.13t is making the news (or atleast one corner of it) quite frequently, the major driver being the fact that this is the first version with the Global Interpreter Lock disabled.  This means that *potentially* Python is no longer constrained from being single-threaded.

Hold your horses, though, free-threaded Python has been released only experimentally.  It remains to be seen whether there's benefit (and risk) to  machine learning and analytics workloads.

This repository is to provide a helping hand in installing Python 3.13t for experimentation.


## Installation

Installation is as per users' comfort.  Based on resources available to me, I provide below steps to install the same on a Mac with M1 Pro.

Install using a package manager, Homebrew


```
 brew update && brew upgrade pyenv
 ```

and a Python version manager called pyenv

 ```
pyenv install 3.13t-dev
 ```

Your log should look similar to the following.  Once pyenv makes 3.13t available, test it by opening Python in the command line.

Hint - the first line of the command-line utility, and the fact that exit (instead of exit()) allows you to close Python, should be a sign that installation has gone well.


```
sinsrn@mld420 ~ % pyenv install 3.13t-dev           
python-build: use openssl@3 from homebrew
python-build: use readline from homebrew
Cloning https://github.com/python/cpython...
Installing Python-3.13-dev...
python-build: use readline from homebrew
python-build: use zlib from xcode sdk
Installed Python-3.13-dev to /Users/sinsrn/.pyenv/versions/3.13t-dev
sinsrn@mld420 ~ % $HOME/.pyenv/versions/3.13t-dev/bin/python3.13t
```

For regular use, however, I seriously recommend using virtual environments.


```
% $HOME/.pyenv/versions/3.13t-dev/bin/python3.13t -m venv py313t

. py313t/bin/activate

```

### How do I check this?

Run the attached [check_version.py](./check_version.py) file.

```
(py313t) % python3.13t check_version.py
```

The function is_gil_enable() should return false.


**For comparison purposes,** also install Python 3.13 (without the free-threaded option)

```
pyenv install 3.13

% $HOME/.pyenv/versions/3.13/bin/python3.13 -m venv py313

. py313/bin/activate

```

## Tests

TBD.  But, a starter program which illustrates and provides a nice intro, is [here](./gil_thread_example.py). Run with the 3.13t and just the 3.13 environment for a more apples-to-apples.

Meanwhile, some quick [reviews](./Review.md) of articles which have talked about 3.13t.

 ## References

 1. Stack Overflow [discussion](https://stackoverflow.com/questions/79122522/how-to-disable-the-gil-in-python3-13)

 2. Python installation docs for [Mac](https://docs.python.org/3/using/mac.html)


 Contact
[Sundaresh Sankaran](sundaresh.sankaran@sas.com)

