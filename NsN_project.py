requesters = {'Erin': 3, 'Mary': 5, 'Sue':1, 'Frank': 2}

MAXIMUM_REQUESTS = 5

def show_requesters():
	for name, request in requesters.items():
		print '{0:5} has requested {1:5d}'.format(name, request)

def new_entry():
	new_name = raw_input('Please enter your name: ')
	new_request = int(raw_input('Enter a number of items you want: '))

	if new_name in requesters:
		total = requesters[new_name]+new_request
		if total<=MAXIMUM_REQUESTS:
			requesters[new_name] = total
			show_requesters()
		else:
			print 'You already requested the maximum.'
			show_requesters()
	else:
		if new_request<=MAXIMUM_REQUESTS:
			requesters[new_name] = new_request
			show_requesters()
		else: 
			print 'You can only have {0} items'.format(MAXIMUM_REQUESTS)
			requesters[new_name] = MAXIMUM_REQUESTS
			show_requesters()
			

new_entry()
