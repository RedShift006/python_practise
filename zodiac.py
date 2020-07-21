zodiac_name = (u'摩羯座',u'宝瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',
			   u'狮子座',u'室女座',u'天秤座',u'天蝎座',u'人马座')
# use tuple to represent dates exp: Capricornus (摩羯) between 1-28 ~ 2.19
zodiac_date = ((1,28),(2,19),(3,21),(4,21),(5,21),(6,22),
			   (7,23),(8,23),(9,23),(10,23),(11,23),(12,23))

(month, day) = (2, 15)

zodiac_day = filter(lambda x: x <= (month, day), zodiac_date)
# print(list(zodiac_day))

zodiac_index = len(list(zodiac_day))
print(zodiac_name[zodiac_index])