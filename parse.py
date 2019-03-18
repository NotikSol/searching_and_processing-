import re
cell = ['8:00', 'ИСТОРИЯ\xa0(пр)\nпроф.\xa0Дианов\xa0С.А. 413\xa0к.А\xa0(ЭТФ)']
def parse(cell):
	item = cell[0]
	time = item

	item = cell[1]
	lecture = item.split(')')[0] + ')'

	rr = r".*?\)(.*?)\d"
	item = cell[1]
	teacher = re.findall(rr, item.replace('\n', ' '))[0]#.replace('\xa0', ' ').strip()

	rr = r"(\d.*?)\)"
	item = cell[1]	
	room = re.findall(rr, item.replace('\n', ' '))[0]#.replace('\xa0', ' ').strip() + ')'
	
	print(time, lecture, teacher, room)#test
	return time, lecture, teacher, room


if __name__ == '__main__':
	print(parse(cell))
