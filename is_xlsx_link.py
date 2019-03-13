def link_from_token(token):
	return token[3]

def is_xlsx_link(token = (0,0,0,"http://pstu.ru/files/file/Abitur/timetable/Raspisanie%20zanyatijj%20ADF%20OOSV-17-1m%20(osennijj%20%20do%20smeny).xlsx")):
	url = link_from_token(token)
	return url.endswith("xlsx")

if __name__ == '__main__':
	print(is_xlsx_link())
