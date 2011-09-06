

def find_match(find_in, offset, search_data):
	
	matched_bytes = 0
	
	for search_byte in search_data:
		if offset + matched_bytes >= len(find_in):
			break
		elif find_in[offset + matched_bytes] == search_byte:
			matched_bytes = matched_bytes + 1
		else:
			break
	
	return matched_bytes

fh = open('core.3381', 'rb')

#ba = bytearray(fh.read())
ba = bytearray(b'\x00\x11\x12\x13\x22\x11\x12\x22\x22\x12\x13')

i = 0

search_text = bytearray(b'\x11\x12\x13')

search_text_pos = 0

THRESHOLD = 2

# Loop once over bytes - keep list of object showing current search positions

for i in range(0, len(ba)):

	matched_bytes = find_match(ba, i, search_text) 

	if matched_bytes >= THRESHOLD:
		print "search from %d, matched %d" % (i, matched_bytes)

	



