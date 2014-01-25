Psync
==
Psync (inspired by grsync) makes it easy to use rsync with multiple apps/sites. 

Just edit psync.py and add your source and destination paths. 
Give each app a short name and you're done.

Setup
==
> In the examples below, the command used is psync. You can create an alias if you want to do that. If you don't know how, read to the end.

Add your local and remote paths by editing psync.py:

```python
a['railsapp'] = ['/home/me/railsapp/', 'user@remote.com:/home/railsapp/']
```

If both your local and remote paths are identical:

```python
a['myfile'] = ['/home/myfile.php',  'user@1.1.1.1:same']
a['myapp']  = ['/home/myapp/',      'server1:same']
```

Usage
==
Normal sync:

    psync -a railsapp
    psync -a myfile

Sync but delete extraneous files (-d):

    psync -da railsapp

List all the apps (or files) that you've added:

    psync -l
    
The output should be something like this:
    
    myapp       /home/myapp/        server1:/home/myapp/
    myfile      /home/myfile.php    user@1.1.1.1:/home/myfile.php
    railsapp    /home/me/railsapp/  user@remote.com:/home/railsapp/

To acess psync.py with psync add the following to `.bashrc` or `.profile` on Mac:

    alias psync='/path/to/psync.py'

> Currently you can't specify additional rsync options when you run psync. Also, everything is stored in one file. If both of these things bother you, feel free to edit the script and make yourself happy.