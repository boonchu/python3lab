#! /usr/bin/env python 

import argparse
import requests
import yaml
import re
import logging
import sys

def main():
	# parse arguments
	parser = argparse.ArgumentParser(description='args.branch')
	#### parse debugger
	parser.add_argument('--debug', action='store_true')
	#### parse branch serach
	parser.add_argument('--branch', help='Which branch to pull the plugin list from. Valid options: production, testing, alpha. Default value: production', default='production', choices=['production', 'testing', 'alpha'], dest='branch', metavar='branch')
	#### parse keyword name for search
	parser.add_argument('name', help='Name of the plugin', metavar='name', nargs='?')
	#### start parser and keep extra if available
	args, argv = parser.parse_known_args()
	sys.argv = [sys.argv[0]] + argv
	#### 
	if not args.branch:
    		print "Unable to parse, exit. Use like this example: %s --branch production puppet (--debug)" % sys.argv[0]
    		sys.exit()

	# if debug, enable debug mode and log it
	if args.debug:
		log = logging.getLogger(__name__)
		logging.basicConfig(level=logging.DEBUG)
	
	# make a request to get YAML
	req = requests.get('https://raw.github.com/aminator-plugins/metadata/%s/plugins.yml' % (args.branch))
	
	# load YAML to plugin
	plugin = yaml.load(req.text)
	
	# check if plugin is visible
	if not plugin:
    		print "Unable to find a plugin named %s. You should use the search to find the correct name or alias for the plugin you want to install" % args.name
    		sys.exit()

	# declare array of "results"
	results = []

	# add regex 
	regex = re.compile(args.name, re.I)

	# iterate elements to find name
	for name, data in plugin.items():
		matched = regex.search(name)
		if not matched:
			for alias in data['aliases']:
				matched = regex.search(alias)
				if matched:	
					break
		if matched:
			results.append("Name:        %s\nAliases:     %s\nType:        %s\nDescription: %s" % (name, ", ".join(data['aliases']), data['type'], data['description']))	
	
	if len(results) == 0:
		print "No plugins found for keyword %s" % args.name
	else:
		print "\n----------\n".join(results)

if __name__ == '__main__':
    main()
