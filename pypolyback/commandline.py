#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def main():

    parser = argparse.ArgumentParser(description='Pypolyback - a restful api framework.')
    parser.add_argument('-s', '--start', '--serve', 
                        action='store_true', default=False, 
                        help='starts server')
    parser.add_argument('-i','--init',
                        action='store_true', default=False, 
                        help='initialize project folder')
    parser.add_argument('-b', '--build', 
                        action='store_true', default=False, 
                        help='build project [not yet implemented]')
    parser.add_argument('-t', '--test',
                        action='store_true', default=False, 
                        help='run automated tests [not yet implemented]')
    
    args = parser.parse_args()

    if args.start:
        from pypolyback import server
        server.start()
    elif args.init:
        from pypolyback import project
        project.init()
    else:
        parser.print_help()