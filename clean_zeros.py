import pprint

ba = bytearray(b'\xff\x00\xff\x00\x00\xff\x00\x00\x00\x00\xff\xff\xff')

zero_run = 0
ZERO_RUN_THRESH = 2

for i in range(0, len(ba)):
	
	byte = ba[i]

	if byte == 0:
		zero_run = zero_run + 1
	else:
		if zero_run > 0 and zero_run <= ZERO_RUN_THRESH:
			print "add run of %d" % zero_run
		print byte
		zero_run = 0

pprint.pprint(ba)
