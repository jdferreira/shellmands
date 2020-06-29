# Common commands on the shell

`shellmands` is a small program that you can use to save, in a file, commands
that you want to execute often inside the directory you are in.

It is a simple tool whose only purpose is to store the procedures inside a
single file, so that later on, when you enter the directory again, you can
easily access the useful commands in it.

`shellmands` offers two actions:

- `mand list` shows you the names of the stored procedures
- `mand map` executes the `.shellmands` file right inside the shell, defining
  functions that can then be called within the shell (it basically executes
  `source .shellmands`)

The `.shellmands` file is the sole source of scripting code use by `shellmands`.
It should define bash functions, with optional comments right above them. `mand
list` shows those comments as a description of the function.
