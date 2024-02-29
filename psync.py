#!/usr/bin/env python

__author__  = 'Ray, github.com/ryt'
__version__ = 'psync version 1.0.0'
__license__ = 'MIT'

import sys
from argparse import ArgumentParser
from ConfigParser import ConfigParser
from collections import OrderedDict
from subprocess import call

parser = ArgumentParser(description='A simple python wrapper to manage rsync.')

# import list of apps/projects from ini file

plist = ConfigParser()
plist.read('psync_list.ini')

# global additional rsync options
# - exclude ".git/" directories
# - to override, use the (-s) or (-c) option and run rsync directly

eopt = '--exclude=".git/"'

a = {}
for sec_name in plist.sections():
  a[sec_name] = [plist.get(sec_name, 'local'), plist.get(sec_name, 'remote')]

apps = OrderedDict(sorted(a.items()))

def main():
  parser.add_argument('-a', '--app', help='start syncing with app name', metavar='appname', default=False, nargs='?', const='empty')
  parser.add_argument('-l', '--list', help='list all apps and directories', action='store_true')
  parser.add_argument('-o', help='override new files on the reciever, rsync !u', action='store_true')
  parser.add_argument('-d', help='delete extra files on destination, rsync --delete', action='store_true')
  parser.add_argument('-s', help='show the rsync command used and exit', action='store_true')
  parser.add_argument('-c', help='show the rsync command used and exit', action='store_true')
  parser.add_argument('-v', '--version', action='store_true')
  parser.add_argument('aname', nargs='?', metavar='appname', help='start syncing with app name (-a)')
  args = parser.parse_args()
  
  if args.list:
    if any(apps):
      print ''
      app_list()
      print ''
    else:
      print 'No apps yet, go add some!'
  elif args.app or args.aname:
    app_run(args)
  elif args.version:
    print __version__
  else:
    print 'Specify an app name, or to get a list use -l or --list'
      
def app_run(args):
  name = args.app or args.aname
  if name in apps:
    dir1 = apps[name][0]
    dir2 = samef(apps[name])
    opt = '-rtpvu' if sys.platform == 'darwin' else '-rtpvus'
    if args.o:
      opt = '-rtpv' if sys.platform == 'darwin' else '-rtpvs'
    cmd = ['rsync', opt, dir1, dir2, eopt ]
    if args.d:
      cmd = ['rsync', opt, '--delete', dir1, dir2, eopt]
    if args.s or args.c:
      print ' '.join(cmd)
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
