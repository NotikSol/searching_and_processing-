

def is_normal_link( token = 'http://pstu.ru/title1/aspirantu/'):
	return token.startswith("http://")


     
if __name__ == '__main__':
    print(is_normal_link())



