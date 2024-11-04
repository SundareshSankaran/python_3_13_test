Typical articles which talk about 3.13t

1. [Medium article 1 ](https://medium.com/@varun-singh-01/python-3-13-released-top-3-features-you-must-know-in-2024-9ba4911f3e19):  (not just the free-threaded feature, but other 3.13 aspects)

   1. Improved REPL: great, now I know what "python" at the command line's called.
      Tried it [here](./img/repl_example.png). Can see benefits - quick testing of functions etc.
      Still have to press enter after one line.
      Can use arrow keys to scroll to prev / next command.
      exit instead of exit() - this is nice. exit() was a typing nightmare.
      Multiline blocks can even be pasted

      Can paste multiline blocks, and even multiline blocks with different indentation patterns ([here](./img/repl_indent_example.png))

      Coloured error message (btw, the use of the environment variable didn't seem to work.  I don't care.)


   2. GIL lock - removed if using 3.13t

   3. Random can be called from command line

   ```
   python -m random 10
   ```

2. [Medium article 2](https://medium.com/python-in-plain-english/python-3-13-is-here-cool-new-features-for-you-to-try-28798d51c977)

   1. For the most part, seems a copy
   2. REPL - additional benefit - [autocomplete](./img/autocomplete_Example.png) for functions

   3. [**Gives a nice simple GIL example**]
