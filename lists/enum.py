#! /usr/bin/env python

my_container = ( 'Larry', 'Moe', 'Curly' )

def print_container( container ):
	list_items = list(container)
	for index, element in enumerate( list_items ):
		print ' {} {} '.format(index, element)

print print_container(my_container) 
