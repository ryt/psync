#!/usr/bin/env python

"""
Manage multiple apps/sites with rsync

Basic usage:
    psync  -a appname
    psync -sa appname
    psync -da appname
    psync -l

"""
__author__  = 'Ray, github.com/ryt'
__version__ = 'psync version 0.1'
__license__ = 'MIT'

from argparse import ArgumentParser
from collections import OrderedDict
from subprocess import call


parser = ArgumentParser(description='Simple rsync interface.')
a = {}

# if you want to, you can create a separate file to store your list but this is a more compact solution

a['app1'] = ['/home/user/app1/', 'user@server1:/home/user/app1/']
a['site2'] = ['/home/user/site2/', 'server2:same'] # :same means destination_path == source_path (server2:/home/user/site2/)
a['file3'] = ['/home/user/file3.py', 'user@host:same']

apps = OrderedDict(sorted(a.items()))
  
def main():
  parser.add_argument('-a', '--app', help='start syncing with app name', metavar='app', default=False, nargs='?', const='empty')
  parser.add_argument('-l', '--list', help='list all apps and directories', action='store_true')
  parser.add_argument('-o', help='override new files on the reciever, rsync !u', action='store_true')
  parser.add_argument('-d', help='delete extra files on destination, rsync --delete', action='store_true')
  parser.add_argument('-s', help='show the rsync command used and exit', action='store_true')
  parser.add_argument('-v', '--version', action='store_true')
  args = parser.parse_args()
  
  if args.list:
    if any(apps):
      print ''
      app_list()
      print ''
    else:
      print 'No apps yet, go add some!'
  elif args.app:
    app_run(args)
  elif args.version:
    print __version__
  else:
    print 'Specify an app name, or to get a list use -l or --list'
      
def app_run(args):
  name = args.app
  if name in apps:
    dir1 = apps[name][0]
    dir2 = samef(apps[name])
    opt = '-rtpvus'
    if args.o:
      opt = '-rtpvs'
    cmd = ['rsync', opt, dir1, dir2 ]
    if args.d:
      cmd = ['rsync', opt, '--delete', dir1, dir2]
      print ' '.join(cmd)
    if args.s:
      exit()
    call(cmd)
  else:
    print "App (%s) dun't exist!" % name
      
      
def app_list():
  len1, len2, len3 = [], [], []
  for app, fol in apps.iteritems():
    len1.append(len(app))
    len2.append(len(fol[0]))
    len3.append(len(samef(fol)))
  max1, max2, max3 = max(len1), max(len2), max(len3)
  for app, fol in apps.iteritems():
    sp1 = max1-len(app)
    sp2 = max2-len(fol[0])
    sp3 = max3-len(samef(fol))
    print ' %s%s   %s%s   %s%s' % (app, spc(sp1), fol[0], spc(sp2), samef(fol), spc(sp3) )

def samef(l):
  return l[1].replace(':same', ':' + l[0]) 

def spc(num): 
  return ''.join([' ']*num) if num else ''


if __name__ == '__main__':
  main()
