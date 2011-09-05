
fh = open('core.3381', 'rb')

ba = bytearray(fh.read())

i = 0

for byte in ba:

	if i > 10:
		break

	i = i + 1

	print byte 

