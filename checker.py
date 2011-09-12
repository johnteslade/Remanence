import clean_zeros

def find_match(find_in, find_in_offset, search_data, search_data_offset):
	
	matched_bytes = 0

	for i in range(find_in_offset, min(len(find_in), find_in_offset + len(search_data) - search_data_offset)):

		if find_in[i] == search_data[search_data_offset + matched_bytes]:
			matched_bytes = matched_bytes + 1
		else:
			break

	return matched_bytes

def find_byte_string(byte_string, search_byte_string):
	
	THRESHOLD = 2

	print "--- SEARCH start ---"

	for i in range(0, len(byte_string)):

		for j in range(0, len(search_byte_string) - THRESHOLD + 1):
			
			matched_bytes = find_match(byte_string, i, search_byte_string, j) 

			if matched_bytes >= THRESHOLD:
				print "search from %d, matched %d chars, search offset %d" % (i, matched_bytes, j)

	
	print "Search done"
	print "-------------"

def main():

	fh = open('core.3381', 'rb')

	ba = bytearray(fh.read())
	#ba = bytearray(b'\x00\x11\x12\x13\x22\x11\x12\x22\x22\x12\x13')

	# Strip runs of zeros
	ba_2 = clean_zeros.strip_byte_runs(ba, 0, 4)
	print "orig = %d, stripped = %d" % (len(ba), len(ba_2))

	i = 0

	#search_text = bytearray(b'\x11\x12\x13')
	#search_text = bytearray(b'\x11\x11\x22\x22')

	find_byte_string(ba_2, bytearray(b'\x11\x11\x22\x22'))
	find_byte_string(ba_2, bytearray(b'\xaa\xaa\xaa\xaa\xbb\xbb\xbb\xbb'))

main()

