#! /usr/bin/env python

import os

files = [
    # full filenames
    "var/log/apache/errors.log",
    "home/kane/images/avatars/crusader.png",
    "home/jane/documents/diary.txt",
    "home/kane/images/selfie.jpg",
    "var/log/abc.txt",
    "home/kane/.vimrc",
    "home/kane/images/avatars/paladin.png",
]

# unfolding of plain filiname list to file-tree
fs_tree = ({}, # dict of folders
           []) # list of files
for full_name in files:
    path, fn = os.path.split(full_name)
    reduce(
        # this fucction walks deep into path
        # and creates placeholders for subfolders
        lambda d, k: d[0].setdefault(k,         # walk deep
                                     ({}, [])), # or create subfolder storage
        path.split(os.path.sep),
        fs_tree
    )[1].append(fn)

print fs_tree
#({'home': (
#    {'jane': (
#        {'documents': (
#           {},
#           ['diary.txt']
#        )},
#        []
#    ),
#    'kane': (
#       {'images': (
#          {'avatars': (
#             {},
#             ['crusader.png',
#             'paladin.png']
#          )},
#          ['selfie.jpg']
#       )},
#       ['.vimrc']
#    )},
#    []
#  ),
#  'var': (
#     {'log': (
#         {'apache': (
#            {},
#            ['errors.log']
#         )},
#         ['abc.txt']
#     )},
#     [])
#},
#[])
