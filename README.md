Psync
==
Psync (inspired by grsync) makes it easy to use rsync with multiple apps/sites. 

Just edit  the config file (`psync.ini`) and add your local and remote paths. 
Give each app or project a short name and you're done.

Setup
==
> In the examples below, the command used is psync. You can create an alias, for example `push`, if you want to do that. If you don't know how, read to the end.

Add your local and remote paths by editing `psync.ini`:

```ini
[list]
railsapp = /home/me/railsapp/    user@remote.com:/home/railsapp/
```

If both your local and remote paths are identical, use the keyword `:same` in the remote value:

```ini
[list]
myfile = /home/myfile.php   user@1.1.1.1:same
myapp  = /home/myapp/       serverhost:same
```
> You can escape spaces in path names using a backslash (e.g. `my\ file`). Additionally, the conf file has a settings section where you can specify paths you'd like to exclude. The default settings will exclude `.git/` and `.DS_Store`.

Usage
==
Normal sync (-a):

    psync railsapp
    psync myfile

Specify a custom file path for config file:

    psync -f /path/to/psync.ini
    
or
    
    psync --conf=/path/to/psync.ini

> By default, the script will look for the config file in your current working directory. You can set a different config path through the above option or by editing the code. The latter option isn't reccomended.
> 
> Additionally, you can set the custom file path if you create an alias (e.g. `push`) to use the shorter command in your normal workflow. Read the **Alias** section at the end for more details.


Sync but delete extraneous files (-d):

    psync -d railsapp
    
Show the rsync command and exit (-s) or (-c):

    psync -s railsapp
    psync -c railsapp

List all the apps (or files) that you've added (-l) or (--list):

    psync -l
    psync --list
    
The output should be something like this:
    
    myapp       /home/myapp/        serverhost:/home/myapp/
    myfile      /home/myfile.php    user@1.1.1.1:/home/myfile.php
    railsapp    /home/me/railsapp/  user@remote.com:/home/railsapp/
    
### Alias with `psync` or `push`

To acess psync.py with `psync` add the following to `.bashrc` or `.profile` on Mac:

    alias psync='/path/to/psync.py'

To access it with `push` simply name the alias `push` :)

    alias push='/path/to/psync.py'

> Note: you may encounter errors if you use the short `~/path` versions of files or directories in your alias. To prevent any errors, use the full path starting with `/path`.
    
To specify a custom config file path with `push` use the `-f` or `--conf` option:

    alias push='/path/to/psync.py --conf=/path/to/psync.ini'

> Final note: if you want to specify additional rsync options when you run psync, run the show command and exit with (-s) or (-c) and add your options accordingly when running the rsync command.
