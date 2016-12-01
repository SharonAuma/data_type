def data_type(s):
	s_type =type(s)
	if s_type == str:
		return len(s)
	if s_type == None:
		return 'no value'	
	elif s_type ==bool:
		return s
	
		if s < 100:
			return "less than 100"
		elif s == 100:
			return 'equal to 100'
		else:
			return "more than 100"
	elif s_type == list:
		if len(s) < 3:
			return None
		else:
			return s[2]
