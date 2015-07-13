#! /usr/bin/python
#
# O(n) mode when hash search key
# http://stackoverflow.com/questions/19103785/python-dictionary-searching

hash_items = {
		'lastName': ['Stone', 'Lee'], 
		'age': ['12'], 
		'firstName': ['Alan', 'Mary-Ann'], 
		'address': ['34 Main Street, 212 First Avenue'],
}

key = 'ssn'
value = '123-45-678'

# if key in data_dict:
# instead of 
# if key in data_dict.keys():
# As mentioned, the first is a direct hash lookup - the intended offset is computed directly, 
# and then checked - it is roughly O(1), whereas the check of keys is a linear search, which is O(n).

# if key in hash_items.keys():
if key in hash_items:
	items = hash_items[key]
	items.append('15') 	
else:
	hash_items[key] = [value]

# or replace whole code entirely with hash_items.get(key, '') + [value]

key = 'age'
value = '15'
hash_items[key] = hash_items.get(key, '') + [value]

print hash_items

# http://stackoverflow.com/questions/17340922/how-to-search-if-dictionary-value-contains-certain-string-with-python
def search_value(has, lookup):
	a = []
	for key, value in has.items():
		for v in value:
			if lookup in v:
				a.append(key)
	a = list(set(a))
	return a

# returns with key after value matched
print search_value(hash_items, 'Mary')
