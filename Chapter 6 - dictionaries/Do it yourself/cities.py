cities = {
	'Katowice':{
			'Country': 'Poland'
			'Population": "292 774',
			'Fact': 'Throughout the mid-18th century, Katowice had developed into a village upon the discovery of rich coal reserves in the area.',
			},
	'Amsterdam':{
			'Country': 'Netherlands',
			'Population': '866 737',
			'Fact': 'The Amsterdam Stock Exchange is considered the oldest "modern" securities market stock exchange in the world.',
			},
	'Kiev':{
			'Country': 'Ukraine',
			'Population': '2 967 360',
			'Fact': 'Kiev is an important industrial, scientific, educational and cultural center of Eastern Europe.',
			},
	}
	
for city, fact in cities.items():
	print('All you need to know about ' + city)
	print(fact)
			
