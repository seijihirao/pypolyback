#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import sys
import imp
import cyclone.web
from twisted.internet import reactor

def start():
    file_paths = []
    
    for root, subdirs, files in os.walk('./endpoints'):
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                file_paths += [{
                    'url': os.path.splitext(os.path.relpath(os.path.join(root, file), 'endpoints/'))[0],
                    'file': os.path.join(root, file)
                }]
    
    print file_paths
    
    application = cyclone.web.Application(
        [
            (
                '/' + file_path['url'],
                imp.load_source(file_path['url'].replace('/', '-'), file_path['file']).Main
            ) for file_path in file_paths
        ]
    )
    reactor.listenTCP(8888, application)
    reactor.run()