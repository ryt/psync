Psync
==
Psync (inspired by grsync) makes it easy to use rsync with multiple apps/sites. 

Just edit `psync_list.ini` and add your local and remote paths. 
Name each section with your app or project's name and you're done.

Setup
==
> In the examples below, the command used is psync. You can create an alias, for example `push`, if you want to do that. If you don't know how, read to the end.

Add your local and remote paths by editing `psync_list.ini`:

```ini
[railsap]
local = /home/me/railsapp/
remote = user@remote.com:/home/railsapp/
```

If both your local and remote paths are identical, use the keyword `:same` in the remote value:

```ini
[myfile]
local = /home/myfile.php
remote = user@1.1.1.1:same

[myapp]
local = /home/myapp/
remote = serverhost:same
```

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