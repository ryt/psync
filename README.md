Psync
==
Psync (inspired by grsync) makes it easy to use rsync with multiple apps/sites. 

Just edit `list.psync.conf` and add your local and remote paths. 
Give each app or project a short name and you're done.

Setup
==
> In the examples below, the command used is psync. You can create an alias, for example `push`, if you want to do that. If you don't know how, read to the end.

Add your local and remote paths by editing `list.psync.conf`:

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
You can escape spaces in path names using a backslash (e.g. `my\ file`). Additionally, the conf file has a settings section where you can specify paths you'd like to exclude. The default settings will exclude `.git/` and `.DS_Store`.

Usage
==
Normal sync (-a):

    psync railsapp
    psync myfile
    
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

To acess psync.py with `psync` add the following to `.bashrc` or `.profile` on Mac:

    alias psync='/path/to/psync.py'

To access it with `push` simply name the key 'push' :)

    alias push='/path/to/psync.py'

> Final note: if you want to specify additional rsync options when you run psync, run the show command and exit with (-s) or (-c) and add your options accordingly when running the rsync command.