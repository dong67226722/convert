
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	Allen_count = 0
	Viki_count = 0
	At = 0
	Vt = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				At += 1
			else:
				for m in s[2:]:
					Allen_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				Vt += 1
			else:
				for m in s[2:]:
					Viki_count += len(m)

	print('Allen说了', Allen_count, '个字','传了', At, '贴图')
	print('Viki说了', Viki_count, '个字','传了', Vt, '贴图')
		# print(s)	


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():

	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)


main()