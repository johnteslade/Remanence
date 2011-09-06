import pprint

# Returns byte array which runs of bytes removed
def strip_byte_runs(in_ba, run_byte, run_threshold):

	zero_run = 0

	out_ba = bytearray()

	for i in range(0, len(in_ba)):
		
		byte = in_ba[i]

		# Look for runs
		if byte == run_byte:
			zero_run = zero_run + 1
		# If end of run then add runs less that the threshold
		else:
			if zero_run > 0 and zero_run <= run_threshold:
				for i in range(0, zero_run): out_ba.append(run_byte)
			out_ba.append(byte)
			zero_run = 0

	return out_ba

def main():

	ba = bytearray(b'\xaa\x00\xbb\x00\x00\xcc\x00\x00\x00\xdd\x00\x00\x00\x00\xee\xff\xff')

	out_ba = bytearray()
	
	out_ba = strip_byte_runs(ba, 0, 2)

	pprint.pprint(ba)
	pprint.pprint(out_ba)

main()

