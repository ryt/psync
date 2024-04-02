#!/usr/bin/env python3

__author__  = 'Ray, github.com/ryt'
__version__ = 'psync version 1.1.3'
__license__ = 'MIT'

import re
import sys
from argparse import ArgumentParser
from configparser import ConfigParser
from collections import OrderedDict
from subprocess import call

parser = ArgumentParser(description='A simple python wrapper to manage rsync.')
parser.add_argument('-a', '--app', help='start syncing with app name', metavar='appname', default=False, nargs='?', const='empty')
parser.add_argument('-l', '--list', help='list all apps and directories', action='store_true')
parser.add_argument('-o', help='override new files on the reciever, rsync !u', action='store_true')
parser.add_argument('-d', help='delete extra files on destination, rsync --delete', action='store_true')
parser.add_argument('-s', help='show the rsync command used and exit', action='store_true')
parser.add_argument('-c', help='show the rsync command used and exit', action='store_true')
parser.add_argument('-v', '--version', action='store_true')
parser.add_argument('aname', nargs='?', metavar='appname', help='start syncing with app name (-a)')
parser.add_argument('-f', '--conf', help='set the path of the config file with list of apps')
args = parser.parse_args()


# default path of the conf file

conf = 'psync.ini'

# if a custom path is set (-f, --conf), use that path instead

if args.conf:
  conf = args.conf

def main():
  if args.list:
    if any(apps):
      print('')
      app_list()
      print('')
    else:
      print('No apps yet, go add some!')
  elif args.app or args.aname:
    app_run(args)
  elif args.version:
    print(__version__)
  else:
    print('Specify an app name, or to get a list use -l or --list')
      
def app_run(args):
  name = args.app or args.aname
  if name in apps:
    dir1 = apps[name][0]
    dir2 = samef(apps[name])
    opt = '-rtpvu' if sys.platform == 'darwin' else '-rtpvus'
    if args.o:
      opt = '-rtpv' if sys.platform == 'darwin' else '-rtpvs'
    cmd = ['rsync', opt, eopt, dir1, dir2]
    if args.d:
      cmd = ['rsync', opt, '--delete', eopt, dir1, dir2]
    if args.s or args.c:
      print(' '.join(cmd))
      exit()
    call(cmd)
  else:
    print("App (%s) dun't exist!" % name)
      
      
def app_list():
  len1, len2, len3 = [], [], []
  for app, fol in apps.items():
    len1.append(len(app))
    len2.append(len(fol[0]))
    len3.append(len(samef(fol)))
  max1, max2, max3 = max(len1), max(len2), max(len3)
  for app, fol in apps.items():
    sp1 = max1-len(app)
    sp2 = max2-len(fol[0])
    sp3 = max3-len(samef(fol))
    print(' %s%s   %s%s   %s%s' % (app, spc(sp1), fol[0], spc(sp2), samef(fol), spc(sp3) ))

def samef(l):
  return l[1].replace(':same', ':' + l[0]) 

def spc(num): 
  return ''.join([' ']*num) if num else ''

def err_nolist():
  print("App list not found in '%s'. Add a valid list or specify config file (-f, --conf) " % (conf))


# parse config file

plist = ConfigParser()
plist.read(conf)

# check the [replace] section & prepare it

rep_sec = False
if plist.has_section('replace'):
  rep_sec = True


# check the [list] section

if plist.has_section('list'):
  a = {}
  for key, val in plist.items('list'):
    vals = val.replace("\\ ", "%20")
    vals = ' '.join(vals.split()).split(' ')
    vals = [v.replace("%20", ' ') for v in vals]
    # [replace] section: if there are a list of replacements -> make substitutions
    if rep_sec:
      for rk, rv in plist.items('replace'):
        rk = re.escape(rk)
        rv = re.escape(rv)
        a[key] = [re.sub(rk, rv, vals[0]), re.sub(rk, rv, vals[1])]
    else:
      a[key] = [vals[0], vals[1]]
else:
  err_nolist()
  exit()

apps = OrderedDict(sorted(a.items()))


# global additional rsync options
# - excludes .git/ & .DS_Store by default, add more to the conf file
# - to override, edit the conf file, or use the (-s) or (-c) option and run rsync directly

eopt = ''
setexcl = plist.get('settings', 'exclude')
if setexcl:
  paths = setexcl.replace("\\ ", "%20")
  paths = ' '.join(paths.split()).split(' ')
  paths = [p.replace("%20", ' ') for p in paths]
  eopt = ' '.join(['--exclude=' + p for p in paths])



if __name__ == '__main__':
  main()
