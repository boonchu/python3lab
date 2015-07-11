#! /usr/bin/env python

import commands

mount = commands.getoutput('mount -v -t hfs,smfs,ntfs')
lines = mount.splitlines()

mount_points = map( lambda line: line.split()[2], lines )

print mount_points
