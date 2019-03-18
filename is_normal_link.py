import sys
def is_normal_link(url = "http://pstu.ru/files/file/Abitur/timetable/Raspisanie%20zanyatijj%20ADF%20OOSV-17-1m%20(osennijj%20%20do%20smeny).xlsx"):
	pass
	#print(1, token, file=sys.stderr)
	return url.startswith("http://")

    
if __name__ == '__main__':
    print(is_normal_link())



