def dollar_to_euro(dollar_value):
	return dollar_value * 0.89

def euro_to_yen(euro_value):
	return euro_value * 124.15

####### ↓ YOUR CODE BELOW ↓ #######
result_euros = dollar_to_euro(137)
result_yenes = euro_to_yen(result_euros)

print(result_yenes)